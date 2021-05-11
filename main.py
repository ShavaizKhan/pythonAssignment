#-----------------------------------------------------------------------------
# Name: Python Assignment 1 - Alien Hijack 
# Purpose: Program where a kid gets abducted by aliens on his way to school and is forced to answer some questions.
#
# Author:      Shavaiz Khan
# Created:     13-Dec-2020
# Updated:     18-Dec-2020
#-----------------------------------------------------------------------------
# Defining functions to use through out the code


#calculates the volume of objects
def volumeCalc(width, length, height):
  volume = width * height * length

  if width < 0 or length < 0 or height < 0:
    return "Error"
  
  else:
    return volume

#calculates a value being divided by 8
def divEight(number):
  number = number / 8

  if number < 0:
    return "Error"

  else:
    return number


#introduction with information for inputs later on in the code.
print("It's almost the first day of school, and Shavaiz is still asleep. To catch the bus he needs to wake up at 8:30!")
print()

#loop for inputing the correct time, time must match 8:30 to continue out of loop
wakeTime = 0

while wakeTime == 0:
  timeInput = input("Is it time for him to wake up? What time is it? ")  
  if timeInput == "8:30":
    print()
    print ("It's time to get up Shavaiz! Get to the bus stop!")
    wakeTime = wakeTime + 1
  else:
    print ("Hmm that doesn't seem right? Try again.") 

#stating the problem at hand
print()
print("Oh No! There seems to be a problem. Your bus has been hijacked by aliens!")

#giving the motive for the alien asking the following questions
print()
print("The alien has a few questions for you. Pay attention to how he asks you to answer the questions. Beware, these questions are case sensitive!")

#loop for asking hether or not you have a name, you were told you do, so the answer must be yes for you to break out of loop
nameAnswer = 0

while nameAnswer == 0:
  askInput = (input("Do you have a name? (Yes or No)"))
  if askInput == "Yes":
    print("Okay, that checks out.")
    nameAnswer = nameAnswer + 1
  else: 
    print("That answer does not make sense. Please try again.")

#asking for a name just to repeat it back at you
petInput = input("And, what is your pet's name? ")

print("Say hi to " + str(petInput) + " for me!")

#statement from the aliens
print()
print("Anyways, welcome aboard our spacecraft, we would like to ask you some questions to better understand humans on this earth.")

#introducing the continent questions
print()
print("First we would like to know if you know all the continents of this planet.")

#list of continents for you to correctly match, Oceania and Australia are both included as people refer to both of them as one continent
continentList = ['Antarctica', 'Australia', 'Oceania', 'South America', 'North America', 'Africa', 'Asia', 'Europe']

#for loop lists out 7 continents for you to input the name of, have all seven match the list to leave the loop, loop will break if answered incorrectly
for continent in range(1, 8, 1):
  contInput = str(input("What is Continent #" + str(continent)+ "? "))
  if contInput in continentList:
    contMessage = "Yep, that's correct!"
    print(contMessage)
    #remove the continent from the list so that it's wrong if the continent is repeated again
    continentList.remove(contInput)
  elif contInput not in continentList:
    contMessage = "No that is wrong."
    print(contMessage)
    print("You failed this question, on to the next one.")

#introducing volume questions
print()
print("Moving on, we need you to calculate the volume of these objects.")  

#first question asks for you to input the width
print()
print("The first object is 8cm in length, 4cm in height, and 1m in width. To calculate the volume, we need to know the width of this item.")

#must input the correct number of cm in a m 
itemWidth = int(input("How many centimeters are in 1 metre? "))

if itemWidth != 100:
  print("That's incorrect, what a shame.")

else: 
  #calls function so that volume is calculated
  firstVolume = volumeCalc(itemWidth, 8, 4)
  print("So, the first volume is " + str(firstVolume) + "cm cubed. Seems about right.")

#second volume question asks for you to input the height
print()
print("Time for the second question. We need a box, the length should be 400cm, the width should be 300cm, and the length should be around your height. Can you tell me your height in cm?")

#your input height must be within a range of numbers
lengthLoop = 0

while lengthLoop == 0:
  print()
  height = int(input("What is your height(cm)? "))

  if height > 300 or height < 50:
    print("Hmm, I find that hard to believe, you're not an alien too? Are you?")
  else:
    #calls function so that volume is calculated and converted to m
    secondVolume = volumeCalc(300, 400, height)
    secondVolume = secondVolume / 100
    print("Alright the box is going to be " + str(secondVolume) + "m cubed. Should be cozy.")
    lengthLoop = 1

#introducing divide eight questions
print()
print("Time for your last question. We need to know how your measurements would be if you were divided into 8.")

#example of calling function on a already given input
heightDiv = divEight(height)
print()
print("For example, the height of each eighth would be, " + str(heightDiv) + "cm.")

print()
print("Let's get started!")

#your input weight must be within a range of numbers otherwise you need to try again
weightLoop = 0

while weightLoop == 0:
  print()
  weight = int(input("How much do you weigh(kg)? "))

  if weight > 150 or weight < 45:
    print("Hmm, I find that hard to believe, you're not an alien too? Are you?")
  else:
    #calls function to divide weight by 8
    weightDiv = divEight(weight)
    print()
    print("So an eighth of you weighs" + str(weightDiv) + "kg.")
    weightLoop = 1

#closing lines to end off the program
print()
print("Haha, that was fun! Thanks for being apart of our tests. It seems like you're a little late to school. Let's drop you off!")

print()
print("See you soon!")