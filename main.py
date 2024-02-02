import os
clear = lambda: os.system("clear")
list1=[]
list2=[]
list3=[]

while True:
	print("Teach the AI something in the format 'X is a Y'""\n""Ask it to remember what you have taught it in the format 'What is X?'""\n""Recall everything that the AI has learnt by typing 'Memory'""\n""Forget everything by typing 'Clear'")
	userinput=input("\n")
	inputlist=userinput.split()
	if len(inputlist)==4 and inputlist[1].lower()=="is" and (inputlist[2].lower()=="a" or inputlist[2].lower()=="an"):
		clear()
		print("Learning...""\n""\n""---""\n")
		thething=[inputlist[2]+" "+inputlist[3]]
		list1.extend((inputlist[0], thething[0]))
	elif len(inputlist)==3 and inputlist[0].lower()=="what" and inputlist[1].lower()=="is":
		itemlist=inputlist[2]
		item = itemlist[0:len(itemlist)-1]
		if item in list1 and list1.index(item)%2==0:
			clear()
			print(item,"is",list1[list1.index(item)+1],"\n","\n""---""\n")
		else:
			clear()
			print("I have not learnt that yet.""\n""\n""---""\n")
	elif len(inputlist)==1 and inputlist[0].lower()=="memory":
		clear()
		if len(list1)==0:
			print("I have not learnt anything yet.""\n""\n""---""\n")
		else:
			for i in range(0,len(list1)):
				if i%2==0:
					list2.append(list1[i])
				else:
					list3.append(list1[i])
			for i in range(0,len(list2)):
				print(list2[i],"is",list3[i])
			print("\n""---""\n")
	elif len(inputlist)==1 and inputlist[0].lower()=="clear":
		list1=[]
		clear()
	else:
		clear()
		print("Sorry, I do not understand.""\n""\n""---""\n")