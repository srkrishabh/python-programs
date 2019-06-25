Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not                 
class               from                or                  
continue            global              pass                

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> print("rishabh")
rishabh
>>> 
================ RESTART: /home/hduser/pythonprogs/rishabh.py ================
rishabh
>>> 
=============== RESTART: /home/hduser/pythonprogs/username.py ===============
rishabh
>>> a=5
>>> b="hello"
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(a+b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(a*b)
hellohellohellohellohello
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a.__add__(3,/)
SyntaxError: invalid syntax
>>> a.__add__(3)
8
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a.__divmod__()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.__divmod__()
TypeError: expected 1 arguments, got 0
>>> a.__divmod__(1)
(5, 0)
>>> a.__divmod__(9)
(0, 5)
>>> a.__floordiv__(9)
0
>>> a.__floordiv__()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.__floordiv__()
TypeError: expected 1 arguments, got 0
>>> a.__floordiv__(5)
1
>>> 
>>> a.__floor__(5)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.__floor__(5)
TypeError: __floor__() takes no arguments (1 given)
>>> a.__floor__()
5
>>> a=7
>>> a.__floor__()
7
>>> dir(b)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> c="hi"
>>> b+c
'hellohi'
>>> del(a)
>>> a
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> help(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    help(a)
NameError: name 'a' is not defined
>>> help(b)
No Python documentation found for 'hello'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> a=5
>>> help(a)
Help on int object:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(...)
 |      default object formatter
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      Returns size in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  bit_length(...)
 |      int.bit_length() -> int
 |      
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  from_bytes(...) from builtins.type
 |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
 |      
 |      Return the integer represented by the given array of bytes.
 |      
 |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument indicates whether two's complement is
 |      used to represent the integer.
 |  
 |  to_bytes(...)
 |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
 |      
 |      Return an array of bytes representing an integer.
 |      
 |      The integer is represented using length bytes.  An OverflowError is
 |      raised if the integer is not representable with the given number of
 |      bytes.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument determines whether two's complement is
 |      used to represent the integer.  If signed is False and a negative integer
 |      is given, an OverflowError is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> x=2
>>> y=3
>>> if x<y:
    print(x)

2
>>> x=3
>>> y=3
>>> if x<y:
	print(x)
	elif x>y:
		
SyntaxError: invalid syntax
>>> if x<y:
    print(x)	elif x>y:
	    
SyntaxError: invalid syntax
>>> if x<y:
    print(x)elif x>y:
	    
SyntaxError: invalid syntax
>>> if x<y:
    print(x)
    elif x>y:
	    
SyntaxError: invalid syntax
>>> if x<y:
    print(x)
elif x>y:
    print(y)
else:
    print(x,y)

    
3 3
>>> x=2
>>> y=3
>>> if x<y:
    print(x)
elif x>y:
    print(y)
else:
    print(x,y)

    
2
>>> i=0
>>> while i<10:
    print(i)
    i+=1

    
0
1
2
3
4
5
6
7
8
9
>>> print(i)
10
>>> while i<10:
    print(i)
    i+=1

    
>>> 
>>> 	f
SyntaxError: unexpected indent
>>> i=0
>>> i++
SyntaxError: invalid syntax
>>> i
0
>>> i=5
>>> i/5
1.0
>>> mylist=[1,2,"hello"]
>>> dir(mylist)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(mylist)

>>> type(mylist)
<class 'list'>
>>> mylist[2:3]
['hello']
>>> mylist[2:2]
[]
>>> mylist[2:1]
[]
>>> mylist=[1,2,"hello"]
>>> mylist[2:1]
[]
>>> mylist=[1,2,"hello"]
>>> mylist+=mylist
>>> print(mylist)
[1, 2, 'hello', 1, 2, 'hello']
>>> mylist=[1,2,"hello"]
>>> mylist*4
[1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello']
>>> 2 in mylist
True
>>> mylist.pop()
'hello'
>>> mylist[::-1]
[2, 1]
>>> mylist[::1]
[1, 2]
>>> mylist[:::1]
SyntaxError: invalid syntax
>>> mylist[::2]
[1]
>>> print(mylist)
[1, 2]
\
>>> mylist=[1,2,"hello"]
>>> mylist[::2]
[1, 'hello']
>>> print(mylist)
[1, 2, 'hello']
>>> mylist.pop(-1)
'hello'
>>> mylist.pop(0)
1
>>> mylist.pop(1)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    mylist.pop(1)
IndexError: pop index out of range
>>> mylist.pop(2)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    mylist.pop(2)
IndexError: pop index out of range
>>> mylist=[1,2,"hello"]
>>> mylist.pop(1)
2
>>> mylist=[1,2,"hello"]
>>> mylist.pop(-1)
'hello'
>>> mylist.pop(-1)
2
>>> mylist.pop(-1)
1
>>> mylist.pop(-1)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    mylist.pop(-1)
IndexError: pop from empty list
>>> 
>>> mylist=[1,2,"hello"]
>>> for i in my list
SyntaxError: invalid syntax
>>> for i in my list:
	
SyntaxError: invalid syntax
>>> list=[1,2,3,"hi",90]
>>> print(list)
[1, 2, 3, 'hi', 90]
>>> for i in mylist
SyntaxError: invalid syntax
>>> for i in mylist:
	print(i)

	
1
2
hello
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):
	print(-(10-i))

	
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
>>> print(i)
9
>>> for i in range(10):
	print((10-i))

	
10
9
8
7
6
5
4
3
2
1
>>> for i in range(10):
	print((9-i))

	
9
8
7
6
5
4
3
2
1
0
>>> for i in range(9):
	print((9-i))

	
9
8
7
6
5
4
3
2
1
>>> for i in range(-9):
	print((i))

	
>>> 
>>> for i in range(9,1):
	print(i)

	
>>> 
>>> 
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> range
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> for i in range(9,1[,-1)
		   
SyntaxError: invalid syntax
>>> for i in range(9,1[,-1):
		   
SyntaxError: invalid syntax
>>> for i in range(9, 1[, -1):
		   
SyntaxError: invalid syntax
>>> for i in range(9, 1[, -1]):
		   
SyntaxError: invalid syntax
>>> for i in range(9, 1,1]):
		   
SyntaxError: invalid syntax
>>> for i in range(9,1,-1):
		   print(i)

		   
9
8
7
6
5
4
3
2
>>> for i in range(9,-1,-1):
		   print(i)

		   
9
8
7
6
5
4
3
2
1
0
>>> for i in range(9,-1):
		   print(i)

		   
>>> for i in range(9,-1,0):
		   print(i)

		   
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    for i in range(9,-1,0):
ValueError: range() arg 3 must not be zero
>>> mylist[]
		   
SyntaxError: invalid syntax
>>> mylist=[]
		   
>>> for i in range(10):
		   mylist.append(i*i)

		   
>>> 
		   
>>> print(mylist)
		   
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list=[i*i for i in range(10)]
		   
>>> print(i)
		   
9
>>> print(list)
		   
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> is mylist = list
		   
SyntaxError: invalid syntax
>>> mylist is list
		   
False
>>> help()
		   

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> is
Comparisons
***********

Unlike C, all comparison operations in Python have the same priority,
which is lower than that of any arithmetic, shifting or bitwise
operation.  Also unlike C, expressions like "a < b < c" have the
interpretation that is conventional in mathematics:

   comparison    ::= or_expr (comp_operator or_expr)*
   comp_operator ::= "<" | ">" | "==" | ">=" | "<=" | "!="
                     | "is" ["not"] | ["not"] "in"

Comparisons yield boolean values: "True" or "False".

Comparisons can be chained arbitrarily, e.g., "x < y <= z" is
equivalent to "x < y and y <= z", except that "y" is evaluated only
once (but in both cases "z" is not evaluated at all when "x < y" is
found to be false).

Formally, if *a*, *b*, *c*, …, *y*, *z* are expressions and *op1*,
*op2*, …, *opN* are comparison operators, then "a op1 b op2 c ... y
opN z" is equivalent to "a op1 b and b op2 c and ... y opN z", except
that each expression is evaluated at most once.

Note that "a op1 b op2 c" doesn’t imply any kind of comparison between
*a* and *c*, so that, e.g., "x < y > z" is perfectly legal (though
perhaps not pretty).


Value comparisons
=================

The operators "<", ">", "==", ">=", "<=", and "!=" compare the values
of two objects.  The objects do not need to have the same type.

Chapter Objects, values and types states that objects have a value (in
addition to type and identity).  The value of an object is a rather
abstract notion in Python: For example, there is no canonical access
method for an object’s value.  Also, there is no requirement that the
value of an object should be constructed in a particular way, e.g.
comprised of all its data attributes. Comparison operators implement a
particular notion of what the value of an object is.  One can think of
them as defining the value of an object indirectly, by means of their
comparison implementation.

Because all types are (direct or indirect) subtypes of "object", they
inherit the default comparison behavior from "object".  Types can
customize their comparison behavior by implementing *rich comparison
methods* like "__lt__()", described in Basic customization.

The default behavior for equality comparison ("==" and "!=") is based
on the identity of the objects.  Hence, equality comparison of
instances with the same identity results in equality, and equality
comparison of instances with different identities results in
inequality.  A motivation for this default behavior is the desire that
all objects should be reflexive (i.e. "x is y" implies "x == y").

A default order comparison ("<", ">", "<=", and ">=") is not provided;
an attempt raises "TypeError".  A motivation for this default behavior
is the lack of a similar invariant as for equality.

The behavior of the default equality comparison, that instances with
different identities are always unequal, may be in contrast to what
types will need that have a sensible definition of object value and
value-based equality.  Such types will need to customize their
comparison behavior, and in fact, a number of built-in types have done
that.

The following list describes the comparison behavior of the most
important built-in types.

* Numbers of built-in numeric types (Numeric Types — int, float,
  complex) and of the standard library types "fractions.Fraction" and
  "decimal.Decimal" can be compared within and across their types,
  with the restriction that complex numbers do not support order
  comparison.  Within the limits of the types involved, they compare
  mathematically (algorithmically) correct without loss of precision.

  The not-a-number values "float('NaN')" and "Decimal('NaN')" are
  special.  They are identical to themselves ("x is x" is true) but
  are not equal to themselves ("x == x" is false).  Additionally,
  comparing any number to a not-a-number value will return "False".
  For example, both "3 < float('NaN')" and "float('NaN') < 3" will
  return "False".

* Binary sequences (instances of "bytes" or "bytearray") can be
  compared within and across their types.  They compare
  lexicographically using the numeric values of their elements.

* Strings (instances of "str") compare lexicographically using the
  numerical Unicode code points (the result of the built-in function
  "ord()") of their characters. [3]

  Strings and binary sequences cannot be directly compared.

* Sequences (instances of "tuple", "list", or "range") can be
  compared only within each of their types, with the restriction that
  ranges do not support order comparison.  Equality comparison across
  these types results in inequality, and ordering comparison across
  these types raises "TypeError".

  Sequences compare lexicographically using comparison of
  corresponding elements, whereby reflexivity of the elements is
  enforced.

  In enforcing reflexivity of elements, the comparison of collections
  assumes that for a collection element "x", "x == x" is always true.
  Based on that assumption, element identity is compared first, and
  element comparison is performed only for distinct elements.  This
  approach yields the same result as a strict element comparison
  would, if the compared elements are reflexive.  For non-reflexive
  elements, the result is different than for strict element
  comparison, and may be surprising:  The non-reflexive not-a-number
  values for example result in the following comparison behavior when
  used in a list:

     >>> nan = float('NaN')
     >>> nan is nan
     True
     >>> nan == nan
     False                 <-- the defined non-reflexive behavior of NaN
     >>> [nan] == [nan]
     True                  <-- list enforces reflexivity and tests identity first

  Lexicographical comparison between built-in collections works as
  follows:

  * For two collections to compare equal, they must be of the same
    type, have the same length, and each pair of corresponding
    elements must compare equal (for example, "[1,2] == (1,2)" is
    false because the type is not the same).

  * Collections that support order comparison are ordered the same
    as their first unequal elements (for example, "[1,2,x] <= [1,2,y]"
    has the same value as "x <= y").  If a corresponding element does
    not exist, the shorter collection is ordered first (for example,
    "[1,2] < [1,2,3]" is true).

* Mappings (instances of "dict") compare equal if and only if they
  have equal *(key, value)* pairs. Equality comparison of the keys and
  values enforces reflexivity.

  Order comparisons ("<", ">", "<=", and ">=") raise "TypeError".

* Sets (instances of "set" or "frozenset") can be compared within
  and across their types.

  They define order comparison operators to mean subset and superset
  tests.  Those relations do not define total orderings (for example,
  the two sets "{1,2}" and "{2,3}" are not equal, nor subsets of one
  another, nor supersets of one another).  Accordingly, sets are not
  appropriate arguments for functions which depend on total ordering
  (for example, "min()", "max()", and "sorted()" produce undefined
  results given a list of sets as inputs).

  Comparison of sets enforces reflexivity of its elements.

* Most other built-in types have no comparison methods implemented,
  so they inherit the default comparison behavior.

User-defined classes that customize their comparison behavior should
follow some consistency rules, if possible:

* Equality comparison should be reflexive. In other words, identical
  objects should compare equal:

     "x is y" implies "x == y"

* Comparison should be symmetric. In other words, the following
  expressions should have the same result:

     "x == y" and "y == x"

     "x != y" and "y != x"

     "x < y" and "y > x"

     "x <= y" and "y >= x"

* Comparison should be transitive. The following (non-exhaustive)
  examples illustrate that:

     "x > y and y > z" implies "x > z"

     "x < y and y <= z" implies "x < z"

* Inverse comparison should result in the boolean negation. In other
  words, the following expressions should have the same result:

     "x == y" and "not x != y"

     "x < y" and "not x >= y" (for total ordering)

     "x > y" and "not x <= y" (for total ordering)

  The last two expressions apply to totally ordered collections (e.g.
  to sequences, but not to sets or mappings). See also the
  "total_ordering()" decorator.

* The "hash()" result should be consistent with equality. Objects
  that are equal should either have the same hash value, or be marked
  as unhashable.

Python does not enforce these consistency rules. In fact, the
not-a-number values are an example for not following these rules.


Membership test operations
==========================

The operators "in" and "not in" test for membership.  "x in s"
evaluates to "True" if *x* is a member of *s*, and "False" otherwise.
"x not in s" returns the negation of "x in s".  All built-in sequences
and set types support this as well as dictionary, for which "in" tests
whether the dictionary has a given key. For container types such as
list, tuple, set, frozenset, dict, or collections.deque, the
expression "x in y" is equivalent to "any(x is e or x == e for e in
y)".

For the string and bytes types, "x in y" is "True" if and only if *x*
is a substring of *y*.  An equivalent test is "y.find(x) != -1".
Empty strings are always considered to be a substring of any other
string, so """ in "abc"" will return "True".

For user-defined classes which define the "__contains__()" method, "x
in y" returns "True" if "y.__contains__(x)" returns a true value, and
"False" otherwise.

For user-defined classes which do not define "__contains__()" but do
define "__iter__()", "x in y" is "True" if some value "z" with "x ==
z" is produced while iterating over "y".  If an exception is raised
during the iteration, it is as if "in" raised that exception.

Lastly, the old-style iteration protocol is tried: if a class defines
"__getitem__()", "x in y" is "True" if and only if there is a non-
negative integer index *i* such that "x == y[i]", and all lower
integer indices do not raise "IndexError" exception.  (If any other
exception is raised, it is as if "in" raised that exception).

The operator "not in" is defined to have the inverse true value of
"in".


Identity comparisons
====================

The operators "is" and "is not" test for object identity: "x is y" is
true if and only if *x* and *y* are the same object.  Object identity
is determined using the "id()" function.  "x is not y" yields the
inverse truth value. [4]

Related help topics: EXPRESSIONS, BASICMETHODS

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> mylist is list
False
>>> mylist
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> i=10
>>> while i>1
SyntaxError: invalid syntax
>>> while i>1:
    p=1*i
    print(p)
    i-=1

    
10
9
8
7
6
5
4
3
2
>>> while i>1:
    p=1
    p=p*i
    print(p)
    i-=1

    
>>> p=1
>>> while i>1:
    
    p=p*i
    print(p)
    i-=1

    
>>> 
>>> while i>1:
    p=p*i
    print(p)
    i-=1

    
>>> i=10
>>> p=1
>>> while i>1:
    p=p*i
    print(p)
    i-=1

    
10
90
720
5040
30240
151200
604800
1814400
3628800
>>> a={1:"hello",2:'world")
SyntaxError: EOL while scanning string literal
>>> a={1:"hello",2:'world"}
SyntaxError: EOL while scanning string literal
>>> a={1:"hello",2:"world"}
>>> type(a)
<class 'dict'>
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if D has a key k, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> a.keys()
dict_keys([1, 2])
>>> a.values()
dict_values(['hello', 'world'])
>>> a.items()
dict_items([(1, 'hello'), (2, 'world')])
>>> a{3}="hi"
SyntaxError: invalid syntax
>>> a{3}={"hi"}
SyntaxError: invalid syntax
>>> tuples=(1,2,3)
>>> x=2
>>> y=3
>>> output=x+y
>>> print(output)
5
>>> help(input)
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

>>> 
================== RESTART: /home/hduser/pythonprogs/add.py ==================
5
>>> s=input()
rock
>>> print(s)
rock
>>> def input(n)
    n=input()
    return n
    
SyntaxError: invalid syntax
>>> def input(n):
    n=input()
    return n

    
>>> sum=input(x) + input(y)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    sum=input(x) + input(y)
  File "<pyshell#212>", line 2, in input
    n=input()
TypeError: input() missing 1 required positional argument: 'n'
>>> x=0
>>> y=0
>>> sum=input(x) + input(y)
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    sum=input(x) + input(y)
  File "<pyshell#212>", line 2, in input
    n=input()
TypeError: input() missing 1 required positional argument: 'n'
>>> sum=input(n) + input(n)
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    sum=input(n) + input(n)
NameError: name 'n' is not defined
>>> a=input(n)
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    a=input(n)
NameError: name 'n' is not defined
>>> a=input(x)
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    a=input(x)
  File "<pyshell#212>", line 2, in input
    n=input()
TypeError: input() missing 1 required positional argument: 'n'
>>> def in(n):
    n=input()
    return n
    
SyntaxError: invalid syntax
>>> def input(n):
        n=input()
        return n

        
>>> print(n)
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    print(n)
NameError: name 'n' is not defined
>>> n
