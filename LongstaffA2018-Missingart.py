data11 = open("DATA11.txt","r") 
Totallist = data11.read()
Totallist = Totallist.split("\n")

while len(Totallist) != 0:
	firstline = Totallist[0]
	#sets the variables 
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
		#checks if youv3e started on the awnsers
		if line == "A" :
			lineindex = Totallist.index(line)
			Totallist.pop(Totallist.index("A"))#removes the line with A
			awnserseries.append(Totallist[lineindex])#adds the next one to the awnserlist becuase its new index has already run
			continue

		#checks if youve finished the first set
		if line == "*" :
			lineindex = Totallist.index(line)
			Totallist.pop(Totallist.index("*"))
			for it in range(0,(N*2)):#delets all previous sets
				if it < N *2 :
					Totallist.pop(0)
			continue
			
		#checks if the line is an awnser
		if Totallist.index(line) > N:
			awnserseries.append(line)
			continue

		#if its not an awnser
		for n in line:
			if int(n) == 0 : #check if 0
				newline += str(Z)

			elif int(n) % 2 == 0: #check if even
				newline += str(int(n) + X)
		
			
			elif int(n) % 2 != 0: #check if odd
				if int(n) - Y >= 0: #check if odd is larger than 0
					newline += str(int(n) - Y)
				
		newseries.append(newline)#adds to the newseries list
		newline = ''


	for i in awnserseries:
		try:
			if i == newseries[newseries.index(i)]: #checks if theres a match
				Match = True
		except:# if therers a failure, add it to the failure list
			failurelist.append(awnserseries.index(i) +1)
			Match = False
	if Match == True: #print the reults
		print("MATCH")
	else:
		print("FAIL", str(failurelist).replace('[','').replace(']',''))



