#!/usr/bin/python3

from time import sleep
from LiquidCrystal import LiquidCrystal, HIGH

lcd = LiquidCrystal( 0 );

def test_1():
    lcd.begin( 16, 2 )
    lcd.setBacklight( HIGH )
    sleep( 1 )

def test_2():
    lcd.setCursor( 0, 0 )
    lcd.print( "I2C Protocol" )
    sleep( 1 )

def test_3():
    for i in range( 5 ):
        lcd.setCursor( 0, 1 )
        lcd.print( "Hello world." )
        lcd.setCursor( 13, 1 )
        lcd.print( i )
        sleep( 1 )

def test_4():
    lcd.setCursor( 0, 1 )
    lcd.print( "Hello world. this is a very long string that does not fit" )
    sleep( 1 )
