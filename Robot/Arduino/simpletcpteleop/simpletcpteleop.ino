#include <FRCmotor.h>
int gamemode = 1;

FRCmotor LeftDriveMotor;
FRCmotor RightDriveMotor;

int leftspeed = 0;
int rightspeed = 0;
  
void setup() {
  Serial.begin(9600);
  LeftDriveMotor.SetPort(3); //port 3,5,6,9,10,11 on uno
  LeftDriveMotor.SetPort(5);
  pinMode(13, OUTPUT);
  digitalWrite(13, INPUT);
  

}

void loop(){
  while (!Serial.available()) {};
  char startlabel = Serial.read();
  if (startlabel == '#') {
    digitalWrite(13, HIGH);
    while (!Serial.available()) {};
    leftspeed = Serial.read() * 200 / 256 - 100;
    Serial.println("got left");
    Serial.println(leftspeed);
    while (!Serial.available()) {};
    rightspeed = Serial.read() * 200 / 256 - 100;
    Serial.println("got right");
    Serial.println(rightspeed);
    Serial.println();
  }
  
  LeftDriveMotor.Set(leftspeed);
  RightDriveMotor.Set(rightspeed);
}
