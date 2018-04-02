#define MOTOR 5 // pin 1 chip
#define DIRA 3 // pin 7 chip
#define DIRB 4 // pin 2 chip
#define MOTOR2 10 // pin 10 chip
#define DIRC 8 // pin 15 chip
#define DIRD 9 // pin 9 chip
 // pins 4, 5, 12, 13 GND
 // pins 8 y 16 to 5V
 // pin 3 left motor
 // pin 6 left motor
 // pin 11 right motor
 // pin 14 right motor

enum state_t { stateStopped, stateRunning };
state_t state;
unsigned long startTime;
int i;
int incomingByte;
 
void setup() {
  //---set pin direction
  pinMode(MOTOR,OUTPUT);
  pinMode(MOTOR2, OUTPUT);
  pinMode(DIRA,OUTPUT);
  pinMode(DIRC, OUTPUT);
  pinMode(DIRB,OUTPUT);
  pinMode(DIRD, OUTPUT);
  Serial.begin(9600);
  state = stateStopped;
  startTime = millis();
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    
    Serial.print(incomingByte);
    Serial.println("Received, going forward");
    
    digitalWrite(MOTOR,HIGH);
    digitalWrite(MOTOR2, HIGH);
    digitalWrite(DIRA,LOW); //forward
    digitalWrite(DIRC, LOW);
    digitalWrite(DIRB,HIGH);
    digitalWrite(DIRD, HIGH);
    delay(100);
    digitalWrite(MOTOR,LOW);
    digitalWrite(MOTOR2, LOW);
    }
    
}
