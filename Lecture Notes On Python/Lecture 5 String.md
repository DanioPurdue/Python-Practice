# String Operations

```python
string a
a.endwith('lo')
a.find('l')
a.split('of')
'#'.join(your_list) # a string will be returned to inteconnect every element
'1#a#xyz'.replace('#', '&')
```

# Regular Expression

package `re` 

[abc] will match any string with a, b or c

when using ^ as the first charcter, anything not a, b, nor c

`\[` is used for escape sequece

predifined sequence class

`ab*c`  -> ac, abbc, abc

` x?` will match "x" or ""

`x{1, 3} will match "x", "xx", "xxx"`



```python
match() #determine if the RE matches at the begining of the string
search() #
finall() #

import re
p = re.complie()
m = p.match('string goes here')
#you can do m.group()
p = re.complie('\d+') #plus sign should appear one and more
p.findall('string') # this will return you a list
```

 # IO

```python
f = open(filename, mode)
s = f.read()
s = f.readline() #this will include the next line character
s = f.readlines()

infile = ("myFile.txt", "r")
for line in infile:
  #process each fline here
infile.close() #<- you always close the file
f.write(s), f.flush()
```

 