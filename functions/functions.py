import pandas as pd
import yaml as y
import hashlib as hl

def read_yaml(file_path:str)->dict:
  """
  Reads a .yaml file from local file system

  language
  --------
  python

  returns
  -------
  dictionary

  version
  -------
  0.1
  
  parameters
  ----------
  * file_path = full path to file to import
      `(datatype = string)`, e.g. '/your_repo/your_config.yaml'

  example
  -------
  >>> settings = read_yaml(file_path = 'your_repo/your_yaml_config.yaml')
  """

  # open connection to local file system
  # read data
  with open(file_path, "r") as f:
    try:
      data = y.safe_load(f)
      f.close()
    except y.YAMLError as error:
        raise error

  return data



def clean_header(column:str)->str:
  """
  Cleans column headers by trimming leading/trailing whitespace, replace spaces 
  with underscores and makes everything lowercase. 
  
  language
  --------
  python
    
  returns
  -------
  cleaned column headers 
  
  return type
  -----------
  string
  
  version
  -------
  0.1
    
  parameters
  ----------
  columns = the name of the column header that are to be cleaned
  `(datatype = string)`.

  example
  -------
  >>> clean_header('column_name')
  
  """
  return column.strip().replace(' ','_').lower()




def recode(dataframe:pd.DataFrame,
           mapping:dict) -> pd.DataFrame:
  """
  recodes columns in a dataframe according to a dictionary
  
  language
  --------
  python
    
  returns
  -------
  dataframe with selected columns recoded as specified
  
  return type
  -----------
  pandas dataframe
  
  version
  -------
  0.1
    
  parameters
  ----------
  dataframe = the name of the pandas dataframe to recode
  `(datatype = pandas dataframe)`. e.g. uk_population
  mapping = specification of old and new values for any number of columns
  `(datatype = dict)`. e.g. {'sex' : {'male'   : 1,
                                      'female' : 2},
                             'residence' : {'hhd'  : 'household',
                                            'cest' : 'communal_establishment'}
                            }

  example
  -------
  >>> recode(dataframe = uk_population,
             mapping = {'sex' : {'male'   : 1,
                                 'female' : 2},
                         'residence' : {'hhd'  : 'household',
                                        'cest' : 'communal_establishment'}
                      })
  
  """
  for column in mapping.keys():
    # recode according to mapping
    dataframe[ column ] = [mapping[column][original_value] for original_value in dataframe[column]]
    
    # recode any values not expected in mapping to catchall value
    dataframe[ column ] = dataframe[ column ].fillna(0,
                                                     inplace = False)
  return dataframe




def hash_column(column:pd.Series) -> list:
  """
  hashes values in a pandas Series according to SHA256 
  
  language
  --------
  python
    
  returns
  -------
  hashed values
  
  return type
  -----------
  list
  
  version
  -------
  0.1
    
  parameters
  ----------
  column = the name of the pandas Series to hash
  `(datatype = pandas Series)`. e.g. pds['id']

  example
  -------
  >>> hash_column(column = pds['id'])
  
  """
  return [hl.sha256(str(value).encode()) for value in column]
