#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        # időzítő
        self.ido = StopWatch()

    def csipog(self):
        for i in range(3):
            self.ev3.speaker.beep()
        
    def vonalkovet(self):
        #felvátva hajtom a motorokat egyik gyorsabb másik lassabb ha letér csere
        while True:
            if self.cs.reflection() > 35:
                self.bm.run(200)
                self.jm.run(100)
            else:
                self.jm.run(200)
                self.bm.run(100)

    def aku(self):
        volt = self.ev3.battery.voltage()/1000
        amper = self.ev3.battery.current()/1000
        print("A feszültség értéke ",volt)
        print("Az áramerősség: ",amper)
        self.ev3.screen.print("Virtuális Pékség")
        wait(1000)

    
    def feladat1(self):
        #1.	feladat: Haladjon az asztal széle fele a robot majd álljon meg a szélén.
        # asztal széle:57
        # asztal széle felesen:30
        # asztal széle után: 0
        # fekete vonal: 7-8
        ut = (57+30)/2
        while self.cs.reflection() > ut:
            self.robot.drive(100,0)
            print("uborka: ",self.cs.reflection())
        self.robot.stop(Stop.BRAKE)



    def feladat2(self):
        self.ido.reset()
        ut = (57+30)/2
        while self.cs.reflection() > ut:
            self.robot.drive(100,0)
            print("uborka: ",self.cs.reflection())
        self.robot.stop(Stop.BRAKE)
        elteltIdo = self.ido.time()
        self.robot.drive(-100,0)
        wait(elteltIdo)
        self.robot.stop(Stop.BRAKE)

    
    def feladat3(self):
        while self.ir.distance() > 10:
            self.robot.drive(self.ir.distance(),0)
        self.robot.stop(Stop.Brake)