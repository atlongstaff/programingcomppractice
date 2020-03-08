data11 = open("DATA11.txt","r") 
Totallist = data11.read()
Totallist = Totallist.split("\n")

while len(Totallist) != 0:
	firstline = Totallist[0]
	N = int(firstline.split(" ")[0])
	X = int(firstline.split(" ")[1])
	Y = int(firstline.split(" ")[2])
	Z = int(firstline.split(" ")[3])
	Totallist.pop(0)

	awnserseries = []
	newseries = []
	newline = ''
	failurelist = []
	for line in Totallist:
		if line == "A" :
			lineindex = Totallist.index(line)
			Totallist.pop(Totallist.index("A"))
			awnserseries.append(Totallist[lineindex])
			continue
		if line == "*" :
			lineindex = Totallist.index(line)
			Totallist.pop(Totallist.index("*"))
			for it in range(0,(N*2)):
				if it < N *2 :
					Totallist.pop(0)
			continue
			

		if Totallist.index(line) > N:
			awnserseries.append(line)
			continue

		for n in line:
			if int(n) == 0 :
				newline += str(Z)

			elif int(n) % 2 == 0:
				newline += str(int(n) + X)
		
			
			elif int(n) % 2 != 0:
				if int(n) - Y > 0:
					newline += str(int(n) - Y)
				if int(n) - Y == 0:
					newline += str(int(n) - Y)


		newseries.append(newline)
		newline = ''

	for i in awnserseries:
		try:
			if i == newseries[newseries.index(i)]:
				Match = True
		except:
			failurelist.append(awnserseries.index(i) +1)
			Match = False
	if Match == True:
		print("MATCH")
	else:
		print("FAIL", str(failurelist).replace('[','').replace(']',''))



