import math


data11 = open("DATA11.txt","r") 
Totallist = data11.read()

Totallist = Totallist.split("\n")

TandN = Totallist[0]

TandN = TandN.split(" ")
T = TandN[0]
N = TandN[1]
boxage = 0

newboxadded = False
Totallist.pop(0)
i=0


while boxage > 0 or newboxadded == False:
	try:
		if Totallist[i] == "B" and i <= int(N):
			boxage += int(T)
			newboxadded = True
		elif newboxadded == True:
			boxage -=1	
	except:
		print("test")
		exit()
	print(boxage)
	i +=1


print( i - int(N))



