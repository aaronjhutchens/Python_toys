class staticPatient:
    'creates patient with various vitals that are set upon instantiation.  Use dynamicPatient or randomPatient for respective functionality'

    #vitals = [ '
    
    def __init__(self, name, age, bodyTemp, pulseRate, respiratoryRate, diastolic, systolic):
        # Instantiates object with set values
        self.name = name
        self.age = int(age)
        self.bodyTemp = float(bodyTemp)
        self.pulseRate = int(pulseRate)
        self.respiratoryRate = int(respiratoryRate)
        self.diastolic = int(diastolic)
        self.systolic = int(systolic)
        print(inspect.getmembers(self))
    
    def getName(self, label):
        if label:
            print("Name: ", self.name)
        else:
            print(self.name)
            
    def setName(self, newName):
        self.name = newName

    def getAge(self, label):
        if label:
            print("Age: ", self.age)
        else:
            print(self.age)

    def setAge(self, newAge):
        self.age = int(newAge)

    def getBodytemp(self, label):
        if label:
            print("Body temperature: ", self.bodyTemp)
        else:
            print(self.bodyTemp)

    def setBodytemp(self, newTemp):
        self.bodyTemp = float(newTemp)

    def getPulserate(self, label):
        if label:
            print("Pulse rate: ", self.pulseRate)
        else:
            print(self.pulseRate)

    def setPulserate(self, newPulse):
        self.pulseRate = int(newPulse)

    def getRespiratoryrate(self, label):
        if label:
            print("Respiratory rate (breaths per minute): ", self.respiratoryRate)
        else:
            print(self.respiratoryRate)

    def setRespiratoryrate(self, newRate):
        self.respiratoryRate = int(newRate)

    def getSystolic(self, label):
        if label:
            print("Systolic BP: ", self.systolic)
        else:
            print(self.systolic)

    def setSystolic(self, newSystolic):
        self.systolic = int(newSystolic)

    def getDiastolic(self, label):
        if label:
            print("Diastolic BP: ", self.diastolic)
        else:
            print(self.diastolic)

    def setDiastolic(self, newDiastolic):
        self.diastolic = int(newDiastolic)

    def printVitals(self):
        self.getName(1)
        self.getAge(1)
        self.getBodytemp(1)
        self.getPulserate(1)
        self.getRespiratoryrate(1)
        self.getDiastolic(1)
        self.getSystolic(1)
