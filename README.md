# Binary Stellar Evolution - Dormant BH in binary system

This repo collects the material related to the project "Dormant Black Holes in Binaries from Gaia DR3" carried out during the Laboratory of Computational Physics (Mod B) course at the University of Padua.  
The supervisors are Dr. [Giuliano Iorio](mailto:giuliano.iorio@unipd.it) and [Erika Korb](mailto:erika.korb@studenti.unipd.it) from the [DEMOBLACK](http://demoblack.com/) group, whose PI is Prof. Michela Mapelli.  

In the GAIA DR3, there are many candidate stars in binary systems with a dark companion. At least two of these are confirmed to be binary systems with a dormant black hole ([Gaia BH1](https://ui.adsabs.harvard.edu/abs/2023MNRAS.518.1057E/abstract) and [Gaia BH2](https://ui.adsabs.harvard.edu/abs/2023arXiv230207880E/exportcitation)).
The objective of the project is to aid in the understanding of how these systems form and how many we expect to detect.  
The research work involves comparing data from [SEVN](https://gitlab.com/sevncodes/sevn) simulations with observations and studying the properties and formation channels of such systems.

## Project kick-off

A lighter version of the dataset to kick-off the project can be found at:

- https://www.dropbox.com/sh/c9i43kmww47kx11/AABu1FhQDSfrSXFrfKGJRBK-a?dl=0 
- https://drive.google.com/drive/folders/1gcEKSJ0L9UuOXqnratUQfg3fNhNlKk1r?usp=share_link 

The dataset repository contains a README.txt with informations about the generated data and how to read the dataset. Those are the outputs of simulations run for the paper [Iorio+22](https://ui.adsabs.harvard.edu/abs/2022arXiv221111774I/abstract), the simulations have been run with the Fiducial set of parameters described in Iorio+22. 
### Preprocessed clustering data
Here you can find a preprocessed version of the databases to use them for clustering or other analysis: https://mega.nz/folder/ngFFECqS#W2BNzX911-OsxqeEipREZg
I concatenated `output_*` files (through `Dask`), selected systems composed of a BH and a MS star and separated the databases between the interacting (`int_binsys`) and non-interactive systems (`non_int_binsys`).
You can find a `.cvs` and a `.parquet` version. After doing some test, the `.parquet` version seemed to perform better.
In order to increase the performance for K-mean clustering the `non_int_binsys` database, I will have to try to implement clustering through Dask, to see if there is any improvement.

## SEVN 
SEVN (Stellar EVolution for 𝑁-body) is a rapid binary population synthesis code. It gets as input the initial conditions of stars or binaries (masses, spin, semi-major axis, eccentricity) and evolve them. SEVN calculates stellar evolution by interpolating pre-computed sets of stellar tracks. Binary evolution is implemented by means of analytic and semi-analytic prescriptions. The main advantage of this strategy is that it makes the implementation more general and flexible: the stellar evolution models adopted in sevn can easily be changed or updated just by loading a new set of look-up tables. SEVN allows to choose the stellar tables at runtime, without modifying the internal structure of the code or even recompiling it.  

SEVN is written entirely in C++ (without external dependencies) following the object-oriented programming paradigm. SEVN exploits the CPU-parallelisation through OpenMP.  

Additional information on the technical details of  SEVN can be found in the presentation paper ([Iorio et al., 2022](https://ui.adsabs.harvard.edu/abs/2022arXiv221111774I/abstract), see also [Spera et al., 2019](https://ui.adsabs.harvard.edu/abs/2019MNRAS.485..889S/abstract)) and in the [user guide](https://gitlab.com/sevncodes/sevn/-/blob/SEVN/resources/SEVN_userguide.pdf).

### Authors and acknowledgment
The original version of SEVN was developed by  Mario Spera, Michela Mapelli and Alessandro Alberto Trani.  

The current updated version is developed and mantained by Giuliano Iorio (main developer), Mario Spera, Michela Mapelli, Guglielmo Costa and Gaston Escobar.  

The developers thanks all the people in the DEMOBLACK group for all the valuable comments and suggestions during the code development.