class SmartPlug:

    def __init__(self, consumptionRate):
        self.consumptionRate = consumptionRate
        self.switchedOn = False

    def toggleSwitch(self):
        if self.switchedOn == False:
            self.switchedOn = True
            return self.switchedOn
        elif self.switchedOn == True:
            self.switchedOn = False
            return self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self, newRate):
        if newRate >= 0 and newRate <= 150:
            self.consumptionRate = newRate
            return self.consumptionRate
        else:
            print(f"Invalid input.")

    def __str__(self):
        output = f"Current state of the swtich is: {self.switchedOn}"
        output += f"\nCurrent consumption rate is: {self.consumptionRate}"
        return output


def testSmartPlug():
    myplug = SmartPlug(45)

    myplug.toggleSwitch()
    print(myplug.getSwitchedOn())

    print(myplug.getConsumptionRate())
    myplug.setConsumptionRate(100)
    print(myplug.getConsumptionRate())

    print(myplug)

#testSmartPlug()

class SmartDoor:

    def __init__(self):
        self.switchedOn = False
        self.locked = True

    def toggleSwitch(self):
        if self.switchedOn == False:
            self.switchedOn = True
            return self.switchedOn
        elif self.switchedOn == True:
            self.switchedOn = False
            return self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getOption(self):
        return self.locked

    def setOption(self, newOption):
        if newOption == True or newOption == False:
            self.locked = newOption
            return self.locked
        else:
            print(f"Invalid input.")
        
    def __str__(self):
        output = f"Door powered state is currently: {self.getSwitchedOn()}"
        output += f"\nDoor locked state is currently: {self.getOption()}"
        return output
        
def testDevice():
    mySmartDoor = SmartDoor()
    mySmartDoor.toggleSwitch()
    print(mySmartDoor.getSwitchedOn())

    mySmartDoor.setOption(False)
    print(mySmartDoor.getOption())

    print(mySmartDoor)

#testDevice()


class SmartHome:

    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDevicesAt(self, index):
        return self.devices[index]

    def addDevice(self, newDevice):
        self.devices.append(newDevice)

    def removeDevice(self, device):
        self.devices.remove(device)

    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()
        return self.devices[index]

    def turnOnAll(self):
        for switchOn in range(len(self.devices)):
            if not self.devices[switchOn].getSwitchedOn():
                self.devices[switchOn].toggleSwitch()
        return self.devices

    def turnOffAll(self):
        for switchOff in range(len(self.devices)):
            if self.devices[switchOff].getSwitchedOn():
                self.devices[switchOff].toggleSwitch()
        return self.devices

    def __str__(self):
        outputList = []
        count = 0
        
        for deviceList in range(len(self.devices)):
            if count == 0:
                output = f"Device {deviceList+1}:"
                count += 1
            else:
                output = f"\nDevice {deviceList+1}:"
            output += f"\nCurrent status: {self.devices[deviceList].getSwitchedOn()}"
            try:
                output += f"\nCurrent consumption rate: {self.devices[deviceList].getConsumptionRate()}"
            except AttributeError:
                output += f"\nCurrent Locked state: {self.devices[deviceList].getOption()}"
            outputList.append(output)

        return "\n".join(outputList)
            

def testSmartHome():
    mySmartHome = SmartHome()
    SmartPlug1 = SmartPlug(45)
    SmartPlug2 = SmartPlug(45)
    myDoor = SmartDoor()

    SmartPlug1.toggleSwitch()
    SmartPlug1.setConsumptionRate(150)
    SmartPlug2.setConsumptionRate(25)
    myDoor.setOption(True)

    mySmartHome.addDevice(SmartPlug1)
    mySmartHome.addDevice(SmartPlug2)
    mySmartHome.addDevice(myDoor)

    mySmartHome.toggleSwitch(1)

    print(mySmartHome)

    mySmartHome.turnOnAll()

    print(mySmartHome)

    mySmartHome.removeDevice(SmartPlug1)

    print(mySmartHome)
    
                    
#testSmartHome()



















    
    
