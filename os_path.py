import os

var1 = os.path.abspath(__file__)
var2 = os.path.dirname(var1)
var3 = os.path.join(var2, 'db_connect.py')
print(var1)
print(var2)
print(var3)
