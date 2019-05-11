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
  