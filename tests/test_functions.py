"""
LANGUAGE: python
WHAT IT DOES: unit tests for main functions module
CREATED: 23/02/2024
"""
import functions.functions as lf
import pytest

#---------SETUP------------
from importlib.machinery import SourceFileLoader

repo_path = '/home/cdsw/ukhsa/tests'

# map local repo so we can import local libraries
import sys
sys.path.append(repo_path)

import conftest as ct

#---------TESTS------------
class TestCleanHeader(object):
  # is upper case changed to lower?
  def test_lower(self):
    assert lf.clean_header('LOWER') == 'lower'

  # is upper case changed to lower?  
  def test_stripped(self):
    assert lf.clean_header(' text ') == 'text'
    
    # is upper case changed to lower?  
  def test_underscore(self):
    assert lf.clean_header('under score') == 'under_score'