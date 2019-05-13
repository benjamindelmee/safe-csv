# Tests documentation

SafeCSV implements two kinds of tests:

- **Core tests:** if a file successfully passes all the core tests, it's meant to be conform to the [RFC4180](https://tools.ietf.org/html/rfc4180). More often as you think, CSV files aren't conform to the standard, especially with the *double-quote escaping* rule.

- **Extended tests:** thoses tests aren't part of the RFC standard. They asses if the file follows some empirical good practices like having unique column names or having column names free of special characters.

## Core tests

In order to implement core tests, the grammar described in the RFC was implemented as a [deterministic finite autmaton](https://en.wikipedia.org/wiki/Deterministic_finite_automaton). You can find it [here](./grammar.png).

- **Core check 01**: Quotechar present in data must be escaped (doubled)

  If the CSV was generated with quotechars to encapsulate the strings, quotechars contained in the data must be doubled to avoid confusion.
  
  Example:
  
  ```
  ...,"John said "I like chocolate"",...  # wrong line
  
  ...,"John said ""I like chocolate""",...  # correct line
  ```

- **Core check 02**: Lines must have the same number of columns

  If the CSV was generated without quotechars and the data contain separators, that will lead to an incorrect number of columns.
  
  Example:
  
  ```
  id,word,definition
  1,sea,The expanse of salt water, covering most of the earth's surface  # wrong line
  
  id,word,definition
  1,sea,The expanse of salt water covering most of the earth's surface  # correct line, or...
  1,sea,"The expanse of salt water, covering most of the earth's surface"  # correct line
  ```

## Extended tests

- **Extended check 01**: Header must contain only letters, numbers or underscores
  
  Example:
  
  ```
  id,family name,prénom  # wrong header
  1,Torvalds,Linus
  2,Wozniak,Steve

  id,family_name,prenom  # correct header
  1,Torvalds,Linus
  2,Wozniak,Steve
  ```
  