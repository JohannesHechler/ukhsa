import pandas as pd
import yaml as y

def read_yaml(file_path:str)->dict:
  """
  Reads a .yaml file from local file system

  language
  --------
  python

  returns
  -------
  dictionary

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
  0.0.1
    
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
  """
  for column in recode_mapping.keys():
    # recode according to mapping
    dataframe[ column ] = [recode_mapping[column][original_value] for original_value in dataframe[column]]

    # recode any values not expected in mapping to catchall value
    dataframe[ column ] = dataframe[ column ].fillna(0,
                                           inplace = True)
  return dataframe

def hash_column(column:pd.Series) -> list:
  return [hl.sha256(str(value).encode()) for value in column]
