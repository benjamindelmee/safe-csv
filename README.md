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

with open('data.csv', 'r') as file_stream:
    valid = Checker.full_check(file_stream, sep=',', quotechar='"')

if valid:
    # load data.csv with pandas
```