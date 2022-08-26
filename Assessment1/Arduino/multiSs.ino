// Defining frequency of each music note
#include "piches.h"
#include "DHT.h"
#define DHTPIN 21      // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
const int led = LED_BUILTIN;
const int ledRed=1;
const int ledYellow=2;
const int ledGreen=3;
const int speaker=4;
const int ledPin = 11;
const int soilpin=20;
const float songSpeed = 1.0;

int melody[] = {
  NOTE_C4, NOTE_C4, NOTE_D4, NOTE_C4, NOTE_F4, NOTE_E4, NOTE_C4, NOTE_C4, NOTE_D4, NOTE_C4, NOTE_G4, NOTE_F4, NOTE_C4, NOTE_C4, NOTE_C5, NOTE_A4, NOTE_F4, NOTE_E4, NOTE_D4, NOTE_AS4, NOTE_AS4, NOTE_A4, NOTE_F4, NOTE_G4, NOTE_F4
};
int buttonPin =12;

//note durations: 4 = quarter note, 8 = eight note, etc.
int noteDurations[] = {
  8, 8, 4, 4, 4, 2, 8, 8, 4, 4, 4, 2, 8, 8, 4, 4, 4, 4, 4, 8, 8, 4, 4, 4, 2, 
};


int arrivingdatabyte; 
void setup() {
  Serial.begin(9600);
  Serial1.begin(9600); // Default communication rate of the Bluetooth module
  pinMode(led, OUTPUT);
  pinMode(ledRed,OUTPUT);
  pinMode(ledYellow,OUTPUT);
  pinMode(ledGreen,OUTPUT);
  pinMode(speaker,OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(DHTPIN, INPUT);
  dht.begin();
}

int songState=1;
int order;
void getOrder(){

  if (Serial.available()>0){
    order=Serial.read();
  if (Serial1.available()>0){
    order=Serial1.read();
    
    }
  }
void loop() {
  powerStatue();
  getOrder();
  switch (order) {
    case 49 :
      DHTSensor();
      delay(1000);
      break;
    case 50:
      THSensor();
      delay(1000);
      break;
    case 51:
      playSongChristmas(1);
      delay(1000);
      break;
    default:
      Serial.println("there is no order for now");
      Serial1.println("there is no order for now");
      delay(1000);
      break;
   }
  powerStatue();
}
void powerStatue(){
  digitalWrite(ledPin, HIGH);   // set the LED on
  delay(1000);                  // wait for a second
  digitalWrite(ledPin, LOW);    // set the LED off
  delay(1000);                  // wait for a second
  }
void turnOnLED(int LEDName){
  digitalWrite(LEDName, HIGH);
  delay(100);
  }
void turnOffLED(int LEDName){
  digitalWrite(LEDName, LOW);
  delay(100);
  }
void blink(int LEDName){
  turnOnLED(LEDName);
  delay(1000);
  turnOffLED(LEDName);
  delay(1000);
  }
void THSensor(){
  int val = analogRead(soilpin);
  Serial.print("soil:");
  Serial.println(val);
  Serial1.print("soil:");
  Serial1.println(val);
  }

void DHTSensor(){
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    float f = dht.readTemperature(true);

    float hif = dht.computeHeatIndex(f, h);
    float hic = dht.computeHeatIndex(t, h, false);  

    Serial.print(F(" Humidity: "));
    Serial.print(h);
    Serial.print(F("%  Temperature: "));
    Serial.print(t);
    Serial.print(F("C "));
    Serial.print(f);
    Serial.print(F("F  Heat index: "));
    Serial.print(hic);
    Serial.print(F("C "));
    Serial.print(hif);
    Serial.println(F("F"));

    Serial1.print(F(" Humidity: "));
    Serial1.print(h);
    Serial1.print(F("%  Temperature: "));
    Serial1.print(t);
    Serial1.print(F("C "));
    Serial1.print(f);
    Serial1.print(F("F  Heat index: "));
    Serial1.print(hic);
    Serial1.print(F("C "));
    Serial1.print(hif);
    Serial1.println(F("F"));
    
    delay(1000);
    digitalWrite(LEDPIN, LOW);
    delay(1000);
  }



























void playSongChristmas(int playState){

if (playState == 1) {

for (int thisNote = 0 ; thisNote < 25 ; thisNote++) { 
    int randomLight1 = random(1, 4);
    int randomLight2 = random(1, 4);
    int randomLight3 = random(1, 4);
     
    delay(100);
    digitalWrite(1, LOW);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    
    digitalWrite (randomLight1, HIGH);
    digitalWrite (randomLight2, HIGH);
    
    digitalWrite (randomLight3, LOW);
    //digitalWrite (random(1, 4), LOW);
    
    
    int noteDuration = 1130/noteDurations[thisNote];
    tone (speaker, melody[thisNote], noteDuration);
    
    int pause = noteDuration * 1.275;
    delay (pause);
    
    noTone(speaker);

    }
}
  
  }