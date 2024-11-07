import math
from graphics import *

def drawRec(win, x, y, colour):
    rec = Rectangle(x,y)
    rec.setFill(colour)
    rec.setOutline(colour)
    rec.draw(win)

def drawCircle(win, x, y, colour):
    circle = Circle(Point(x, y), 10)
    circle.setFill(colour)
    circle.setOutline(colour)
    circle.draw(win)
        
def drawLine(win, x, y, colour):
    line = Line(x, y)
    line.setFill(colour)
    line.setOutline(colour)
    line.draw(win)

def drawBlock(win, x, y, colour):
    tLeft = Point(x,y)
    bRight = Point(x+100,y+100)
    rec = Rectangle(tLeft,bRight)
    rec.setFill(colour)
    rec.setOutline(colour)
    rec.draw(win)

def drawPatchF(win, x, y, colour):
    tLine = Point(x, y)
    bLine = Point(x+100, y+100)
    tLine2 = Point(x, y+10)
    bLine2 = Point(x+100, y+90)
    for b in range(10):
        drawLine(win, tLine, bLine, colour)
        tLine.x += 10
        bLine.x -= 10
        drawLine(win, tLine2, bLine2, colour)
        tLine2.y += 10
        bLine2.y -= 10

def drawPatchPa(win, x, y, colour):
    x += 10
    y += 10
    drawCircle(win, x, y, colour)
    drawCircle(win, (x+20), y, colour)
    drawRec(win, Point((x+20),(y-10)), Point((x+30),(y+10)), colour)
    drawCircle(win, (x+30), y, colour)
    drawCircle(win, (x+50), y, colour)
    drawCircle(win, (x+70), y, colour)
    drawRec(win, Point((x+70),(y-10)), Point((x+80),(y+10)), colour)
    drawCircle(win, (x+80), y, colour)

def drawPatchPb(win, x, y, colour):
    x += 10
    y += 10
    drawCircle(win, x, y, colour)
    drawRec(win, Point(x,(y-10)), Point((x+10),(y+10)), colour)
    drawCircle(win, (x+10), y, colour)
    drawCircle(win, (x+30), y, colour)
    drawCircle(win, (x+50), y, colour)
    drawRec(win, Point((x+50),(y-10)), Point((x+60),(y+10)), colour)
    drawCircle(win, (x+60), y, colour)
    drawCircle(win, (x+80), y, colour)

def drawPatchP(win, x, y, colour):
    drawPatchPa(win, x, y, colour)
    drawPatchPb(win, x, (y+20), colour)
    drawPatchPa(win, x, (y+40), colour)
    drawPatchPb(win, x, (y+60), colour)
    drawPatchPa(win, x, (y+80), colour)
        
def drawPatchArtWork(win, x, y, colour1, colour2, colour3, patchSize):
    nth = patchSize
    y -= 100
    for a in range(patchSize-1):
        nth -= 1
        y += 100
        x = 0
        for b in range(nth):
            if b == 0 or a == 0:
                drawPatchP(win, x, y, colour1)
                x += 100
            else:
                drawBlock(win, x, y, colour1)
                x += 100
    x = 0
    y = (patchSize*100) - 100
    for c in range(patchSize):
        if c % 2:
            drawBlock(win, x, y, colour2)
            x += 100
            y -= 100
        else:
            drawPatchF(win, x, y, colour2)
            x += 100
            y -= 100
    x = (patchSize*100)
    y = (patchSize*100) - 100
    nth = patchSize
    for d in range(patchSize-1):
        nth -= 1
        x -= 100
        y = (patchSize*100) - 100
        for e in range(nth):
            if d % 2:
                drawBlock(win, x, y, colour3)
                y -= 100
            else:
                drawPatchF(win, x, y, colour3)
                y -= 100            

def drawOkClose(win, winSize):
    okButton = Rectangle(Point(0,0), Point(30,30))
    okButton.setOutline("White")
    okButton.setFill("Black")
    okButton.draw(win)
    okText = Text(Point(15,15), "OK")
    okText.setOutline("White")
    okText.setFill("White")
    okText.setSize(14)
    okText.draw(win)
    closeButton = Rectangle(Point((winSize-30),0), Point(winSize,30))
    closeButton.setOutline("White")
    closeButton.setFill("Red")
    closeButton.draw(win)
    closeLine1 = Line(Point((winSize-25),25), Point((winSize-5),5))
    closeLine1.setFill("White")
    closeLine1.draw(win)
    closeLine2 = Line(Point((winSize-25),5), Point((winSize-5),25))
    closeLine2.setFill("White")
    closeLine2.draw(win)

def drawBorder(win, tLeft, tRight, bRight, bLeft):
    drawLine(win, tLeft, tRight, "Black")
    drawLine(win, tLeft, bLeft, "Black")
    drawLine(win, bLeft, bRight, "Black")
    drawLine(win, bRight, tRight, "Black")
        
