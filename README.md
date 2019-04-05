# SafeCSV

The purpose of this script is to make **data integration** more reliable.

Practically speaking, if a CSV file passes all the checks, it is supposed to be read by Pandas without any error (**that's data integration**). One of the most common issues solved by this script is column shift.

Take care, **only the structure is assessed, not the data themselves (that's data cleaning)**. Things like number and date formating, removing of non-printable characters, etc. aren't checked here.

**Currently, the following tests are implemented:**

*If you find a scenario leading to an error during the integration but not covered in these tests, please feel free to submit a new test to enhance this script.*

- **Check 01**: Header must contain only letters, numbers or underscores
  
  This test is highly recommended but not mandatory, actually Pandas works fine with headers containing special characters. However, it's easier for data manipulation to have simple column names.
  
  Example:
  
  ```
  id,family name,prénom  # wrong header
  1,Torvalds,Linus
  2,Wozniak,Steve

  id,family_name,prenom  # correct header
  1,Torvalds,Linus
  2,Wozniak,Steve
  ```
    
- **Check 02**: Quotechar present in data must be escaped (doubled)

  If the CSV was generated with quotechars to encapsulate the strings, quotechars contained in the data must be doubled to avoid confusion.
  
  Example:
  
  ```
  ...,"John said "I like chocolate"",...  # wrong line
  
  ...,"John said ""I like chocolate""",...  # correct line
  ```

- **Check 03**: Lines must have the same number of columns

  If the CSV was generated without quotechars and the data contain separators, that will lead to an incorrect number of columns.
  
  Example:
  
  ```
  id,word,definition
  1,sea,The expanse of salt water, covering most of the earth's surface  # wrong line
  
  id,word,definition
  1,sea,The expanse of salt water covering most of the earth's surface  # correct line, or...
  1,sea,"The expanse of salt water, covering most of the earth's surface"  # correct line
  ```
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

valid = Checker.full_check('data.csv', sep=',', quotechar='"')

if valid:
    # load data.csv with pandas
```