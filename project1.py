#Nicholas Lam


#This is a program using statistics based on Average (Silver tier) and Professional League of Legends players to determine whether teams on either blue side or red side have the advantage. These statistics are found on leagueofgraphs.com as well as as gol.gg


#Hypothesis: In League of Legends, based on the layout of Summoners Rift (the map), players believe that teams, who by random chance, happen to end up starting the match on the blue side (bottom side) have the advantage over the other team, who starts on red side (top side).


#Declaring and Initializing dictionary for data of the Average Player on Red/Blue Side
	
	#Only the Win Rates are based off of percentages
	
	#The data had to be slightly scewed as a result of not being able to index floating point numbers in lists. 


avgPlayerBlueSide = {"Win Rate":51,						#originally 50.8
					 "Dragons Killed":1,    			#originally 1.96
					 "Rift Heralds Killed":1, 			#originally 0.75
					 "Barons Killed":0}					#originally 0.42
 

avgPlayerRedSide = {"Win Rate":49,						#originally 49.2
					"Dragons Killed":2,					#originally 1.98
					"Rift Heralds Killed":0,			#originally 0.69
					"Barons Killed":1 }					#originally 0.46



#Declaring and Initializing dictionary for data of Professional Players from the Summer 2020 tournament on Red/Blue Side.
	#These are all done as percentages


proPlayerBlueSide = {"Win Rate":54,						#originally 53.8
					 "First Dragon Killed":43, 			#originally 42.9
					 "First Rift Herald Killed":62, 	#originally 61.5
					 "First Baron Killed":57 }			#originally 56.8

proPlayerRedSide = {"Win Rate":46,						#originally 46.2
				 	"First Dragon Killed":57, 			#originally 57.1
				 	"First Rift Herald Killed":39, 		#originally 38.5
				 	"First Baron Killed":43 }			#originally 43.2




#Comparing Average Player stats on both sides, to see which side has the advantage


avgBlueCount = 0 #New variable to count the amount of times blue side has the advantage for average players
avgRedCount = 0 #New variable to count the amount of times red side has the advantage for average players 

b = list(avgPlayerBlueSide.values())  #Transferring the dictionary values into a list
r = list(avgPlayerRedSide.values())


for i in range(len(b)):
	if b[i] > r[i]:
		avgBlueCount = avgBlueCount + 1

print ("For the average player, blue side stats show that there are " + str(avgBlueCount) + " more advantages over red side")

for i in range(len(r)):
	if r[i] > b[i]:
		avgRedCount = avgRedCount + 1


print("For the average player, red side stats show that there are " + str(avgRedCount) + " more advantages over blue side")
print (" ")
print (" ")





#Comparing Professional Player stats on both sides to see which side has the advantage


proBlueCount = 0  #New variable to count the amount of times blue side has the advantage for professional players
proRedCount = 0   #New variable to count the amount of time red side has the advantage for professional players

bs = list(proPlayerBlueSide.values())
rs = list(proPlayerRedSide.values())

for i in range(len(bs)):
	if bs[i] > rs[i]:
		proBlueCount = proBlueCount + 1

print("For a professional player, blue side stats show that there are " + str(proBlueCount) + " more advantages over red side")


for i in range(len(rs)):
	if rs[i] > bs[i]:
		proRedCount = proRedCount + 1

print("For a professional player, red side stats show that there are " + str(proRedCount) + " more advantages over blue side")
print(" ")
print(" ")


#Now we add up the total results of red and blue side advantages using both average and professional players 

totalBlue = avgBlueCount + proBlueCount

totalRed = avgRedCount + proRedCount


print ("The total advantages that blue side has are " + str(totalBlue) + " total advantages.")
print ("The total advantages that red side has are " + str(totalRed) + " total advantages.")
print(" ")



#Stating the results of the testing

print("Based on the results that were yielded, the statistics prove that in League of Legends, starting on blue side does result in having a slight advantage over red side.")