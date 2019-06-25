x=0
y=0
z=0
e=0
def  getcs():
	print("servname")
	x=input()
	print("dbname")
	y=input()
	print("username")
	z=input()
	print("password")
	e=input()
	globals()['x'] = x
	globals()['y'] = y
	globals()['z'] = z
	globals()['e'] = e
	return "servname=%s;dbname=%s;username=%s;password=%s"%(x,y,z,e)
q=getcs()
print(q)



def cstolot():
	return "[('server','%s'),('dbname','%s'),('username','%s'),('pwd','%s')]"%(x,y,z,e)



print(cstolot())
	
