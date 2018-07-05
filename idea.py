import sys
import math

#asks for voters per region
nevotes = input ("How many registered voters are in the Northeast?")
sevotes = input ("How many registered voters are in the Southeast?")
mwvotes = input ("How many registered voters are in the Midwest?")
swvotes = input ("How many registered voters in the Southeast?")
westvotes = input ("How many registered voters are in the West?")
osvotes = input ("How many registered voters are Overseas?")
voters = nevotes + sevotes + mwvotes + swvotes + westvotes + osvotes #finds the total number of voters

#calculates the highest number of voters for a region
highvotes = nevotes #i assume automatically the northeast will, to save time
if (highvotes < osvotes) : highvotes = osvotes
if (highvotes < mwvotes) : highvotes = mwvotes
if (highvotes < sevotes) : highvotes = sevotes
if (highvotes < westvotes) : highvotes = westvotes
if (highvotes < swvotes) : highvotes = swvotes

delta = 1 / highvotes
total = voters / 2 #number of times the loop will run, since it shouldn't be possible to have less than one seat
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

	lowerror = 0 #used to calculate which ratio works best, i set it to 6, since it's an impossible error value
	interval = 1 #i'm using this because i don't like for statements, the interval is set to 2 because 1 would be direct democracy
	
	#starting the algorithm
	while (interval < total) :
		
		if (not(interval in invalid)):
			
			#calculates the error for each interval
			neerror = abs(.5 - (nevotes % interval / interval))
			seerror = abs(.5 - (sevotes % interval / interval))
			mwerror = abs(.5 - (mwvotes % interval / interval))
			swerror = abs(.5 - (swvotes % interval / interval))
			westerror = abs(.5 - (swvotes % interval / interval))
			oserror = abs(.5 - (osvotes % interval / interval))
			error = neerror + seerror + mwerror + swerror + westerror + oserror

			#calculates seats per region
			netest = nevotes / interval + 1
			setest = sevotes / interval + 1
			mwtest = mwvotes / interval + 1
			swtest = swvotes / interval + 1
			westtest = westvotes / interval + 1
			ostest = osvotes / interval + 1
			
			#if the error is low, then the number of seats per region is recorded
			if (error >= lowerror) :
				lowerror = error #sets the lowest error
				ratio = interval #records the seat to voter ratio
				neseats = nevotes / interval
				seseats = sevotes / interval
				mwseats = mwvotes / interval
				swseats = swvotes / interval
				westseats = westvotes / interval
				osseats = osvotes / interval
		
		interval += delta #increases the interval number and starts the loop again

	#prints the number of seats required, they will probably need to be rounded
	print("_____________________________________________________________")
	print ("Northeast: " + str(neseats))
	print ("Southeast: " + str(seseats))
	print ("Midwest:   " + str(mwseats))
	print ("Southwest: " + str(swseats))
	print ("West:      " + str(westseats))
	print ("Overseas:  " + str(osseats))

	print ("") #enters a blank line
	print ("Seat Ratio: 1 Representative per " + str(ratio) + " Voters")
	print ("Accuracy: " + str(lowerror * (100/3)) + "%")

	#asks for a different result
	wait = input ("Press enter for a different result")
	invalid.append (ratio)
