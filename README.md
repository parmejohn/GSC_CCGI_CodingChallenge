# GSC CCGI Coding Challenge
Takes a low coverage file and a sample identifier, and outputs the minimum coverage and total bases affected per gene

## Dependencies
python3 >= 3.7.6

## Usage
```
python3 /path_to_directory/main.py [low_coverage_file.csv] [sample_id]
```
Ensure that the low_coverage_file contains a 'patient_id', 'Minimum.Depth', and 'Number.of.Sites' columns. 'Minimum.Depth' and 'Number.of.Sites' should be whole integer values.

Output will be printed to the command line in a tab-delimited format with the following columns
- Gene = gene name
- Minimum.Coverage = minimum coverage for the given gene
- Total.Low.Coverage = total amount of low coverage positions for the given gene


## Unit tests
To run unit tests
```
python -m unittest discover /path_to_directory/GSC_CCGI_CodingChallenge/test
```
