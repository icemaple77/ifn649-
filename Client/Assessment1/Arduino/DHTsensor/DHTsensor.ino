#include "DHT.h"
//#include <SoftwareSerial.h>

#define DHTPIN 21      // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11

#define LEDPIN 11

DHT dht(DHTPIN, DHTTYPE);

// Teensy 5V <--> HC-05 Vcc
// Teensy Ground <--> HC-05 GND
#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx
//SoftwareSerial BTSerial =  SoftwareSerial(rxPin, txPin);

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  // Setup DHT Sensor
  pinMode(DHTPIN, INPUT);
  dht.begin();

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() {
  if(Serial1.available() > 0){ // Checks whether data is comming from the serial port
    digitalWrite(LEDPIN, HIGH);
    
    float h = dht.readHumidity();
    delay(1000);
    float t = dht.readTemperature();
    delay(1000);

    Serial.print(F(" *ROOM1201* "));
    Serial.print(F(" Humidity : "));
    Serial.print(h);
    Serial.print(F(" %  Temperature : "));
    Serial.print(t);
    Serial.println(F("C "));

    Serial1.print(F(" *ROOM1201* "));
    Serial1.print(F(" Humidity : "));
    Serial1.print(h);
    
    Serial1.print(F(" %  Temperature : "));
    Serial1.print(t);
    Serial1.println(F(" C "));

    
    delay(1000);
    digitalWrite(LEDPIN, LOW);
    delay(1000);
 }
}
