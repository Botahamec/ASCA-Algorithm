import sys
import math

#asks for voters per region
nevotes = int(input("How many registered voters are in the Northeast?"))
sevotes = int(input("How many registered voters are in the Southeast?"))
mwvotes = int(input("How many registered voters are in the Midwest?"))
swvotes = int(input("How many registered voters in the Southwest?"))
westvotes = int(input("How many registered voters are in the West?"))
osvotes = int(input("How many registered voters are Overseas?"))
voters = nevotes + sevotes + mwvotes + swvotes + westvotes + osvotes #total voters

#calculates the highest number of voters for a region
highvotes = nevotes #i assume automatically the northeast will, to save time
if (highvotes < osvotes) : highvotes = osvotes
if (highvotes < mwvotes) : highvotes = mwvotes
if (highvotes < sevotes) : highvotes = sevotes
if (highvotes < westvotes) : highvotes = westvotes
if (highvotes < swvotes) : highvotes = swvotes

delta = 1 / highvotes
total = voters / 2 #times the loop will run, impossible to have less than one seat
total += 1 #number of times the loop will run + 1
invalid = [1] #one will not be used as a seat to voter ratio

while (True):
	
	#pre-defines number of seats, in case no intervals work
	neseats = 1.0
	seseats = 1.0
	mwseats = 1.0
	swseats = 1.0
	westseats = 1.0
	osseats = 1.0

	lowerror = 0 #calculates which ratio works best, set to 0
	interval = 1 #i don't like for loops
	
	#starting the algorithm
	while (interval < total) :

		valid = True

		netest = nevotes / interval
		setest = sevotes / interval
		mwtest = mwvotes / interval
		westtest = westvotes / interval
		ostest = osvotes / interval

		netest = round(int(netest))
		setest = round(int(setest))
		mwtest = round(int(mwtest))
		swtest = round(int(swtest))
		westtest = round(int(westtest))
		ostest = round(int(ostest))

		if (ostest == 0) : valid = False
		if (westtest == 0) : valid = False
		if (swtest == 0) : valid = False
		if (mwtest == 0) : valid = False
		if (setest == 0) : valid = False
		if (netest == 0) : valid = False

		if 
		
		if (valid):
			
			#calculates the error for each interval
			neerr = abs(.5 - (nevotes % interval / interval))
			seerr = abs(.5 - (sevotes % interval / interval))
			mwerr = abs(.5 - (mwvotes % interval / interval))
			swerr = abs(.5 - (swvotes % interval / interval))
			westerr = abs(.5 - (westvotes % interval / interval))
			oserr = abs(.5 - (osvotes % interval / interval))
			err = neerr + seerr + mwerr + swerr + westerr + oserr
			
			#if error is low, then the number of seats per region is recorded
			if (err >= lowerror) :
				lowerror = err #sets the lowest error
				ratio = interval #records the seat to voter ratio
				neseats = netest
				seseats = setest
				mwseats = mwtest
				swseats = swtest
				westseats = westtest
				osseats = ostest
		
		interval += delta #increases the interval and starts the loop again

	#prints the number of seats required
	print("_____________________________________________________________")
	print ("Northeast: " + strneseats))
	print ("Southeast: " + strseseats))
	print ("Midwest:   " + strmwseats))
	print ("Southwest: " + strswseats))
	print ("West:      " + strwestseats))
	print ("Overseas:  " + strosseats))

	print ("") #enters a blank line
	print ("Seat Ratio: 1 Representative per " + str(ratio) + " Voters")
	print ("Accuracy: " + str(lowerror * (100/3)) + "%")

	#asks for a different result
	wait = input ("Press enter for a different result")
	invalid.append (ratio)
