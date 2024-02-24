# ukhsa
- demo pipeline for UKHSA job advert

- processes custom version of sd2011 synthetic dataset into 2 derivatives:
- attributes (no disclosive columns)
- identifiers (disclosive)

source: https://rdrr.io/cran/synthpop/man/SD2011.html
I added random numbers of NULL values and an ID column for added realism

flowchart:
![alt text](flowchart.png "processing flowchart")

desk instructions:
- find file inputs/config.yml
- update parameters as required
- in particular review
- which columns to write to which outputs
- which column to hash
- review the output-column mapping in inputs/data_dictionary.csv
- run script pipeline.py
- review dictionary quality_metrics in memory
- review the engineering log in sd2011.log
