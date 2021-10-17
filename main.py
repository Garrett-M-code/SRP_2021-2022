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

dead_list = []

death_rate = float(input("What is the death rate?\n\t"))
# The death rate

vaccinatedNum = 0
#The amount of people vaccininated.

day = 0
#This prints the days summary.

correct_daily_infected_num = 0

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
#This will be a percentage

infectionRate = input("What is the infection rate?\n\t")
infectionRate = float(infectionRate)
#This will be a percentage

#########
## Main ##
#########

creator = populationfunctions.PopulationCreate(population, popNum, infected,
    infectedNum, vaccinated, vaccinatedRate, amountDead, dead_list)

population = creator.populate()

contagion = populationfunctions.AssignmentVal(population, popNum, infected,
    infectedNum, vaccinated, vaccinatedRate, amountDead, dead_list)

vaccine_runner = vaccine.VaccineInfo(popNum, vaccinatedNum, vaccinatedRate,
    population)

rate_manager = rate.Rates(population, popNum, infected,
    infectedNum, vaccinated, vaccinatedNum, death_rate, vaccineEffectiveness,
    infectionRate)

data_manager = dataWrite.FileManager(vaccinatedNum, popNum, infectedNum)
data_manager.createFile()

vax_return = vaccine_runner.vaccine()
population = vax_return

death_rate_return = rate_manager.deathRateGenerator()
population = death_rate_return

pop_return = contagion.initial_Infection()
population = pop_return

while True:
    day += 1
    old_infected_num = infectedNum

    print(f"\nDay {day}:")

    print(f"Current population:\n\t{popNum}")
    print(f"Total Amount Dead:\n\t{amountDead}")
    print(f"Currently Infected:\n\t{infectedNum}")
    print(f"Today's Newly infected Compared to Yesterday:\n\t{correct_daily_infected_num}")

    data_manager.dailyUpdate(popNum, infectedNum, amountDead,
        newInfected, day)

    if infectedNum <= 0:
        print("Congrats! The pandemic has ended. There are no more sick people!")
        break

    else:
        pass

    for people in population:
        people[1] -= 1
        #deals with quarinitne

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

    tomarrow_s_infected_num = infectedNum - old_infected_num
    correct_daily_infected_num = abs(int(tomarrow_s_infected_num))

    keepOn = input("Continue? (Y/n) ")
    keepOn = keepOn.title()

    if keepOn == "N":
        break

    elif keepOn == "Y":
        continue

    else:
        print("\n\t\tNot a valid option, continuing to the next day.")
