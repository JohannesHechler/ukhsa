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


# import packages
import pandas as pd
import ukhsa.functions.functions as lf

#========SETUP==========

# read config
config = read_yaml('ukhsa/config.yml')

# read data dictionary

# read input data
sd2011 = pd.read_csv(config['sd2011_path'])


#========CLEANING==========
# header lower case
sd2011.columns = [clean_header(column) for column in sd2011.columns]

# filter


# recode

#========DEFINE OUTPUTS==========
# subset by column names

# write to .csv
