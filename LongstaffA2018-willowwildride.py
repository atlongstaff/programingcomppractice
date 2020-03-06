data11 = open("DATA11.txt","r") 
Totallist = data11.read()
Totallist = Totallist.split("\n")
TandN = Totallist[0]
TandN = TandN.split(" ")
T = int(TandN[0])
N = int(TandN[1])
boxage = 0
newboxadded = False
Totallist.pop(0)
i=0
while boxage > 0 or i < T or newboxadded == False:
	if i <= T:
		if Totallist[i] == "B":
			boxage += T
			newboxadded = True
	if newboxadded == True:
		boxage -=1	
	i +=1	

print(max(0,i - N))