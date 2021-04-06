from sys import argv


#testrun
print("Hello World!")
print("Hello Again")


#set the values of the cards
i = 0;
#2=2, 3=3.... J/A/K/Q = 10

#put the beneath into a loop?
count = 0
currentCard = 0
val = 0

while i < 10:
	i+= 1
	print("Round", i)
	
	#input card prompt = 
	currentCard = input("What's your card?")
	val = currentCard
	if val == "A" or "K" or "Q" or "J":
		val = 10
		
	
	
	if val > 8:
		count = count - 1
		
	if val < 7:
		count = count +1
	
	
	
	
	print ("You got a", currentCard)
	print ("the count is now", count)
 
	if count == 0:
		print ("count is zero")
  
	if count >= 5:
		print ("increase your bet size")
		break;
  
	if count <= -5:
		print ("maybe find another table")
		break;
  
	
  

