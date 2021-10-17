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

death_rate = int(input("What is the death rate?\n\t"))
# The death rate

vaccinatedNum = 0
#The amount of people vaccininated.

day = 0
#This prints the days summary.

keepOn = ""

##########
## Rates ##
##########

vaccinatedRate = input("What percent is vaccinated?\n\t")
vaccinatedRate = float(vaccinatedRate)
vaccinatedRate = vaccinatedRate * 0.01
#This will be a percentage

vaccinated = []

vaccineEffectiveness = input("How effective is this vaccine against death?\n\t")
vaccineEffectiveness = int(vaccineEffectiveness)
vaccineEffectiveness = vaccineEffectiveness * 0.01
#This will be a percentage

infectionRate = input("What is the infection rate?\n\t")
infectionRate = int(infectionRate)
#This will be a percentage

#########
## Main ##
#########

creator = populationfunctions.PopulationCreate(population, popNum, infected,
    infectedNum, vaccinated, vaccinatedRate, amountDead)

population = creator.populate()
#print(f"Population: {population}")

contagion = populationfunctions.AssignmentVal(population, popNum, infected,
    infectedNum, vaccinated, vaccinatedRate, amountDead)

vaccine_runner = vaccine.VaccineInfo(popNum, vaccinatedNum, vaccinatedRate,
    population)

rate_manager = rate.Rates(population, popNum, infected,
    infectedNum, vaccinated, vaccinatedNum, death_rate, vaccineEffectiveness,
    infectionRate)

data_manager = dataWrite.FileManager(vaccinatedNum, popNum, infectedNum)
data_manager.createFile()

death_rate_return = rate_manager.deathRateGenerator()
population = death_rate_return

vax_return = vaccine_runner.vaccine()
population = vax_return

pop_return = contagion.initial_Infection()
population = pop_return

while True:
    day += 1
    print(f"\nDay {day}:")

    print(f"Current population:\n\t{popNum}")
    print(f"Total Amount Dead:\n\t{amountDead}")
    print(f"Currently Infected:\n\t{infectedNum}")
    print(f"Today's Newly infected:\n\t{newInfected}")

    data_manager.dailyUpdate(popNum, infectedNum, amountDead,
        newInfected, day)

    for people in population:
        people[1] -= 1

    infect_assign = rate_manager.infectionRateWorker()
    population = infect_assign

    infection_return = contagion.infectionAssignment()
    population = infection_return[0]
    infected = infection_return[1]
    infectedNum = infection_return[2]
    popNum = infection_return[3]
    amountDead = infection_return[4]

    choice_return = rate_manager.deathChoice()
    population = choice_return

    newInfected = 0

    keepOn = input("Continue? (Y/n) ")
    keepOn = keepOn.title()

    if keepOn == "N":
        break

    elif keepOn == "Y":
        continue

    else:
        print("\n\t\tNot a valid option, continuing to the next day.")
