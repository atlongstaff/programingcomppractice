data11 = open("DATA11.txt","r") 
Totallist = data11.read()
Totallist = Totallist.split("\n")
while len(Totallist) != 0:
	TandN = Totallist[0]
	TandN = TandN.split(" ")
	T = int(TandN[0])
	N = int(TandN[1])
	boxage = 0
	newboxadded = False
	Totallist.pop(0)
	iteration=0
	while boxage > 0 or iteration < T or newboxadded == False:
		if iteration <= T:
			if Totallist[iteration] == "B":
				boxage += T
				newboxadded = True
		if newboxadded == True:
			boxage -=1	
		iteration +=1	
	print(max(0,iteration - N))
	for x in range(N):
	    Totallist.pop(0)