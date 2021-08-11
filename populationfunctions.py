# Garrett Moore Jun 19 6:12 PM

class AssignmentVal():
    """This deals with the population"""

    def __init__(self, population, populationNumber, infected,
        infectedNum, vaccinated, vaccinatedNum):
        print("The simulation is now running.")
        self.population = population
        self.populationNumber = populationNumber
        self.infected = infected
        self.infectedNum = infectedNum
        self.vaccinated = vaccinated
        self.vaccinatedNum = vaccinatedNum

    def sickPeople(self):
        """Deals with getting people sick"""
        # TODO: Get people sick
        pass

    def popEffect(self):
        for people in self.population:
            if people[4] == "Dead":
                print(f"Person #{people[0]} is dead!")
                popped = self.population.pop(people)
                self.infected.append(people)
                self.infectedNum += 1
                self.populationNumber -= 1

            elif people[4] == "Alive":
                print(f"Person #{people[0]} is alive.")

            return self.population
                # TODO: Finish this dead/alive system

class PopulationCreate(AssignmentVal):
    """This creates the population data in a dictionary."""

    def __init__(self, population, populationNumber, infected,
        infectedNum, vaccinated, vaccinatedNum):
        super().__init__(population, populationNumber, infected,
            infectedNum,  vaccinated, vaccinatedNum)
        print("Creating the population.")

    def populate(self):
        self.population = []
        person = -1
        length = len(self.population)

        while person < self.populationNumber - 1:
            person = person + 1
            self.population.append([person, 0, "Not vaccinated",
                "Healthy", "Alive", 0])
                # The first 0 is the infection cooldown, the second 0 is the
                # death rate.

        return self.population
