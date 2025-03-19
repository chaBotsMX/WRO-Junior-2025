from Junior_2025_Kirby import *

kirby = Kirby()

def checkBluetoothButton():
    if(Button.BLUETOOTH in kirby.hub.buttons.pressed()):
        kirby.hub.speaker.beep(500, 500)
        wait(200)
        while True:
            print("Line Sensor:", kirby.lineSensor.reflection())
            #print("Color sensor:", kirby.colorSensor.color())
            #print("color sensor: ", kirby.colorSensor.hsv())
            #print("heading: ", kirby.getAngle(kirby.hub.imu.heading()))
            #print("battery voltage", kirby.hub.battery.voltage())
            #kirby.hub.display.text(str(round(kirby.hub.battery.voltage()/1000, 2)))

def checkLeftButton():
    global MAX_LIGHT, MIN_LIGHT
    if(Button.LEFT in kirby.hub.buttons.pressed()):
        kirby.hub.speaker.beep(200, 400)
        for i in range (50000):
            if MAX_LIGHT < kirby.lineSensor.reflection():
                MAX_LIGHT = kirby.lineSensor.reflection()
            if MIN_LIGHT > kirby.lineSensor.reflection():
                MIN_LIGHT = kirby.lineSensor.reflection()
        kirby.hub.speaker.beep(100, 400)
        print("black: ", MIN_LIGHT)
        print("white: ", MAX_LIGHT)

def start():
    kirby.frontMotor.brake()
    kirby.turnInPlace(0, 60, 8, 0.1)
    kirby.driveStraightTime(1300, 100)
    kirby.turnInPlace(0, 60, 8, 0.1)
    kirby.driveStraightDegrees(855, -60, 1.5, 0.1)
    kirby.turnInPlace(-90, 60, 8, 0.1)
    wait(100)

def rover():
    kirby.driveStraightTime(1300, 80)
    kirby.turnInPlace(-90, 60, 8, 0.1)
    kirby.hub.imu.reset_heading(-90)
    wait(400)
    kirby.driveStraightDegrees(664, -60, 1.5, 0.1)
    wait(200)
    kirby.moveFrontMotorDegrees(-90,200)
    kirby.turnInPlace(0, 40, 10, 0.1)
    wait(100)

def takeWaterTanks():
    kirby.moveBackMotorDegrees(185, 300)
    wait(500)
    kirby.moveFrontMotorDegrees(0,500)
    kirby.turnInPlace(0,60,10,0.1)

    kirby.driveStraightDegrees(350, 60, 1.5, 0.1)
    kirby.turnInPlace(0,60,10,0.1)
    wait(200)
    kirby.driveStraightDegrees(100, -60,1.5,0.1)
    wait(200)
    kirby.driveStraightDegrees(150, 60, 1.5, 0.1)
    wait(400)
    kirby.driveStraightDegrees(210, -60,1.5,0.1)
    kirby.moveBackMotorDegrees(0, 200)
    kirby.turnInPlace(0, 60, 10, 0.1)
    kirby.driveStraightDegrees(100,60,1.5,0.1)
    kirby.turnInPlace(90,60,10,0.1)
    wait(100)

def goToBox():
    kirby.driveStraightDegrees(900,80,1.5,0.1)
    kirby.driveStraightTime(1500, 60)
    kirby.turnInPlace(90,60,10,0.1)

    kirby.driveStraightDegrees(280,-60,1.5,0.1)
    kirby.turnInPlace(90,60,10,0.1)
    wait(100)

    kirby.turnInPlace(0, 60, 10, 0.1)
    kirby.driveStraightTime(1000, 50)
    kirby.turnInPlace(0, 60, 10, 0.1)
    kirby.driveStraightDegrees(360,-60,1.5,0.1)
    kirby.turnInPlace(0, 30, 10, 0.1)
    kirby.moveBackMotorDegrees(187, 300)
    wait(200)
    kirby.driveStraightDegrees(100,60,1.5,0.1)
    kirby.moveBackMotorDegrees(120, 1000)
    kirby.driveStraightDegrees(85,60,1.5,0.1)
    kirby.driveStraightDegrees(100,-60,1.5,0.1)

def leaveWaterTanks():
    kirby.moveFrontMotorDegrees(-300,600)
    kirby.turnInPlace(200, 60, 10, 0.1)
    kirby.driveStraightDegrees(150,-60,1.5,0.1)
    wait(500)