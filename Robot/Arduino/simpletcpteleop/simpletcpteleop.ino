#include <FRCmotor.h>
int gamemode = 1;

FRCmotor LeftDriveMotor;
FRCmotor RightDriveMotor;
  
void setup() {
  Serial.begin(9600);
  LeftDriveMotor.SetPort(5); //port 3,5,6,9,10,11 on uno
  RightDriveMotor.SetPort(9);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  

}

void loop(){
  int leftspeed = 0;
  int rightspeed = 0;
  while (!Serial.available()) {};
  char startlabel = Serial.read();
  if (startlabel == '#') {
    digitalWrite(13, HIGH);
    while (!Serial.available()) {};
    char l = Serial.read();
    leftspeed = l * 200 / 127 - 100;
    //Serial.print("  got left " );
    Serial.print(leftspeed);
     while (!Serial.available()) {};
    char r = Serial.read();
    rightspeed = r * 200 / 127 - 100;
    //Serial.print("  got right ");
    //Serial.println(rightspeed);
    while(Serial.available()){Serial.read();}
  }
  LeftDriveMotor.Set(leftspeed);
  RightDriveMotor.Set(rightspeed);
}
