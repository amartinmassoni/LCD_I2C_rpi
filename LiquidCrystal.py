#!/usr/bin/python3

# https://github.com/smoya/SPI_II2C_LCD_for_ElecFreaks1602/blob/master/LiquidCrystal.h
#
# #ifndef LiquidCrystal_h
# #define LiquidCrystal_h
#
# #include <inttypes.h>
# #include "Print.h"
from MCP23008 import *
#
# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80
#
# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00
#
# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00
#
# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00
#
# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00
# 
# class LiquidCrystal : public Print {
class LiquidCrystal:
# public:
#   LiquidCrystal(uint8_t rs, uint8_t enable,
# 		uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3,
# 		uint8_t d4, uint8_t d5, uint8_t d6, uint8_t d7);
#   LiquidCrystal(uint8_t rs, uint8_t rw, uint8_t enable,
# 		uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3,
# 		uint8_t d4, uint8_t d5, uint8_t d6, uint8_t d7);
#   LiquidCrystal(uint8_t rs, uint8_t rw, uint8_t enable,
# 		uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3);
#   LiquidCrystal(uint8_t rs, uint8_t enable,
# 		uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3);
# 
#   LiquidCrystal(uint8_t i2cAddr);
#   LiquidCrystal(uint8_t data, uint8_t clock, uint8_t latch);
# 
#   void init(uint8_t fourbitmode, uint8_t rs, uint8_t rw, uint8_t enable,
# 	    uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3,
# 	    uint8_t d4, uint8_t d5, uint8_t d6, uint8_t d7);
#     
#   void begin(uint8_t cols, uint8_t rows, uint8_t charsize = LCD_5x8DOTS);
# 
#   void clear();
#   void home();
# 
#   void noDisplay();
#   void display();
#   void noBlink();
#   void blink();
#   void noCursor();
#   void cursor();
#   void scrollDisplayLeft();
#   void scrollDisplayRight();
#   void leftToRight();
#   void rightToLeft();
#   void autoscroll();
#   void noAutoscroll();
#   
#   // only if using backpack
#   void setBacklight(uint8_t status); 
# 
#   void createChar(uint8_t, uint8_t[]);
#   void setCursor(uint8_t, uint8_t); 
#   virtual size_t write(uint8_t);
#   void command(uint8_t);
# private:
#   void send(uint8_t, uint8_t);
#   void write4bits(uint8_t);
#   void write8bits(uint8_t);
#   void pulseEnable();
#   void _digitalWrite(uint8_t, uint8_t);
#   void _pinMode(uint8_t, uint8_t);
# 
#   uint8_t _rs_pin; // LOW: command.  HIGH: character.
#   uint8_t _rw_pin; // LOW: write to LCD.  HIGH: read from LCD.
#   uint8_t _enable_pin; // activated by a HIGH pulse.
#   uint8_t _data_pins[8];
# 
#   uint8_t _displayfunction;
#   uint8_t _displaycontrol;
#   uint8_t _displaymode;
# 
#   uint8_t _initialized;
# 
#   uint8_t _numlines,_currline;
# 
#   uint8_t _SPIclock, _SPIdata, _SPIlatch;
#   uint8_t _SPIbuff;
# 
#   uint8_t _i2cAddr;
#   MCP23008 _i2c;
# };
# 
# #endif

