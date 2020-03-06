data11 = open("DATA11.txt","r") 
Totallist = data11.read()
Totallist = Totallist.split("\n")

while len(Totallist) != 0:
	SplitList = []
	minlist = []
	minlistholdinglist = []
	FinalSplitList = []
	N = int(Totallist[0])

	Totallist.pop(0)
#creates two splitlists one for first parse one for second

	for i in Totallist: 
		if Totallist.index(i) < N:
			SplitList.append(i.split(" "))
			FinalSplitList.append(i.split(" "))


#checks to find the minimum in the entier document
	for l in SplitList:
		l.pop(0)
		l.pop(1)
		minlist.append(min(l))
		absolutemin = min(minlist)

#creates a list of the lists that hold the minimum
	for m in FinalSplitList:
		if absolutemin == m[0]:#checks to make sure that the first number isnt the minimum
			m.pop(0)
			if absolutemin in m:#if it is the minimum remove and check again
				minlistholdinglist.append(absolutemin)
		elif absolutemin in m:#check if minimum numberis in the list
			minlistholdinglist.append(m[0])
	print(absolutemin , minlistholdinglist)

#removes all parsred lists fom the list
	for it in range(0,N):
		if it < N :
			Totallist.pop(0)
			
