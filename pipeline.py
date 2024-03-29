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

#========SETUP==========

# import standard packages
import pandas as pd
import collections as co
import logging

# local libraries
import ukhsa.functions.functions as lf


# create empty dictionary to record quality metrics
quality_metrics = co.OrderedDict()

#------READ DATA----------
# pipeline settings
config = lf.read_yaml(f'ukhsa/inputs/config.yml')

# data dictionary
data_dictionary = pd.read_csv(f"{config['root']}{config['data_dict_path']}")

# input data
sd2011 = pd.read_csv(f"{config['root']}{config['sd2011_path']}")

# QA: record row count after reading
quality_metrics['sd2011_initial_rows'] = sd2011.shape[0]



#---------- start engineering log ---------
logging.basicConfig( filename = f"{config['root']}sd2011.log",
                     level = 'DEBUG',
                     format = "%(asctime)s - %(levelname)s - %(message)s",
                     datefmt = "%Y-%m-%d")

logging.info(f"read main input file with {quality_metrics['sd2011_initial_rows']} rows")




#--------------PARAMETERS--------------
# define columns for each output:
# ... those defined in the data dictionary
# ... please those agreed to be in both outputs
output_columns = {'attributes' : set((list(data_dictionary.loc[~data_dictionary['DISCLOSIVE']]['COLUMN']) + 
                                      config['output_columns']['attributes'] + 
                                      config['output_columns']['both'])
                                    ),
                 'identifiers' : set((list(data_dictionary.loc[data_dictionary['DISCLOSIVE']]['COLUMN']) + 
                                          config['output_columns']['both'])
                                    )}


#========CLEANING==========
# header lower case
sd2011.columns = [lf.clean_header(column) for column in sd2011.columns]

# remove records where either ymarr or workab are NULL
# restore contiguous index
sd2011 = sd2011.loc[ (sd2011['ymarr'].notna()) &
                     (sd2011['workab'].notna())].reset_index(drop = True)

# record remaining row count
quality_metrics['sd2011_filtered_rows'] = sd2011.shape[0]

# recode columns as specified
sd2011 = lf.recode(dataframe = sd2011,
                mapping = config['recode_mapping'])

#========HASH DISCLOSIVE COLUMN==========
sd2011[config['hashing']['new_id']] = lf.hash_column(sd2011[config['hashing']['old_id']])


#========DEFINE & WRITE OUTPUTS==========
for output in output_columns.keys():
  # define subset to write
  file = sd2011[ output_columns[ output ]]
  
  # record quality metrics
  quality_metrics[f'{output}_rows'] = file.shape[0]
  
  # write to .csv
  file.to_csv(f"{config['root']}{config['out_folder']}{output}.csv")
  
  # record writing on engineering log
  logging.info(f"write {output}.csv with {quality_metrics[f'{output}_rows']} rows")

  
# print metrics for review
quality_metrics
