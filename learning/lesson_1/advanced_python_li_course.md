import statements go to the top
indent code using spaces instead of tabs
use four spaces for each indentation level
limit lines to 79 characters (72 for docstring/comments)
separate functions and classes by two blank lines
within classes, separate methods by one blank line
no spaces around function calls, indexes, keyword arguments

## Python whitespace conventions: Exercise files


## Python Truth values
- False and None evaluate to false
- Numeric zero values: 0, 0.0, 0j
- Decimal(0), Fraction(0, x)
- Empty sequences/collections: '', (), [], {}
- Empty sets and ranges: set(), range(0)

## Custom objects by default are equal to True, but if we overwrite bool method, it will be equal to False
class myClass:
  def __bool__(self):
    return False

  def __len__(self):
    return 0

## Boolean operation
- and
- or
- not

## Built-in Functions: https://docs.python.org/3/library/functions.html
