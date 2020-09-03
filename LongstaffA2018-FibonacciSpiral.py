data11 = open("DATA11.txt","r") 
Totallist = data11.read()
Totallist = Totallist.split("\n")


XandY = Totallist[0]
XandY = XandY.split(" ")
X = int(XandY[0])
Y = int(XandY[1])

Fibsequence = []
char1 = 1
char2 = 1
Fibsequence.append(char1)
Fibsequence.append(char2)

for i in range(100):
	char1 += char2
	char2 += char1
	Fibsequence.append(char1)
	Fibsequence.append(char2)
print(Fibsequence)

