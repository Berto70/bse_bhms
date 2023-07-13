import glob
import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy as sc
import astropy as ap

#%matplotlib inline

pd.set_option('display.max_columns', None)

def process_file(met, n_file):
    folder = f'.\data\sevn_output_Z0.{met}A1L1\data_0'
    filename = folder + f'\output_{n_file}.csv'

    file = pd.read_csv(filename)

    # select bh+star systems
    mask = ((file['RemnantType_0'] == 6) & (file['RemnantType_1'].isin([0,1,2,3,4,5]))) | ((file['RemnantType_1'] == 6) & (file['RemnantType_0'].isin([0,1,2,3,4,5])))
    bh_star_df = file[mask]

    #dividing non-interacting and interacting sys
    non_interacting_sys_df = bh_star_df[bh_star_df['BEvent'] == 0]
    interacting_sys_df = bh_star_df[bh_star_df['BEvent'] != 0]

    #selecting only binary sys
    non_int_binsys = non_interacting_sys_df[non_interacting_sys_df['Semimajor'].notna()]
    int_binsys = interacting_sys_df[interacting_sys_df['Semimajor'].notna()]

    # adding column Period fo non_int_binsys
    from astropy import constants as const
    from astropy import units as u
    semimaj = non_int_binsys['Semimajor']* const.R_sun
    mass_tot = (non_int_binsys['Mass_0'] * const.M_sun) + (non_int_binsys['Mass_1'] * const.M_sun)
    s_to_day = 60*60*24
    period = (2*m.pi*np.sqrt( semimaj**3 / (const.G * mass_tot) )) / s_to_day
    non_int_binsys.insert(loc=30, column='Period', value = period)

    # adding column Period fo int_binsys
    semimaj = int_binsys['Semimajor']* const.R_sun
    mass_tot = (int_binsys['Mass_0'] * const.M_sun) + (int_binsys['Mass_1'] * const.M_sun)
    s_to_day = 60*60*24
    period = (2*m.pi*np.sqrt( semimaj**3 / (const.G * mass_tot) )) / s_to_day
    int_binsys.insert(loc=30, column='Period', value = period)

    return non_int_binsys, int_binsys

met = input("Enter the value of met: ")
n_file = input("Enter the value of n_file: ")

process_file(met, n_file)