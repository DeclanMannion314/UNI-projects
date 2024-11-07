from tkinter import *
from backend import SmartHome
from backend import SmartPlug
from backend import SmartDoor

def setUpHome():
    global devices
    myHome = SmartHome()

    devices = []

    while len(devices) != 5:
        try:
            userInput = int(input("Enter 1 for a regular device, Enter 2 for a door."))
            if userInput == 1:
                deviceName = input("Enter your a device.")
                devices.append(deviceName)
                consumptionRate = int(input("Enter the consumption rate."))
                device = SmartPlug(consumptionRate)
                myHome.addDevice(device)
            elif userInput == 2:
                doorName = input("Enter name of door.")
                devices.append(doorName)
                device = SmartDoor()
                myHome.addDevice(device)
            elif userInput != 1 or userInput != 2:
                print("Enter 1 or 2.")
                userInput = 0
        except ValueError:
            print("Enter a valid integer.")
            userInput = 0

    
    return myHome, devices

class SmartHomeSystem:

    def __init__(self, myHome, devices):
        self.myHome = myHome
        self.devices = devices
        self.root = Tk()
        self.root.title("Smart Home GUI")
        self.root.geometry("550x300")
        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(row=0, column=0)
        self.editedDevice = StringVar()
        self.editedConsumptionRate = IntVar()
        self.newDeviceName = StringVar()
        self.newDoorName = StringVar()
        self.newConsumptionRate = IntVar()

    def createWidgets(self):
        self.mainFrame.destroy()
        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(row=0, column=0)
        
        sortedLst = []
        sort = 0
        for sort in range(len(self.devices)):
            tempD = self.myHome.getDevicesAt(sort)
            try:
                insert = f"{self.devices[sort]}: {tempD.getSwitchedOn()}, Consumption: {tempD.getConsumptionRate()}"
            except AttributeError:
                insert = f"{self.devices[sort]}: {tempD.getSwitchedOn()}, Locked state: {tempD.getOption()}"
            sortedLst.append(insert)
            
        output = 0
        for output in range(len(sortedLst)):
            devicelbl = Label(
                self.mainFrame,
                width = 30,
                text = sortedLst[output]
            )
            devicelbl.grid(row=1+output, column=0)

            togglebtn = Button(
                self.mainFrame,
                text = "Toggle",
                command = lambda index=output: self.toggleDevice(index) #colours?
            )
            togglebtn.grid(row=1+output, column=1)

            editbtn = Button(
                self.mainFrame,
                text = "Edit",
                command = lambda index=output: self.editDevice(index)
            )
            editbtn.grid(row=1+output, column=2)

            deletebtn = Button(
                self.mainFrame,
                text = "Delete",
                command = lambda index=output: self.deleteDevice(index)
            )
            deletebtn.grid(row=1+output, column=3)

        turnOnAllbtn = Button(
            self.mainFrame,
            text = "Turn on all",
            command = lambda: self.turnOnAll()
        )
        turnOnAllbtn.grid(row=0, column=0)

        turnOffAllbtn = Button(
            self.mainFrame,
            text = "Turn off all",
            command = lambda: self.turnOffAll()
        )
        turnOffAllbtn.grid(row=0, column=1)

        addbtn = Button(
            self.mainFrame,
            text = "Add",
            command = lambda: self.addDevice()
        )
        addbtn.grid(row=len(sortedLst)+1, column=0)

                        
    def turnOnAll(self):
        self.myHome.turnOnAll()
        self.createWidgets()

    def turnOffAll(self):
        self.myHome.turnOffAll()
        self.createWidgets()

    def toggleDevice(self, index):
        self.myHome.getDevicesAt(index).toggleSwitch()
        self.createWidgets()

    def deleteDevice(self, index):
        tempD = self.myHome.getDevicesAt(index)
        self.myHome.removeDevice(tempD)
        self.devices.pop(index)
        self.createWidgets()

    def addDevice(self):
        newWin2 = Toplevel(self.root)
        newWin2.title("Add device")
        newWin2.geometry("500x150")

        devicechooselabel = Label(
            newWin2,
            text = "Enter Device details"
        )
        devicechooselabel.grid(row=0, column=0)

        doorchooselabel = Label(
            newWin2,
            text = "Enter Door details"
        )
        doorchooselabel.grid(row=0, column=2)

        devicechooselabel = Label(
            newWin2,
            text = "Enter Device name:"
        )
        devicechooselabel.grid(row=1, column=0)

        doorchooselabel = Label(
            newWin2,
            text = "Enter Door name:"
        )
        doorchooselabel.grid(row=1, column=2)

        devicenameentry = Entry(
            newWin2,
            width = 10,
            textvariable = self.newDeviceName
        )
        devicenameentry.grid(row=1, column=1)

        doornameentry = Entry(
            newWin2,
            width = 10,
            textvariable = self.newDoorName
        )
        doornameentry.grid(row=1, column=3)

        consumptionchooselabel = Label(
            newWin2,
            text = "Enter consumption:"
        )
        consumptionchooselabel.grid(row=2, column=0)

        consumptionrateentry = Entry(
            newWin2,
            width = 10,
            textvariable = self.newConsumptionRate
        )
        consumptionrateentry.grid(row=2, column=1)

        choosedevicebutton = Button(
            newWin2,
            text= "Choose Device",
            command = lambda: self.newDeviceFun(self.newDeviceName.get(), self.newConsumptionRate.get())
        )
        choosedevicebutton.grid(row=3, column=1)

        choosedoorbutton = Button(
            newWin2,
            text= "Choose Door",
            command = lambda: self.newDoor(self.newDoorName.get())
        )
        choosedoorbutton.grid(row=3, column=3)


    def newDeviceFun(self, newDevice, conRate):
        devices.append(newDevice)
        device = SmartPlug(conRate)
        self.myHome.addDevice(device)
        self.createWidgets()

    def newDoor(self, newDoorName):
        devices.append(newDoorName)
        userDoor = SmartDoor()
        self.myHome.addDevice(userDoor)
        self.createWidgets()

    def editDevice(self, index):
        newWin = Toplevel(self.root)
        newWin.title("Edit device")
        newWin.geometry("450x150")

        helplabel = Label(
            newWin,
            text = "Enter device name in text box"
        )
        helplabel.grid(row=0, column=0)

        newDeviceEntry = Entry(
            newWin,
            width = 15,
            textvariable= self.editedDevice
        )
        newDeviceEntry.grid(row=0, column=1)

        switchlabel = Label(
            newWin,
            text = "Lock/Unlock switch"
        )
        switchlabel.grid(row=1, column=0)
        
        temp = self.myHome.getDevicesAt(index)
        try:
            textInput = str(temp.getOption())
        except AttributeError:
            textInput = "Door only."
        switchView = Label(
            newWin,
            text = textInput
        )
        switchView.grid(row=1, column=1)

        switchButton = Button(
            newWin,
            text = "Toggle",
            command = lambda index=index, label=switchView: self.toggleSwitch(index, label)
        )
        switchButton.grid(row=1, column=2)

        consumptionlabel = Label(
            newWin,
            text = "Consumption Rate:"
        )
        consumptionlabel.grid(row=2, column=0)

        try:
            textOutput = temp.getConsumptionRate()
        except AttributeError:
            textOutput = "Devices Only"
        consumptionView = Label(
            newWin,
            text = textOutput
        )
        consumptionView.grid(row=2, column=1)
            
        consumptionEntry = Entry(
            newWin,
            width = 10,
            textvariable = self.editedConsumptionRate
        )
        consumptionEntry.grid(row=2, column=2)

        confirmbutton = Button(
            newWin,
            text = "Confirm",
            command = lambda index=index, rate=self.editedConsumptionRate.get(), name=self.editedDevice.get(): self.confirmSettings(index, rate, name, newWin)
        )
        confirmbutton.grid(row=3, column=1)

    def toggleSwitch(self, index, label):
        try:
            tempD = self.myHome.getDevicesAt(index)
            if tempD.getOption() == False:
                tempD.setOption(True)
                label.config(text=str(tempD.getOption()))
            elif tempD.getOption() == True:
                tempD.setOption(False)
                label.config(text=str(tempD.getOption()))
        except AttributeError:
            print("This is not an option for this device.")
                
    def confirmSettings(self, index, rate, name, newWin):
        tempD = self.myHome.getDevicesAt(index)
        try:
            tempD.setConsumptionRate(rate)
        except AttributeError:
            print("Unable to enter consumption rate.")
            
        self.devices[index] = name
        self.createWidgets()
        newWin.destroy()

        
    def run(self):
        self.createWidgets()
        self.root.mainloop()

def main():
    
    myHome, devices = setUpHome()
    app = SmartHomeSystem(myHome, devices)
    app.run()

main()


















