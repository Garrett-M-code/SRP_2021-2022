# Garrett Moore Jun 19 6:12 PM

import populationfunctions
import dataWrite
import vaccine
import rate

###############
## Variables ##
###############

popNum = input("What is the total population:\n\t")
popNum = int(popNum) + 1
#How many people there are.

population = []
#This will be a dictionary

amountDead = 0
newInfected = 0

infectedNum = input("How many are infected?\n\t")
infectedNum = int(infectedNum)
#This is the starting and currently infected.

infected = []
#This is a list that contains infected people.

vaccinatedNum = 0
#The amount of people vaccininated.

day = 0
#This prints the days summary.

keepOn = ""

##########
## Rates ##
##########

vaccinatedRate = input("What percentage is vaccinated?\n\t")
vaccinatedRate = int(vaccinatedRate)
vaccinatedRate = vaccinatedRate * 0.10
#This will be a percentage

vaccinated = []

vaccineEffectiveness = input("How effective is this vaccine?\n\t")
vaccineEffectiveness = int(vaccineEffectiveness)
vaccineEffectiveness = vaccineEffectiveness * 0.10
#This will be a percentage

infectionRate = input("What is the infection rate?\n\t")
infectionRate = int(infectionRate)
infectionRate = infectionRate * 10
#This will be a percentage

#########
## Main ##
#########

creator = populationfunctions.PopulationCreate(population, popNum, infected,
    infectedNum, vaccinated, vaccinatedRate)

population = creator.populate()
print(f"Population: {population}")

contagion = populationfunctions.AssignmentVal(population, popNum, infected,
    infectedNum, vaccinated, vaccinatedRate)

#contagion.vaccine()
# TODO: Update this to the vaccine functions
contagion.popEffect()

data_manager = dataWrite.FileManager(vaccinatedNum, popNum, infectedNum)
data_manager.createFile()

# TODO: Add other class actions

while True:
    day += 1
    print(f"\nDay {day}:")

    print(f"Current population:\n\t{popNum}")
    print(f"Total Amount Dead:\n\t{amountDead}")
    print(f"Currently Infected:\n\t{infectedNum}")
    print(f"Today's Newly infected:\n\t{newInfected}")

    data_manager.dailyUpdate(popNum, infectedNum, amountDead,
        newInfected, day)

    keepOn = input("Continue? (Y/n) ")
    keepOn = keepOn.title()

    if keepOn == "N":
        break
    elif keepOn == "Y":
        continue
