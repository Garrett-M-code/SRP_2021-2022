# Garrett Moore Jun 19 6:12 PM

class AssignmentVal():
    """This deals with the population"""

    def __init__(self, population, populationNumber, infected,
        infectedNum, vaccinated, vaccinatedNum, dead, dead_list):
        print("The simulation is now running.")
        self.population = population
        self.populationNumber = populationNumber
        self.infected = infected
        self.infectedNum = infectedNum
        self.vaccinated = vaccinated
        self.vaccinatedNum = vaccinatedNum
        self.deadNum = dead
        self.dead_list = dead_list

    def infectionAssignment(self):
        """Deals with the moving of infection and dead"""
        person = 0
        person_1 = 0

        for people in self.population:
            if people[3] == "Sick":
                if people[1] <= 0:
                    people[3] = "Healthy"
                    #poped = self.infected.pop(person_1)
                    self.infectedNum -= 1

                elif people[1] == 14:
                    self.infected.append(people)
                    self.infectedNum += 1

            elif people[3] == "Healthy":
                pass

            person += 1

        for people in self.population:
            if people[4] == "Dead":
                poped = self.population.pop(person_1)
                self.deadNum += 1
                self.populationNumber -= 1
                self.infectedNum -= 1

            elif people[4] == "Alive":
                pass

            person_1 += 1

        for dead_peeps in self.dead_list:
            number = dead_peeps[0]
            ex_dead = 0
            for people in self.infected:
                if people[0] == number:
                    poped = self.infected.pop(ex_dead)

                else:
                    pass
                ex_dead += 1

        return self.population, self.infected, self.infectedNum, self.populationNumber, self.deadNum, self.dead_list

    def initial_Infection(self):
        initial_infected_num = self.infectedNum
        for people in self.population:
            if initial_infected_num > 0.0:
                people[3] = "Sick"
                people[1] = 14

            else:
                people[3] = "Healthy"

            initial_infected_num -= 1

        return self.population

class PopulationCreate(AssignmentVal):
    """This creates the population data in a dictionary."""

    def __init__(self, population, populationNumber, infected,
        infectedNum, vaccinated, vaccinatedNum, dead, dead_list):
        super().__init__(population, populationNumber, infected,
            infectedNum,  vaccinated, vaccinatedNum, dead, dead_list)
        print("Creating the population.")

    def populate(self):
        self.population = []
        person = -1
        length = len(self.population)

        while person < self.populationNumber - 1:
            person = person + 1
            self.population.append([person, 0, "Not vaccinated",
                "Healthy", "Alive", 0.0])
                # The first 0 is the infection cooldown, the second 0 is the
                # death rate.

        return self.population
