class Car:
    engineType = "strongest Engine"
    numberOfTyers = 4
    numberOfWindow = 6
    isFridgeAValble = True


    def getNumberOfWindows(self):
        return self.numberOfWindow

    def getNumberOfTyres(self):
        return self.numberOfTyers

car1 = Car()
print(car1.getNumberOfWindows())
print(car1.getNumberOfTyres())








