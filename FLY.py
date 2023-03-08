##########################################################
#Title: Fly guy
#Programmer: Ibrahim Muni
#Date Started:09/01/2017
#Date Last Modified:
##########################################################

from tkinter import *
from math import *
from time import *
from random import *
import random


root = Tk()
s = Canvas( root, width =380, height =580, background = "white")
s.pack()

flyer = PhotoImage(file = "Flyer1.gif")
SunnySkyBackground = PhotoImage(file ="SunnySky.gif")
cloud = PhotoImage(file = "cloud.gif")
playB = PhotoImage(file = "Play-button.gif")
enemy = PhotoImage(file = "enemy.gif")
dark = PhotoImage(file = "cloudD.gif")
backG = PhotoImage(file = "back.gif")
s.update()


def setInitialValues():
    global x, y, xSpeed,maxSpeed, FlyerL, Qpressed, cloudSpeed,ax,ax2,ax3,ay,ay2,ay3,py,px,enemys
    global spread,cloudA,cloudB,cloudC,cloudD,cloudE,colxSpace,colySpace,coin,gameRunning,player 
    global xspread,yspread,nopoint,ax4,ax5,cx,gameRunning,gameMode,ay5,ay4,xList,Lose,playerHeight
    global distance, meter , xMouseMotion, yMouseMotion,mode , enemyX , enemyY,lvl,B
    global enemys,Lose,gameRunning
    
    x = 300
    y = 450
    xSpeed = 0
    maxSpeed = 3
    FlyerL = 0
    Qpressed = False
    cloudSpeed = 10
    ax = 40
    ax2 = 190
    ax3 = 300
    ay = 50
    ay2 = -180
    ay3 = -410
    xList =[40,190,300]
    spread = 123
    cloudA = 0
    cloudB = 0
    cloudC = 0
    cloudD = 0
    cloudE = 0
    colxSpace = 9
    colySpace = 55
    coins = 0
    gameRunning = True
    player = flyer
    xspread = 95
    yspread = 55
    nopoint = 1
    playerHeight = 108
    ax4 = 40
    ax5 = 190
    cx = 40
    gameRunning = True
    gameMode = 0
    xList = [40,190,300]
    ay5 = 50
    ay4 = -410
    Lose = False
    py = y - 54
    px = x - 26
    distance = 0
    meter = cloudSpeed 
    xMouseMotion = 0
    yMouseMotion = 0
    mode = "IntroScreen"
    enemyX = 40
    enemyY = -180
    lvl = 5000
    B = s.create_image(200,300,image=SunnySkyBackground)
    if distance<lvl:
        s.create_image(200,300,image=SunnySkyBackground)
    enemys = 0
    gameRunning = True

    

def printInstructions():
    intr = s.create_text(50,25,text = "Instructions", anchor=W,font="Times 40")
    startMessage = s.create_text(50,50,text = "Press the Left and right arrow keys", anchor=W,font="Times 10")
    Quit = s.create_text(50,65,text = "press q to quit", anchor=W,font="Times 10")
    s.update()
    sleep(2)
    s.delete(startMessage,Quit,intr)
    Lose == False

    

def keyDownHandler( event ):
    global xSpeed, Qpressed
    
    if event.keysym == "Left":   
        xSpeed = -13
        
    elif event.keysym == "Right":   
        xSpeed = 13

    elif event.keysym == "q" or event.keysym == "Q":
        root.destroy()

def keyUpHandler( event ):
    global xSpeed

    xSpeed = 0
    
def mouseClick(event):
    global xMouse, yMouse
    xMouse = event.x
    yMouse = event.y
    
def mouseMotion(event): 
    global xMouseMotion, yMouseMotion, title, titleButton, backButton
    s.bind("<Motion>", mouseMotion)
    s.bind("<Button-1>", mouseClick)
    #Set cursor location
    xMouseMotion = event.x
    yMouseMotion = event.y

    #If cursor is in area of buttons
    if xMouseMotion >= 15 and xMouseMotion <= 365:

        #If cursor is within range of Play Button
        if yMouseMotion >= 75 and yMouseMotion <= 225:
            runGame()
            s.delete(playButton)
    
    s.update()
    sleep(0.001)
    s.delete()   

def updateFlyerLPosition():
    global x

    if x < 370 and x > 10:
        x = x + xSpeed 
    else:
        if x >= 370:
            x = 369.99
        else:
            x = 10.01


def drawFlyerL():
    global FlyerL,red,player,nopoint,Lose,ay,ay2,ay3,ay4,ay5,py,px
    global ax,ax2,ax3,ax4,ax5,xspread,x,playerHeight,cloudX1,cloudX2,cloudX3,cloudX4,cloudX5

    
    FlyerL = s.create_image(x, y, image= player)
    
    