# https://github.com/smoya/SPI_II2C_LCD_for_ElecFreaks1602/blob/master/LiquidCrystal.cpp
#
# #include "LiquidCrystal.h"
# 
# #include <stdio.h>
# #include <string.h>
# #include <inttypes.h>
# #include "Arduino.h"
# 
# // When the display powers up, it is configured as follows:
# //
# // 1. Display clear
# // 2. Function set: 
# //    DL = 1; 8-bit interface data 
# //    N = 0; 1-line display 
# //    F = 0; 5x8 dot character font 
# // 3. Display on/off control: 
# //    D = 0; Display off 
# //    C = 0; Cursor off 
# //    B = 0; Blinking off 
# // 4. Entry mode set: 
# //    I/D = 1; Increment by 1 
# //    S = 0; No shift 
# //
# // Note, however, that resetting the Arduino doesn't reset the LCD, so we
# // can't assume that its in that state when a sketch starts (and the
# // LiquidCrystal constructor is called).
# 
# LiquidCrystal::LiquidCrystal(uint8_t rs, uint8_t rw, uint8_t enable,
# 			     uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3,
# 			     uint8_t d4, uint8_t d5, uint8_t d6, uint8_t d7)
# {
#   init(0, rs, rw, enable, d0, d1, d2, d3, d4, d5, d6, d7);
# }
# 
# LiquidCrystal::LiquidCrystal(uint8_t rs, uint8_t enable,
# 			     uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3,
# 			     uint8_t d4, uint8_t d5, uint8_t d6, uint8_t d7)
# {
#   init(0, rs, 255, enable, d0, d1, d2, d3, d4, d5, d6, d7);
# }
# 
# LiquidCrystal::LiquidCrystal(uint8_t rs, uint8_t rw, uint8_t enable,
# 			     uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3)
# {
#   init(1, rs, rw, enable, d0, d1, d2, d3, 0, 0, 0, 0);
# }
# 
# LiquidCrystal::LiquidCrystal(uint8_t rs,  uint8_t enable,
# 			     uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3)
# {
#   init(1, rs, 255, enable, d0, d1, d2, d3, 0, 0, 0, 0);
# }
# 
# LiquidCrystal::LiquidCrystal(uint8_t i2caddr) {
#   _i2cAddr = i2caddr;
# 
#   _displayfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS;
#   
#   // the I/O expander pinout
#   _rs_pin = 7;
#   _rw_pin = 255;
#   _enable_pin = 6;
#   _data_pins[0] = 5;  // really d4
#   _data_pins[1] = 4;  // really d5
#   _data_pins[2] = 3;  // really d6
#   _data_pins[3] = 2;  // really d7
#   
#   // we can't begin() yet :(
# }
  def __init__( self, i2caddr ):
    self._i2cAddr = i2caddr
    self._displayfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS
	
    # the I/O expander pinout
    self._rs_pin = 7
    self._rw_pin = 255
    self._enable_pin = 6
    self._data_pins = [ 5,  # really d4
                        4,  # really d5
                        3,  # really d6
                        2 ] # really d7
# 
# 
# LiquidCrystal::LiquidCrystal(uint8_t data, uint8_t clock, uint8_t latch ) {
#   _i2cAddr = 255;
# 
#   _displayfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS;
#   
#   // the SPI expander pinout
#   _rs_pin = 7;
#   _rw_pin = 255;
#   _enable_pin = 6;
#   _data_pins[0] = 5;  // really d4
#   _data_pins[1] = 4;  // really d5
#   _data_pins[2] = 3;  // really d6
#   _data_pins[3] = 2;  // really d7
#   
#   _SPIdata = data;
#   _SPIclock = clock;
#   _SPIlatch = latch;
# 
#   pinMode(_SPIdata, OUTPUT);
#   pinMode(_SPIclock, OUTPUT);
#   pinMode(_SPIlatch, OUTPUT);
#   _SPIbuff = 0;
# 
#   // we can't begin() yet :(
#   begin(16,1);
# }
# 
# 
# void LiquidCrystal::init(uint8_t fourbitmode, uint8_t rs, uint8_t rw, uint8_t enable,
# 			 uint8_t d0, uint8_t d1, uint8_t d2, uint8_t d3,
# 			 uint8_t d4, uint8_t d5, uint8_t d6, uint8_t d7)
# {
#   _rs_pin = rs;
#   _rw_pin = rw;
#   _enable_pin = enable;
#   
#   _data_pins[0] = d0;
#   _data_pins[1] = d1;
#   _data_pins[2] = d2;
#   _data_pins[3] = d3; 
#   _data_pins[4] = d4;
#   _data_pins[5] = d5;
#   _data_pins[6] = d6;
#   _data_pins[7] = d7; 
# 
#   _i2cAddr = 255;
#   _SPIclock = _SPIdata = _SPIlatch = 255;
# 
#   pinMode(_rs_pin, OUTPUT);
#   // we can save 1 pin by not using RW. Indicate by passing 255 instead of pin#
#   if (_rw_pin != 255) { 
#     pinMode(_rw_pin, OUTPUT);
#   }
#   pinMode(_enable_pin, OUTPUT);
#   
#   if (fourbitmode)
#     _displayfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS;
#   else 
#     _displayfunction = LCD_8BITMODE | LCD_1LINE | LCD_5x8DOTS;
#   
#   begin(16, 1);  
# }
# 
# void LiquidCrystal::begin(uint8_t cols, uint8_t lines, uint8_t dotsize) {
  def begin( self, cols, lines, dotsize ):
    # check if i2c
    if self._i2cAddr != 255:
        self._i2c.begin( self._i2cAddr )
        self._i2c.pinMode( 1, OUTPUT ) # backlight
        self._i2c.digitalWrite( 1, HIGH )  # backlight

        self._i2c.pinMode( self._rs_pin, OUTPUT )
        self._i2c.pinMode( self._enable_pin, OUTPUT )
    elif _SPIclock != 255:
        self._SPIbuff = 0x80 # backlight

    if lines > 1:
        self._displayfunction |= LCD_2LINE
    self._numlines = lines
    self._currline = 0

    # for some 1 line displays you can select a 10 pixel high font
    if dotsize != 0 and lines == 1:
        _displayfunction |= LCD_5x10DOTS

    #   // SEE PAGE 45/46 FOR INITIALIZATION SPECIFICATION!
    #   // according to datasheet, we need at least 40ms after power rises above 2.7V
    #   // before sending commands. Arduino can turn on way befer 4.5V so we'll wait 50
    delayMicroseconds(50000)
    #   // Now we pull both RS and R/W low to begin commands
    self._digitalWrite( self._rs_pin, LOW )
    self._digitalWrite( self._enable_pin, LOW )
    if self._rw_pin != 255:
        self._digitalWrite( self._rw_pin, LOW )

    #   //put the LCD into 4 bit or 8 bit mode
    if ! ( _displayfunction & LCD_8BITMODE ) ):
