#This file deals with all information dealing with the vaccine.

import random

class VaccineInfo:
    """Everything dealing with the vaccine"""
    def __init__(self, populationNumber, vaccinatedNum, vaccinatedRate,
        population):
        """The inizilation of the vaccine class"""
        self.populationNumber = populationNumber
        self.vaccinatedNum = vaccinatedNum
        self.vaccinatedRate = vaccinatedRate
        self.population = population

    def vaccine(self):
        """Deals with assigning the vaccination tag"""
        vaccinatedPercent = self.populationNumber * self.vaccinatedRate
        vaccinatedPercent = int(vaccinatedPercent)
        for people in self.population:
            if people[0] < vaccinatedPercent + 1:
                people[2] = "Vaccinated"

            else:
                pass
            print(people)
        return self.population
        # NOTE: make sure to add something to return.
