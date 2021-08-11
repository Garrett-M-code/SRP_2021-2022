class FileManager:
    """Deals with managing files"""
    def __init__(self, vaccinatedNum, populationNumber,
        infectedNum):
        """The inizilation for the FileManager class."""
        filename = input("Whats is your filename?\n\t")
        filename = 'Data/'+ filename + '.txt'

        self.vaccinatedNum = vaccinatedNum
        self.populationNumber = populationNumber
        self.infectedNum = infectedNum
        self.filename = filename

    def createFile(self):
        """Deals with creating files at the begginging of operation"""
        with open(self.filename, 'w') as file_content:
            file_content.write("VIRUS SIMULATION DATA:\n")
            file_content.write(f"Population: {self.populationNumber}\n")
            file_content.write(f"Vaccinated: {self.vaccinatedNum}\n")
            file_content.write(f"Infected: {self.infectedNum}\n\n")

    def dailyUpdate(self, populationNumber, infectedNum, amountDead,
        newInfected, day):
        """Updates to daily numbers to a seperate document"""
        with open(self.filename, 'a') as file_content:
            file_content.write(f"Day: {day}")
            file_content.write(f"\n\tCurrent population:\n\t\t{populationNumber}\n")
            file_content.write(f"\n\tTotal Amount Dead:\n\t\t{amountDead}\n")
            file_content.write(f"\n\tCurrently Infected:\n\t\t{infectedNum}\n")
            file_content.write(f"\n\tToday's Newly infected:\n\t\t{newInfected}\n")
