import numpy as np
import pandas as pd
import random
import math

candidates_data = pd.read_csv('../../candidates_clean.csv')

normal_df = candidates_data.copy()

def calculate_mean_and_std(dataframe, lower_bound, upper_bound, num_samples):
    samples = dataframe.apply(lambda row: np.random.uniform(row[lower_bound], row[upper_bound], size=num_samples), axis=1)
    mean = samples.apply(np.mean)
    std_dev = samples.apply(np.std)
     
    return mean, std_dev

mean_bh, std_dev_bh = calculate_mean_and_std(normal_df, 'Mass_BH_lower', 'Mass_BH_upper', 10000)

mass_bh_df = pd.DataFrame({'Mass_BH_mean': mean_bh, 'Mass_BH_std': std_dev_bh})

mean_1, std_dev_1 = calculate_mean_and_std(normal_df, 'Mass_1_lower', 'Mass_1_upper', 10000)

mass_1_df = pd.DataFrame({'Mass_1_mean': mean_1, 'Mass_1_std': std_dev_1})

mean_p, std_dev_p = calculate_mean_and_std(normal_df, 'logP_lower', 'logP_upper', 10000)

logp_df = pd.DataFrame({'logP_mean': mean_p, 'logP_std': std_dev_p})

mean_std_df = pd.concat([normal_df['source_id'], mass_bh_df, mass_1_df, logp_df], axis=1)

sampled_df = pd.DataFrame(columns=['ID', 'Mass_BH', 'Mass_1', 'logP'])

for unique_id in mean_std_df['source_id']:
    subset = mean_std_df[mean_std_df['source_id'] == unique_id]
    samples = pd.DataFrame({
        'ID': unique_id,
        'Mass_BH': np.random.normal(subset['Mass_BH_mean'], subset['Mass_BH_std'], (10000)).reshape(-1),
        'Mass_1': np.random.normal(subset['Mass_1_mean'], subset['Mass_1_std'], (10000)).reshape(-1),
        'logP': np.random.normal(subset['logP_mean'], subset['logP_std'], (10000)).reshape(-1)
    })
    
    
    #sampled_df = sampled_df.append(samples, ignore_index=True)
    sampled_df = pd.concat([sampled_df, samples], ignore_index=True)

sampled_df.to_csv('./sampled_df.csv')
