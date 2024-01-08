#Simple bubble sort that gets user input of integers then sorts the list in ascending order
#create the list, the continue bool and the temp used for the swap
numlist = []
cont = False
temp = 0

#loops asking for input until user inputs whitespace
while cont == False:
	num = input("Enter a whole number or just press enter to continue: ")
	if num == "": #breaks loop when user inputs whitespace
		cont = True
	else:
		try: #error checking, ensures that user enters a whole number
			int(num)
		except:
			print("Please enter a whole number.")
			continue
		numlist.append(int(num)) #assuming no error, adds num to list as an int

#actual bubble sort algorithm

#loops through the entire array
for i in range(len(numlist)-1, 0, -1):
	#swaps elements from the current index if the number is bigger than the next index
	for n in range(i):
		if numlist[n] > numlist[n + 1]:
				#stores index in a temporary variable, then swaps the value if index i with index i + 1 but only if the former is a larger number
				temp = numlist[n]
				numlist[n] = numlist[n + 1]
				numlist[n + 1] = temp
				
print("The sorted list is:", numlist)
