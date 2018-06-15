#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

#Standard code from MAX31855 library

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

#imports gspread oauth, enables google drive API
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet  Make sure you use the right name here.
#sheet = client.open("temp_data").sheet1


# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0


# Uncomment one of the blocks of code below to configure your Pi or BBB to use
# software or hardware SPI.

# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 24
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)

# Raspberry Pi hardware SPI configuration.
#SPI_PORT   = 0
#SPI_DEVICE = 0
#sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# BeagleBone Black software SPI configuration.
#CLK = 'P9_12'
#CS  = 'P9_15'
#DO  = 'P9_23'
#sensor = MAX31855.MAX31855(CLK, CS, DO)

# BeagleBone Black hardware SPI configuration.
#SPI_PORT   = 1
#SPI_DEVICE = 0
#sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Loop printing measurements every second.
#print('Press Ctrl-C to quit.')
#temp_file = open('temps.csv', 'a')

#while True:
#    temp = sensor.readTempC()
#    internal = sensor.readInternalC()
#    print('Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp)))
#    print('Internal Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal, c_to_f(internal)))



#    temp_recorded = str(c_to_f(temp)) + ','
#    temp_file.write(temp_recorded)

#    time.sleep(1.0)

spreadsheet = client.open("temp_data")

food  = input("What are you cooking?")
date = input("What is today?")

minutes = 0

newsheet = food + date
cur_sheet = spreadsheet.add_worksheet(newsheet,1,3)

rows = 0
row = ["Celsius","Farenheit","Intervals"]
#print(newsheet)
#print(now)

#sheet = client.open("temp_data").cur_sheet

readings = 0

while True:
    rows += 1
    cur_sheet.insert_row(row,rows)
    readings += 1
    temp_Celsius = sensor.readTempC()
    temp_Farenheit = c_to_f(temp_Celsius)
#    internal = sensor.readInternalC()
#    print('Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp)))
#    print('Internal Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal, c_to_f(internal)))
    row = [temp_Celsius,temp_Farenheit,readings]
    time.sleep(1.0)
