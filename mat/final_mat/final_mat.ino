/* This is the main code for Lampy using the Arduino Micro with BT breakout
 * 
 * Capstone GW3 2018
 */
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

// Pin definitions
#define Pin_LO_while_ON  6
#define Pin_ON_LED       7
#define Pin_BLE_LED      8
#define Pin_PWR          9

//#define Pin_HI_while_ON  11
//#define Pin_LO_while_ON_B  8

void setup() {
  // Open Serial
  Serial.begin(9600);
  Serial.println("Enter AT commands:");
  mySerial.begin(38400);
  
  // Initialize pins
  pinMode(Pin_PWR, OUTPUT);
  digitalWrite(Pin_PWR, HIGH);
  pinMode(Pin_LO_while_ON, OUTPUT);
  digitalWrite(Pin_LO_while_ON, LOW);
  pinMode(Pin_ON_LED, OUTPUT);
  digitalWrite(Pin_ON_LED, HIGH);
  pinMode(Pin_BLE_LED, OUTPUT);
  digitalWrite(Pin_BLE_LED, LOW);
  
  //pinMode(Pin_HI_while_ON, OUTPUT);
  //digitalWrite(Pin_LO_while_ON, LOW);
  //digitalWrite(Pin_HI_while_ON, HIGH);
  

}

unsigned char buf[16] = {0};
unsigned char len = 0;
unsigned int count = 0;

void loop() {
  // Serial interface to Bluetooth
  if (mySerial.available())
  Serial.write(mySerial.read());
  if (Serial.available())
  mySerial.write(Serial.read());

  // Blink LED to signal BLE activity
  delay(1000);
  digitalWrite(Pin_BLE_LED, HIGH);
  delay(100);
  digitalWrite(Pin_BLE_LED, LOW);
  
  // BT Advertise 10 times
  // Cut off power by setting pin low
  if(count == 10)
  {
    digitalWrite(Pin_PWR, LOW);
  }
  
  count++;
}
