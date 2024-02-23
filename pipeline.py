"""
LANGUAGE: python
WHAT IT DOES:
* reads synthetic .csv file
* applies standard cleaning
* splits dataset into subset based on customer requirements
* write outputs to .csv

AUTHOR: johannes hechler
DATE: 23/02/2024
JOB REF: UKHSA01111
"""


# import standard packages
import pandas as pd
import collections as co

# local libraries
import ukhsa.functions.functions as lf

#========SETUP==========

# read config
config = read_yaml('ukhsa/config.yml')

# read data dictionary
data_dictionary = pd.read_csv(config['data_dict_path'])

# read input data
sd2011 = pd.read_csv(config['sd2011_path'])

# define columns for each output:
# ... those defined in the data dictionary
# ... please those agreed to be in both outputs
output_columns = {'attributes' : set(list(data_dictionary.loc[~data_dictionary['DISCLOSIVE']]['COLUMN']) + config['output_columns_both']),
                 'identifiers' : set(list(data_dictionary.loc[data_dictionary['DISCLOSIVE']]['COLUMN']) + config['output_columns_both'])}



quality_metrics = co.OrderedDict()

#========CLEANING==========
# header lower case
sd2011.columns = [clean_header(column) for column in sd2011.columns]

# remove records where either ymarr or workab are NULL
# restore contiguous index
sd2011 = sd2011.loc[ (sd2011['ymarr'].notna()) &
                     (sd2011['workab'].notna())].reset_index()

# recode selected columns



#========DEFINE OUTPUTS==========
# record quality metrics
# write to .csv
for output in output_columns.keys():
  file = sd2011[ output_columns[ output ]]
  
  quality_metrics[f'{output}_rows'] = file.shape[0]
  
  file.to_csv(f'{config['out_folder']}{output}.csv')