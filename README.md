# ![SafeCSV](misc/safe_csv.png)

This script assesses if a CSV file is conform to the [RFC4180](https://tools.ietf.org/html/rfc4180).

It helps people dealing with **CSV generation** to ensure that their output is valid. It also helps people dealing with **data integration** to assess the validity of CSV files provided by third parties.

Tests performed by this script can be split in two categories:
- **Core tests:** assess if a file is conform to the RFC4180
- **Extended tests:** asses if a file follows some empirical good practices (like column naming convention)
 
For more information about the tests performed, please read the [tests documentation](doc/tests.md).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

```bash
sudo apt-get install git
```

### Installing

#### Automatic installation (recommended when integrated in other projects)

Add the following line to your `requirements.txt` file

```
-e git+ssh://git@github.com/benjamindelmee/SafeCSV.git#egg=safecsv
```

And then install the new requirements

```
python -m pip install -r requirements.txt
```

#### Manual installation (recommended for development)

```bash
# clone the repository
git clone
cd safecsv/

# install the module into your environment
pip install -e .
```

## Usage

```python
from safecsv import Checker

with open('data.csv', 'r') as file_stream:
    valid = Checker.full_check(file_stream, sep=',', quotechar='"')

if valid:
    # load data.csv with pandas
```