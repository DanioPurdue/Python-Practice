# Class

fields or memebr variables or attibutes

methods or member functions

contructor

```python
class name:
	statements
    
```

all member functions should have `self` as parameter.

you can add attributes dynamically in python, which is different from lots of other programming languages.

static function <- you need at static

self can be both explicit and implicit

```python
p = Point(3, 4)
p,move(1, 5)
Point.move(p, 1, 5)
```

## Inheritance

```python
class Subclass (Parent class)
```

override does not need to have same function signature

## Pickle Module

`pickle.dump(x,f)` writes object x as a string into file f

x = pickle.load(f)