#     // this is according to the hitachi HD44780 datasheet
#     // figure 24, pg 46
# 
#     // we start in 8bit mode, try to set 4 bit mode
#     write4bits(0x03);
#     delayMicroseconds(4500); // wait min 4.1ms
# 
#     // second try
#     write4bits(0x03);
#     delayMicroseconds(4500); // wait min 4.1ms
#     
#     // third go!
#     write4bits(0x03); 
#     delayMicroseconds(150);
# 
#     // finally, set to 8-bit interface
#     write4bits(0x02); 
#   } else {
#     // this is according to the hitachi HD44780 datasheet
#     // page 45 figure 23
# 
#     // Send function set command sequence
#     command(LCD_FUNCTIONSET | _displayfunction);
#     delayMicroseconds(4500);  // wait more than 4.1ms
# 
#     // second try
#     command(LCD_FUNCTIONSET | _displayfunction);
#     delayMicroseconds(150);
# 
#     // third go
#     command(LCD_FUNCTIONSET | _displayfunction);
#   }
# 
#   // finally, set # lines, font size, etc.
#   command(LCD_FUNCTIONSET | _displayfunction);  
# 
#   // turn the display on with no cursor or blinking default
#   _displaycontrol = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF;  
#   display();
# 
#   // clear it off
#   clear();
# 
#   // Initialize to default text direction (for romance languages)
#   _displaymode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT;
#   // set the entry mode
#   command(LCD_ENTRYMODESET | _displaymode);
# 
# }
# 
# /********** high level commands, for the user! */
# void LiquidCrystal::clear()
# {
#   command(LCD_CLEARDISPLAY);  // clear display, set cursor position to zero
#   delayMicroseconds(2000);  // this command takes a long time!
# }
# 
# void LiquidCrystal::home()
# {
#   command(LCD_RETURNHOME);  // set cursor position to zero
#   delayMicroseconds(2000);  // this command takes a long time!
# }
# 
# void LiquidCrystal::setCursor(uint8_t col, uint8_t row)
# {
#   int row_offsets[] = { 0x00, 0x40, 0x14, 0x54 };
#   if ( row > _numlines ) {
#     row = _numlines-1;    // we count rows starting w/0
#   }
#   
#   command(LCD_SETDDRAMADDR | (col + row_offsets[row]));
# }
# 
# // Turn the display on/off (quickly)
# void LiquidCrystal::noDisplay() {
#   _displaycontrol &= ~LCD_DISPLAYON;
#   command(LCD_DISPLAYCONTROL | _displaycontrol);
# }
# void LiquidCrystal::display() {
#   _displaycontrol |= LCD_DISPLAYON;
#   command(LCD_DISPLAYCONTROL | _displaycontrol);
# }
# 
# // Turns the underline cursor on/off
# void LiquidCrystal::noCursor() {
#   _displaycontrol &= ~LCD_CURSORON;
#   command(LCD_DISPLAYCONTROL | _displaycontrol);
# }
# void LiquidCrystal::cursor() {
#   _displaycontrol |= LCD_CURSORON;
#   command(LCD_DISPLAYCONTROL | _displaycontrol);
# }
# 
# // Turn on and off the blinking cursor
# void LiquidCrystal::noBlink() {
#   _displaycontrol &= ~LCD_BLINKON;
#   command(LCD_DISPLAYCONTROL | _displaycontrol);
# }
# void LiquidCrystal::blink() {
#   _displaycontrol |= LCD_BLINKON;
#   command(LCD_DISPLAYCONTROL | _displaycontrol);
# }
# 
# // These commands scroll the display without changing the RAM
# void LiquidCrystal::scrollDisplayLeft(void) {
#   command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT);
# }
# void LiquidCrystal::scrollDisplayRight(void) {
#   command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT);
# }
# 
# // This is for text that flows Left to Right
# void LiquidCrystal::leftToRight(void) {
#   _displaymode |= LCD_ENTRYLEFT;
#   command(LCD_ENTRYMODESET | _displaymode);
# }
# 
# // This is for text that flows Right to Left
# void LiquidCrystal::rightToLeft(void) {
#   _displaymode &= ~LCD_ENTRYLEFT;
#   command(LCD_ENTRYMODESET | _displaymode);
# }
# 
# // This will 'right justify' text from the cursor
# void LiquidCrystal::autoscroll(void) {
#   _displaymode |= LCD_ENTRYSHIFTINCREMENT;
#   command(LCD_ENTRYMODESET | _displaymode);
# }
# 
# // This will 'left justify' text from the cursor
# void LiquidCrystal::noAutoscroll(void) {
#   _displaymode &= ~LCD_ENTRYSHIFTINCREMENT;
#   command(LCD_ENTRYMODESET | _displaymode);
# }
# 
# // Allows us to fill the first 8 CGRAM locations
# // with custom characters
# void LiquidCrystal::createChar(uint8_t location, uint8_t charmap[]) {
#   location &= 0x7; // we only have 8 locations 0-7
#   command(LCD_SETCGRAMADDR | (location << 3));
#   for (int i=0; i<8; i++) {
#     write(charmap[i]);
#   }
# }
# 
# /*********** mid level commands, for sending data/cmds */
# 
# inline void LiquidCrystal::command(uint8_t value) {
#   send(value, LOW);
# }
# 
# inline size_t LiquidCrystal::write(uint8_t value) {
#   send(value, HIGH);
#   return 1;
# }
# 
# /************ low level data pushing commands **********/
# 
# // little wrapper for i/o writes
# void  LiquidCrystal::_digitalWrite(uint8_t p, uint8_t d) {
#   if (_i2cAddr != 255) {
#     // an i2c command
#     _i2c.digitalWrite(p, d);
#   } else if (_SPIclock != 255) {
#     if (d == HIGH)
#       _SPIbuff |= (1 << p);
#     else 
#       _SPIbuff &= ~(1 << p);
# 
#     digitalWrite(_SPIlatch, LOW);
#     shiftOut(_SPIdata, _SPIclock, MSBFIRST,_SPIbuff);
#     digitalWrite(_SPIlatch, HIGH);
#   } else {
#     // straightup IO
#     digitalWrite(p, d);
#   }
# }
# 
# // Allows to set the backlight, if the LCD backpack is used
# void LiquidCrystal::setBacklight(uint8_t status) {
#   // check if i2c or SPI
#   if ((_i2cAddr != 255) || (_SPIclock != 255)) {
#     _digitalWrite(1, status); // backlight is on pin 7
#   }
# }
# 
# // little wrapper for i/o directions
# void  LiquidCrystal::_pinMode(uint8_t p, uint8_t d) {
#   if (_i2cAddr != 255) {
#     // an i2c command
#     _i2c.pinMode(p, d);
#   } else if (_SPIclock != 255) {
#     // nothing!
#   } else {
#     // straightup IO
#     pinMode(p, d);
#   }
# }
# 
# // write either command or data, with automatic 4/8-bit selection
# void LiquidCrystal::send(uint8_t value, uint8_t mode) {
#   _digitalWrite(_rs_pin, mode);
# 
#   // if there is a RW pin indicated, set it low to Write
#   if (_rw_pin != 255) { 
#     _digitalWrite(_rw_pin, LOW);
#   }
#   
#   if (_displayfunction & LCD_8BITMODE) {
#     write8bits(value); 
#   } else {
#     write4bits(value>>4);
#     write4bits(value);
#   }
# }
# 
# void LiquidCrystal::pulseEnable(void) {
#   _digitalWrite(_enable_pin, LOW);
#   delayMicroseconds(1);    
#   _digitalWrite(_enable_pin, HIGH);
#   delayMicroseconds(1);    // enable pulse must be >450ns
#   _digitalWrite(_enable_pin, LOW);
#   delayMicroseconds(100);   // commands need > 37us to settle
# }
# 
# void LiquidCrystal::write4bits(uint8_t value) {
#   for (int i = 0; i < 4; i++) {
#     _pinMode(_data_pins[i], OUTPUT);
#     _digitalWrite(_data_pins[i], (value >> i) & 0x01);
#   }
# 
#   pulseEnable();
# }
# 
# void LiquidCrystal::write8bits(uint8_t value) {
#   for (int i = 0; i < 8; i++) {
#     _pinMode(_data_pins[i], OUTPUT);
#     _digitalWrite(_data_pins[i], (value >> i) & 0x01);
#   }
#   
#   pulseEnable();
# }
#

