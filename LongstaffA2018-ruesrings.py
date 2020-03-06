import numpy

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
		parseinglist = l
		parseinglist.pop(0)
		parseinglist.pop(1)
		minlist.append(min(parseinglist))
		absolutemin = min(minlist)

#creates a list of the lists that hold the minimum
	for m in FinalSplitList:
		if absolutemin in m:
			minlistholdinglist.append(m[0])
	print(absolutemin , minlistholdinglist)

#removes all parsred lists fom the list
	for it in range(0,N):
		if it < N :
			Totallist.pop(0)
			
