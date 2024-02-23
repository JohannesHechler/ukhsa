import pandas as pd
import pytest

@pytest.fixture(scope = 'session')
def test_data(spark_context):
  return pd.DataFrame(
    {'strVar' : ['a', ' b', 'c ', ' d ', 'A', ' B', 'C ', None, ' D '],
     'numVar' : list(range(9)),
     'strNumVar' : ['1', '2', None, '4', '5', '6', '7', '8', '9']}
  )
