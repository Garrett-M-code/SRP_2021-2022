#This file deals with the rates of the program
import random
import populationfunctions

class Rates:
    """Generates and deals with most rates"""
    def __init__(self, population, populationNumber, infected,
        infectedNum, vaccinated, vaccinatedNum, deathRate, vaccineEffectiveness):
        """The inizilation of the rates class"""
        self.population = population
        self.populationNumber = populationNumber
        self.infected = infected
        self.infectedNum = infectedNum
        self.vaccinated = vaccinated
        self.vaccinatedNum = vaccinatedNum
        self.deathrate = deathrate
        self.effect = vaccineEffectiveness
        # TODO: Create the deathRate

    def deathRateGenerator(self):
        for people in self.population:
            if people[2] == "Vaccinated":
                temp_rate = self.deathRate * self.effect
                people[5] = temp_rate
            elif people[2] == "Not vaccinated":
                people[5] = self.deathRate

        return self.population
        # TODO: Create the generator for the death rate.

    def deathChoice(self):
        for people in self.population:
            choice = randint(1, 100)
            life_death = populationfunctions.AssignmentVal(self.population,
                self.populationNumber, self.infected,
                self.infectedNum, self.vaccinated, self.vaccinatedNum)

            if choice > people[5]:
                print("Congrats you survived.")
            elif choice <= people[5]:
                print("You died")

        self.population = life_death.popEffect(self)
        return self.population

    def infectionRateWorker(self):
        """Will Deal with the overall infection rate."""
