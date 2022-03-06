#!/usr/bin/python3

import smbus
from Arduino import *

MCP23008_ADDRESS = 0x20

# registers
MCP23008_IODIR = 0x00
MCP23008_IPOL = 0x01
MCP23008_GPINTEN = 0x02
MCP23008_DEFVAL = 0x03
MCP23008_INTCON = 0x04
MCP23008_IOCON = 0x05
MCP23008_GPPU = 0x06
MCP23008_INTF = 0x07
MCP23008_INTCAP = 0x08
MCP23008_GPIO = 0x09
MCP23008_OLAT = 0x0A

class MCP23008:
  
  def __init__( self ):
    self.i2caddr = 0
    self.bus = smbus.SMBus(1)

  def begin( self, addr = 0 ):
    addr = abs( int( addr ) )
    if addr > 7:
      addr = 7

    self.i2caddr = MCP23008_ADDRESS | addr

    self.bus.write_byte(self.i2caddr, MCP23008_IODIR)
    self.bus.write_byte(self.i2caddr, 0xFF)
    self.bus.write_byte(self.i2caddr, 0x00)
    self.bus.write_byte(self.i2caddr, 0x00)
    self.bus.write_byte(self.i2caddr, 0x00)
    self.bus.write_byte(self.i2caddr, 0x00)
    self.bus.write_byte(self.i2caddr, 0x00)
    self.bus.write_byte(self.i2caddr, 0x00)
    self.bus.write_byte(self.i2caddr, 0x00)
    self.bus.write_byte(self.i2caddr, 0x00)
    self.bus.write_byte(self.i2caddr, 0x00)

  def pinMode( self, p, d ):
    p = abs( int( p ) )
    if p > 7:
      return

	#    read the current IODIR
    self.bus.write_byte(self.i2caddr, MCP23008_IODIR)
    iodir = self.bus.read_byte(self.i2caddr)

    # set the pin and direction
#   if (d == INPUT) {
#     iodir |= 1 << p;
#   } else {
#     iodir &= ~(1 << p);
#   }
#
#   // write the new IODIR
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_IODIR);
#   Wire.write(iodir);
#   Wire.endTransmission();
# }
  
  def digitalWrite( self, p, d ):
    pass
  
  def pullUp( self, p, d ):
    pass

  def digitalRead( self, p ):
    pass

# https://github.com/smoya/SPI_II2C_LCD_for_ElecFreaks1602/blob/master/MCP23008.h

# // i2c expander library - slow I/O!
#
# // also works with the MCP23009
#
# // Don't forget the Wire library
# class MCP23008 {
# public:
#   void begin(uint8_t addr);
#   void begin(void);
#
#   void pinMode(uint8_t p, uint8_t d);
#   void digitalWrite(uint8_t p, uint8_t d);
#   void pullUp(uint8_t p, uint8_t d);
#   uint8_t digitalRead(uint8_t p);
#
#  private:
#   uint8_t i2caddr;
# };
#
# #define MCP23008_ADDRESS 0x20
#
# // registers
# #define MCP23008_IODIR 0x00
# #define MCP23008_IPOL 0x01
# #define MCP23008_GPINTEN 0x02
# #define MCP23008_DEFVAL 0x03
# #define MCP23008_INTCON 0x04
# #define MCP23008_IOCON 0x05
# #define MCP23008_GPPU 0x06
# #define MCP23008_INTF 0x07
# #define MCP23008_INTCAP 0x08
# #define MCP23008_GPIO 0x09
# #define MCP23008_OLAT 0x0A
#


# https://github.com/smoya/SPI_II2C_LCD_for_ElecFreaks1602/blob/master/MCP23008.cpp

# // Code by Adafruit Industries/Limor Fried
# // License: LGPL
#
# #include <Wire.h>
# #include <avr/pgmspace.h>
# #include "MCP23008.h"
# #include <Arduino.h>
#
#
# ////////////////////////////////////////////////////////////////////////////////
# // RTC_DS1307 implementation
#
# void MCP23008::begin(uint8_t addr) {
#   if (addr > 7) {
#     addr = 7;
#   }
#   i2caddr = addr;
#
#   Wire.begin();
#
#   // set defaults!
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_IODIR);
#   Wire.write(0xFF);  // all inputs
#   Wire.write(0x00);
#   Wire.write(0x00);
#   Wire.write(0x00);
#   Wire.write(0x00);
#   Wire.write(0x00);
#   Wire.write(0x00);
#   Wire.write(0x00);
#   Wire.write(0x00);
#   Wire.write(0x00);
#   Wire.endTransmission();
#
# }
#
# void MCP23008::begin(void) {
#   begin(0);
# }
#
# void MCP23008::pinMode(uint8_t p, uint8_t d) {
#   uint8_t iodir;
#
#
#   // only 8 bits!
#   if (p > 7)
#     return;
#
#   // read the current IODIR
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_IODIR);
#   Wire.endTransmission();
#
#   Wire.requestFrom(MCP23008_ADDRESS | i2caddr, 1);
#   iodir = Wire.read();
#
#   // set the pin and direction
#   if (d == INPUT) {
#     iodir |= 1 << p;
#   } else {
#     iodir &= ~(1 << p);
#   }
#
#   // write the new IODIR
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_IODIR);
#   Wire.write(iodir);
#   Wire.endTransmission();
# }
#
#
# void MCP23008::digitalWrite(uint8_t p, uint8_t d) {
#   uint8_t gpio;
#
#   // only 8 bits!
#   if (p > 7)
#     return;
#
#   // read the current GPIO output latches
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_OLAT);
#   Wire.endTransmission();
#
#   Wire.requestFrom(MCP23008_ADDRESS | i2caddr, 1);
#   gpio = Wire.read();
#
#   // set the pin and direction
#   if (d == HIGH) {
#     gpio |= 1 << p;
#   } else {
#     gpio &= ~(1 << p);
#   }
#
#   // write the new GPIO
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_GPIO);
#   Wire.write(gpio);
#   Wire.endTransmission();
# }
#
# void MCP23008::pullUp(uint8_t p, uint8_t d) {
#   uint8_t gppu;
#
#   // only 8 bits!
#   if (p > 7)
#     return;
#
#   // read the current pullup resistor set
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_GPPU);
#   Wire.endTransmission();
#
#   Wire.requestFrom(MCP23008_ADDRESS | i2caddr, 1);
#   gppu = Wire.read();
#
#   // set the pin and direction
#   if (d == HIGH) {
#     gppu |= 1 << p;
#   } else {
#     gppu &= ~(1 << p);
#   }
#
#   // write the new GPIO
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_GPPU);
#   Wire.write(gppu);
#   Wire.endTransmission();
# }
#
# uint8_t MCP23008::digitalRead(uint8_t p) {
#   // only 8 bits!
#   if (p > 7)
#     return 0;
#
#   // read the current GPIO
#   Wire.beginTransmission(MCP23008_ADDRESS | i2caddr);
#   Wire.write(MCP23008_GPIO);
#   Wire.endTransmission();
#
#   Wire.requestFrom(MCP23008_ADDRESS | i2caddr, 1);
#   return (Wire.read() >> p) & 0x1;
# }
