Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Basic:
	def__init__(self,name):
		
SyntaxError: invalid syntax
>>> class Basic:
	def __init__(self.name):
		self.name=name
	def show(self):
		print('basic-name:%s'%self.name)
		
SyntaxError: invalid syntax
>>> class Basic:
	def __init__(self,name):
		self.name=name
	def show(self):
		print('basic-name:%s'%self.name)

		
>>> obj1=Basic('Apricot')
>>> obj1.show()
basic-name:Apricot
>>> dir(Basic)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'show']
>>> dir(obj1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'show']
>>> help(class)
SyntaxError: invalid syntax
>>> Class definitions
*****************

A class definition defines a class object (see section The standard
type hierarchy):

   classdef    ::= [decorators] "class" classname [inheritance] ":" suite
   inheritance ::= "(" [argument_list] ")"
   classname   ::= identifier

A class definition is an executable statement.  The inheritance list
usually gives a list of base classes (see Metaclasses for more
advanced uses), so each item in the list should evaluate to a class
object which allows subclassing.  Classes without an inheritance list
inherit, by default, from the base class "object"; hence,

   class Foo:
       pass

is equivalent to

   class Foo(object):
       pass

The class’s suite is then executed in a new execution frame (see
Naming and binding), using a newly created local namespace and the
original global namespace. (Usually, the suite contains mostly
function definitions.)  When the class’s suite finishes execution, its
execution frame is discarded but its local namespace is saved. [4] A
class object is then created using the inheritance list for the base
classes and the saved local namespace for the attribute dictionary.
The class name is bound to this class object in the original local
namespace.

The order in which attributes are defined in the class body is
preserved in the new class’s "__dict__".  Note that this is reliable
only right after the class is created and only for classes that were
defined using the definition syntax.

Class creation can be customized heavily using metaclasses.

Classes can also be decorated: just like when decorating functions,

   @f1(arg)
   @f2
   class Foo: pass

is roughly equivalent to

   class Foo: pass
   Foo = f1(arg)(f2(Foo))

The evaluation rules for the decorator expressions are the same as for
function decorators.  The result is then bound to the class name.

**Programmer’s note:** Variables defined in the class definition are
class attributes; they are shared by instances.  Instance attributes
can be set in a method with "self.name = value".  Both class and
instance attributes are accessible through the notation “"self.name"”,
and an instance attribute hides a class attribute with the same name
when accessed in this way.  Class attributes can be used as defaults
for instance attributes, but using mutable values there can lead to
unexpected results.  Descriptors can be used to create instance
variables with different implementation details.

See also: **PEP 3115** - Metaclasses in Python 3 **PEP 3129** -
  Class Decorators

Related help topics: CLASSES, SPECIALMETHODS

No Python documentation found for 'Class definitions'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> No Python documentation found for '*****************'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 
You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> os.listdir()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    os.listdir()
NameError: name 'os' is not defined
>>> listdir()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    listdir()
NameError: name 'listdir' is not defined
>>> import os
>>> os.listdir()
['work.py', 'server.py', 'fibo.py', 'add.py', 'username.py', 'rishabh.py']
>>> fibo.py
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    fibo.py
NameError: name 'fibo' is not defined
>>> insert fibo.py
SyntaxError: invalid syntax
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    shutil.copyfile('data.db', 'archive.db')
  File "/usr/lib/python3.6/shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'data.db'
>>> import sqlite3
>>> conn = sqlite3.connect('example.db')
>>> c = conn.cursor()
>>> c.execute('''CRTEATE TABLE T SHIRTS
                       (colot text,size text,price real)''')
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    (colot text,size text,price real)''')
sqlite3.OperationalError: near "CRTEATE": syntax error
>>> c.execute('''CREATE TABLE T SHIRTS
                       (colot text,size text,price real)''')
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    (colot text,size text,price real)''')
sqlite3.OperationalError: near "SHIRTS": syntax error
>>> c.execute('''CREATE TABLE SHIRTS
                       (colot text,size text,price real)''')
<sqlite3.Cursor object at 0x7f2258300960>
>>> c.execute("INSERT INTO shirts VALUES ('blue','L','1200')")
<sqlite3.Cursor object at 0x7f2258300960>
>>> c.execute("INSERT INTO shirts VALUES ('green','L','1200')")
<sqlite3.Cursor object at 0x7f2258300960>
>>> conn.comit
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    conn.comit
AttributeError: 'sqlite3.Connection' object has no attribute 'comit'
>>> conn.commit
<built-in method commit of sqlite3.Connection object at 0x7f225841f030>
>>> print(c.fetchone())
None
>>> print(c.execute)
<built-in method execute of sqlite3.Cursor object at 0x7f2258300960>
>>> for row in c.execute('SELECT * FROM shirts ORDER BY color'):
        print(row)

        
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for row in c.execute('SELECT * FROM shirts ORDER BY color'):
sqlite3.OperationalError: no such column: color
>>> for row in c.execute('SELECT * FROM shirts ORDER BY colort'):
        print(row)

        
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    for row in c.execute('SELECT * FROM shirts ORDER BY colort'):
sqlite3.OperationalError: no such column: colort
>>> for row in c.execute('SELECT * FROM shirts ORDER BY colot'):
        print(row)

        
('blue', 'L', 1200.0)
('green', 'L', 1200.0)
>>> for row in c.execute('SELECT * FROM shirts ORDER BY size'):
        print(row)

        
('blue', 'L', 1200.0)
('green', 'L', 1200.0)
>>> c.execute("INSERT INTO shirts VALUES ('yellow','m','1200')")
<sqlite3.Cursor object at 0x7f2258300960>
>>> for row in c.execute('SELECT * FROM shirts ORDER BY size'):
        print(row)

        
('blue', 'L', 1200.0)
('green', 'L', 1200.0)
('yellow', 'm', 1200.0)
>>> c.execute("INSERT INTO shirts VALUES ('yellow','m','120')")
<sqlite3.Cursor object at 0x7f2258300960>
>>> 
>>> for row in c.execute('SELECT * FROM shirts ORDER BY size'):
        print(row)

        
('blue', 'L', 1200.0)
('green', 'L', 1200.0)
('yellow', 'm', 1200.0)
('yellow', 'm', 120.0)
>>> for row in c.execute('SELECT * FROM shirts ORDER BY size'):
        print(row)for row in c.execute('SELECT * FROM shirts ORDER BY size'):
                print(row)
                
SyntaxError: invalid syntax
>>> for row in c.execute('SELECT * FROM shirts ORDER BY price'):
        print(row)

        
('yellow', 'm', 120.0)
('blue', 'L', 1200.0)
('green', 'L', 1200.0)
('yellow', 'm', 1200.0)
>>> c.execute("INSERT INTO shirts VALUES ('yellow','A','1200')")
<sqlite3.Cursor object at 0x7f2258300960>
>>> for row in c.execute('SELECT * FROM shirts ORDER BY size'):
        print(row)

        
('yellow', 'A', 1200.0)
('blue', 'L', 1200.0)
('green', 'L', 1200.0)
('yellow', 'm', 1200.0)
('yellow', 'm', 120.0)
>>> 