def main():
    colour = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    validSize = [5, 7, 9]
    sizeSelect = True
    colourSelect1 = True
    colour1 = ""
    colourSelect2 = True
    colour2 = ""
    colourSelect3 = True
    colour3 = ""
    x = 0
    y = 0
    

    print("Welcome to up2204118's patchwork designer!")

    while sizeSelect == True:
        print("Valid sizes for patchwork")
        print("5 for 5 x 5")
        print("7 for 7 x 7")
        print("9 for 9 x 9")
        patchSize = int(input("Please enter a size for your patchwork."))
        for sCheck in range(len(validSize)):
            if patchSize == validSize[sCheck]:
                print(f"Size selected: {patchSize}")
                sizeSelect = False
            elif sCheck == len(validSize)-1 and sizeSelect == False:
                print("This is not a valid size, please refer to the list.")
                
    print("===============")
    print("Here is your list of available colours.")
    print("===============")
    for i in range(len(colour)):
        print(colour[i])
    print("===============")
    while colourSelect1 == True:
        colourEntry1 = input("Please your first of three colours.")
        for cCheck in range(len(colour)):
            if colourEntry1.lower() == colour[cCheck]:
                colour1 = colour[cCheck]
                print(f"Colour selected: {colour1}")
                colourSelect1 = False
            elif cCheck == len(colour)-1 and colour1 == "":
                print("This is not a valid colour, please refer to the list.")
    while colourSelect2 == True:
        colourEntry2 = input("Please your second of three colours.")
        for cCheck2 in range(len(colour)):
            if colourEntry2.lower() == colour[cCheck2] and colourEntry2 != colourEntry1:
                colour2 = colour[cCheck2]
                print(f"Colour selected: {colour2}")
                colourSelect2 = False
            elif colourEntry2 == colourEntry1:
                print("You cannot use two of the same colour, please refer to the list.")
                break
            elif cCheck2 == len(colour)-1 and colour2 == "":
                print("This is not a valid colour, please refer to the list.")
    while colourSelect3 == True:
        colourEntry3 = input("Please your second of three colours.")
        for cCheck3 in range(len(colour)):
            if colourEntry3.lower() == colour[cCheck3] and colourEntry3 != colourEntry1 and colourEntry3 != colourEntry2:
                colour3 = colour[cCheck3]
                print(f"Colour selected: {colour3}")
                colourSelect3 = False
            elif colourEntry3 == colourEntry1 or colourEntry3 == colourEntry2:
                print("You cannot use two of the same colour, please refer to the list.")
                break
            elif cCheck3 == len(colour)-1 and colour3 == "":
                print("This is not a valid colour, please refer to the list.")

    print("===============")
    print("You have selected...")
    print(f"Size: {patchSize} x {patchSize}")
    print(f"Colour 1: {colour1}")
    print(f"Colour 2: {colour2}")
    print(f"Colour 3: {colour3}")
    print("===============")
    
    winSize = patchSize * 100
    win = GraphWin("up2204118 Patchwork", winSize, winSize)
    win.setBackground("White")

    drawPatchArtWork(win, x, y, colour1, colour2, colour3, patchSize)

    selectionMode = True
    
    drawOkClose(win, winSize)
    okButtonX = 30
    okButtonY = 30
    xButtonX = winSize - 30
    xButtonY = winSize - 30
    
    
    while selectionMode == True:
        mouseClick = win.getMouse()
        p1 = mouseClick.x
        p2 = mouseClick.y
        if p1 <= okButtonX and p2 <= okButtonY:
            print("##")
        elif p1 >= xButtonX and p2 <= okButtonY:
            win.close()
            selectionMode = False
        elif p1 <= 100 and p2 <= 100:
            tRight = Point(100, 0)
            tLeft = Point(0, 0)
            bRight = Point(100, 100)
            bLeft = Point(0, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)
        elif p1 <= 200 and p1 > 100 and p2 <= 100:
            tRight = Point(200, 0)
            tLeft = Point(100, 0)
            bRight = Point(200, 100)
            bLeft = Point(100, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)
        elif p1 <= 300 and p1 > 200 and p2 <= 100:
            tRight = Point(300, 0)
            tLeft = Point(200, 0)
            bRight = Point(300, 100)
            bLeft = Point(200, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)
        elif p1 <= 400 and p1 > 300 and p2 <= 100:
            tRight = Point(400, 0)
            tLeft = Point(300, 0)
            bRight = Point(400, 100)
            bLeft = Point(300, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)
        elif p1 <= 500 and p1 > 400 and p2 <= 100:
            tRight = Point(500, 0)
            tLeft = Point(400, 0)
            bRight = Point(500, 100)
            bLeft = Point(400, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)
        elif p1 <= 600 and p1 > 500 and p2 <= 100:
            tRight = Point(600, 0)
            tLeft = Point(500, 0)
            bRight = Point(600, 100)
            bLeft = Point(500, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)
        elif p1 <= 700 and p1 > 600 and p2 <= 100:
            tRight = Point(700, 0)
            tLeft = Point(600, 0)
            bRight = Point(700, 100)
            bLeft = Point(600, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)
        elif p1 <= 800 and p1 > 700 and p2 <= 100:
            tRight = Point(800, 0)
            tLeft = Point(700, 0)
            bRight = Point(800, 100)
            bLeft = Point(700, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)
        elif p1 <= 900 and p1 > 800 and p2 <= 100:
            tRight = Point(900, 0)
            tLeft = Point(800, 0)
            bRight = Point(900, 100)
            bLeft = Point(800, 100)
            drawBorder(win, tLeft, tRight, bRight, bLeft)


            
    

main()
