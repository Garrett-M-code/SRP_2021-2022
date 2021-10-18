#This file deals with the rates of the program
import random
import populationfunctions

class Rates:
    """Generates and deals with most rates"""
    def __init__(self, population, populationNumber, infected,
        infectedNum, vaccinated, vaccinatedNum, deathRate, vaccineEffectiveness,
        infectionRate):
        """The inizilation of the rates class"""
        self.population = population
        self.populationNumber = populationNumber
        self.infected = infected
        self.infectedNum = infectedNum
        self.vaccinated = vaccinated
        self.vaccinatedNum = vaccinatedNum
        self.death_rate = deathRate
        self.effect = vaccineEffectiveness
        self.infect_rate = infectionRate

    def deathRateGenerator(self):
        self.effect = 100.0 - self.effect
        self.effect = float(self.effect)
        self.effect = self.effect * 0.01

        for people in self.population:
            if people[2] == "Vaccinated":
                temp_rate = self.death_rate * self.effect
                people[5] = temp_rate
            elif people[2] == "Not vaccinated":
                people[5] = self.death_rate


        return self.population

    def deathChoice(self):
        for people in self.population:
            if people[3] == "Sick":
                choice = random.uniform(0.0, 100.0)

                if choice > people[5]:
                    people[4] = "Alive"

                elif choice <= people[5]:
                    people[4] = "Dead"

            else:
                pass

        return self.population

    def infectionRateWorker(self):
        for people in self.population:
            if people[3] == "Sick":
                pass

            elif people[3] == "Healthy":
                rando = random.uniform(0.0, 100.0)
                if rando <= self.infect_rate:
                    people[3] = "Sick"
                    people[1] = 14

                else:
                    pass

        return self.population
