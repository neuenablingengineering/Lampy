/* This is the main code for Lampy using the Blend Micro
 * 
 * Capstone GW3 2018
 */
/*

Copyright (c) 2012-2014 RedBearLab

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

*/

/*
 *    HelloWorld
 *
 *    HelloWorld sketch, work with the Chat iOS/Android App.
 *    It will send "Hello World" string to the App every 1 sec.
 *
 */

//"SPI.h/Nordic_nRF8001.h/RBL_nRF8001.h" are needed in every new project
#include <SPI.h>
#include <Nordic_nRF8001.h>
#include <RBL_nRF8001.h>

#define Pin_PWR          A0
#define Pin_BLE_LED      A9
#define Pin_ON_LED       A10
#define Pin_LO_while_ON      A1


void setup()
{
  //  
  // For BLE Shield or Blend:
  //   Default pins set to 9 and 8 for REQN and RDYN
  //   Set your REQN and RDYN here before ble_begin() if you need
  //
  // For Blend Micro:
  //   Default pins set to 6 and 7 for REQN and RDYN
  //   So, no need to set for Blend Micro.
  //
  //ble_set_pins(3, 2);
  
  // Set your BLE advertising name here, max. length 10
  //ble_set_name("My BLE");
  
  // Init. and start BLE library.
  ble_begin();
  
  // Enable serial debug
  Serial.begin(57600);
  
  pinMode(Pin_ON_LED, OUTPUT);
  pinMode(Pin_BLE_LED, OUTPUT);
  pinMode(Pin_PWR, OUTPUT);
  pinMode(Pin_LO_while_ON, OUTPUT);
  //delay(1000);
  digitalWrite(Pin_LO_while_ON, LOW);
    
  // set LED that is always on
  digitalWrite(Pin_ON_LED, HIGH);
  // set pin which prevents mat from triggering power off
  // set power pin to high by default
  digitalWrite(Pin_PWR, HIGH);
  
}

unsigned char buf[16] = {0};
unsigned char len = 0;
unsigned int count = 0;

void loop()
{
  if ( ble_connected() )
  {  
    //digitalWrite(BLE_LED, HIGH);

    ble_write('L');
    ble_write('a');
    ble_write('m');
    ble_write('p');
    ble_write('y');
    ble_write(' ');
    ble_write('C');
    ble_write('o');
    ble_write('m');
    ble_write('p');
    ble_write('a');
    ble_write('n');
    ble_write('i');
    ble_write('o');
    ble_write('n');
    ble_write(' ');
    ble_write('M');
    ble_write('a');
    ble_write('t');
  }
  else
  {
    //digitalWrite(BLE_LED, LOW);
  }

  ble_do_events();
  
  if ( ble_available() )
  {
    while ( ble_available() )
    {
      Serial.write(ble_read());
    }
    
    Serial.println();
  }
  
  // wait time
  //delay(3000);
  
  //flicker a few times
  /*digitalWrite(BLE_LED, HIGH);
  delay(500);
  digitalWrite(BLE_LED, LOW);
  delay(500);
  digitalWrite(BLE_LED, HIGH);
  delay(500);
  digitalWrite(BLE_LED, LOW);
  delay(500);
  digitalWrite(BLE_LED, HIGH);
  delay(500);
  digitalWrite(BLE_LED, LOW);
  delay(500); */
  

  
  
  // Blink LED to signal BLE activity
  delay(1000);
  digitalWrite(Pin_BLE_LED, HIGH);
  delay(100);
  digitalWrite(Pin_BLE_LED, LOW);

  
  
  // Cut off power by setting pin low
  if(count == 10)
  {
    digitalWrite(Pin_PWR, LOW);
  }
  
  count++;
  
  
  //digitalWrite(BLE_LED, LOW);
  //delay(1000);  
  //digitalWrite(BLE_LED, HIGH);
  //delay(1000);
}
