import json
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
f=open ("test.json","w" )
data=json.dump(data,f)

f=open ("test.json","r" )
data=json.load(f)
print(data,type(data))