thisdict =	{}

keys = ("maquina","nome","valor")


for indce,k in enumerate(keys):
	thisdict[k] = indce * 10
	
print(thisdict)