def drawCloud():
    global cloudSpeed,ax,ay,ay2,ay3,ax2,ax3,cloudA,cloudB,cloudC,cloudD,cloudE,coins,ax4,ax5,cx,ay5,ay4
    global xList,Lose,cloudX1,cloudX2,cloudX3,cloudX4,cloudX5,enemyX,enemyY,distance,cloud,lvl

    if lvl<distance<lvl+50:
        cloud = dark        
        
    cloudA = s.create_image(ax,ay,image= cloud)
    cloudB = s.create_image(ax2,ay2,image= cloud)
    cloudC = s.create_image(ax3,ay3,image= cloud)
    cloudD = s.create_image(ax4,ay4,image = cloud)
    cloudE = s.create_image(ax5,ay5,image = cloud)
        
    if ay >= 725 :
        ay = -20
        ax = choice(xList)
    elif ay2 >= 725 :
      ay2 = -20
      ax2 = choice(xList)
      cx = choice(xList) 
    elif ay3 >= 725 :
        ay3 = -20
        ax3 = choice(xList)
    elif ay4 >= 725 :
      ay4 = -20
      ax4 = choice(xList)
    elif ay5 >= 725 :
      ay5 = -20
      ax5 = choice(xList)
    elif enemyY >= 725:
      enemyY = -20
      enemyX = choice(xList)
    else:
      ay = ay + cloudSpeed
      ay2 = ay2 + cloudSpeed
      ay3 = ay3 + cloudSpeed
      ay4 = ay4 + cloudSpeed
      ay5 = ay5 + cloudSpeed
      enemyY = enemyY + cloudSpeed
      

def getHit():
    global nopoint,Lose,ay,ay2,ay3,ay4,ay5,py,px,cloudSpeed
    global ax,ax2,ax3,ax4,ax5,xspread,x,playerHeight,cloudX1,cloudX2,cloudX3,cloudX4,cloudX5

    cloudX1 = ax + xspread
    cloudX2 = ax2 + xspread
    cloudX3 = ax3 + xspread
    cloudX4 = ax4 + xspread
    cloudX5 = ax5 + xspread
    

    if py <= ay:
        if (py+playerHeight)>ay:
            if ax <= x <= cloudX1:
                cloudSpeed =  -6
    if py <= ay2:
        if (py+playerHeight)>ay2:
            if ax2 <= x <= cloudX2:
                cloudSpeed =  -6
    if py <= ay3:
        if (py+playerHeight)>ay3:
            if ax3 <= x <= cloudX3:
                cloudSpeed =  -6

    if py <= ay4:
        if (py+playerHeight)>ay4:
            if ax4 <= x <= cloudX4:
                cloudSpeed =  -6

    if py <= ay5:
        if (py+playerHeight)>ay5:
            if ax5 <= x <= cloudX5:
                cloudSpeed =  -6
    if ay < -100 and ay2 < -100 and ay3 < -100 and ay4 < -100 and ay5 < -100 :
        s.delete(FlyerL)
        Lose = True


def distanceCount():
    global distance,distanceText
    if cloudSpeed > 0:
        distance = round(distance + meter/2)
        distanceText = s.create_text( 190, 10, text=("Distance:",distance,"m"), anchor=CENTER, font="Times 20",fill="red")


def stopGame():
    global GOV,DIS

    gameRunning = False
    s.delete(FlyerL)
    GOV = s.create_text( 200, 300, text="Game Over", anchor=CENTER, font="Times 30")
    DIS = s.create_text( 200, 350, text=("Distance:",distance), anchor=CENTER, font="Times 30")
    s.update()
    sleep(2)
    s.delete(GOV,DIS)
    s.update()
    start()



    
def start():
    global gameMode
    gameMode = "intro screen"
    drawIntroScreen()
    Lose = False


def drawIntroScreen():
        global playButton
        s.bind("<Motion>", mouseMotion)
        s.bind("<Button-1>", mouseClick)

        playButton = s.create_image(190,200,image = playB)
        
        s.update()


def runGame():
    global startMessage, gameRunning,Lose

    setInitialValues()
    printInstructions()


    while Lose == False:
        if lvl+50 > distance >lvl:
           s.create_image(200,300,image=backG)
           cloudSpeed = 14
        updateFlyerLPosition()    
        drawFlyerL()
        getHit()
        drawCloud()
        distanceCount()
        s.update()
        sleep(0.01)
        s.delete(FlyerL,cloudA,cloudB,cloudC,cloudD,cloudE,distanceText,enemys)

    stopGame()
    start()

     
      
   
root.after(0, start)
s.bind( "<Key>", keyDownHandler)
s.bind( "<KeyRelease>",keyUpHandler)
##s.bind("<Button-1>", mouseClickHandler)
##s.bind("<ButtonRelease-1>", mouseReleaseHandler)
##s.bind("<Motion>", mouseMotion)
##s.bind("<Button-1>", mouseClick)
s.pack()
s.focus_set()
root.mainloop()
