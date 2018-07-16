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

interval = float(input("What's the seat to voter ratio?")) #asks for the ratio

neerr = abs(.5 - (nevotes % interval / interval))
seerr = abs(.5 - (sevotes % interval / interval))
mwerr = abs(.5 - (mwvotes % interval / interval))
swerr = abs(.5 - (swvotes % interval / interval))
westerr = abs(.5 - (westvotes % interval / interval))
oserr = abs(.5 - (osvotes % interval / interval))
err = neerr + seerr + mwerr + swerr + westerr + oserr

print ("Accuracy: " + str(err*100/3) + "%")
wait = input("Press enter to exit")