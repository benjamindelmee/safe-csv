# ![SafeCSV](misc/safe_csv.png)

This script assesses if a CSV file is conform to the [RFC4180](https://tools.ietf.org/html/rfc4180).

It helps people dealing with **CSV generation** to ensure that their output is valid. It also helps people dealing with **data integration** to assess the validity of CSV files provided by third parties.

Tests performed by this script can be split in two categories:
- **Core tests:** assess if a file is conform to the RFC4180
- **Extended tests:** asses if a file follows some empirical good practices (like column naming convention)
 
For more information about the tests performed, please read the [tests documentation](doc/tests.md).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

First, install SafeCSV into your python environment:

```bash
python -m pip install git+https://github.com/benjamindelmee/safe-csv
```

### Usage

```python
from safecsv import Checker

# open the CSV file you want to perform tests on
with open('data.csv', 'r') as file_stream:
    
    # performs all the tests
    # (you can also specify tests="core" or tests="extended")
    valid = Checker.full_check(file_stream, sep=',', quotechar='"')

if valid:
    print('Success!')
else:
    print('Error!')
```

*output example (for a valid file):*

```
Stream: data.csv
check_core_01 ⇨ Quotechar present in data must be escaped (doubled)
check_core_02 ⇨ Lines must have the same number of columns
check_extd_01 ⇨ Header must contain only letters, numbers or underscores
Success!
```

*output example (for an invalid file):*

```
Stream: data.csv
check_core_01 ⇨ Quotechar present in data must be escaped (doubled)
check_core_02 ⇨ flaw found at line 8: Lines must have the same number of columns
Error!
```
