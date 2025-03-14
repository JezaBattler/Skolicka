#include "funshield.h"
long start = millis();
constexpr int interval = 300;
int ledky[4] = {led1_pin, led2_pin, led3_pin, led4_pin};
constexpr int ledky_count = sizeof(ledky) / sizeof(ledky[0]);
int pos = 0;
bool direction = true;

void setup() {
  pinMode(led1_pin, OUTPUT);
  pinMode(led2_pin, OUTPUT);
  pinMode(led3_pin, OUTPUT);
  pinMode(led4_pin, OUTPUT);
  digitalWrite(led2_pin, HIGH);
  digitalWrite(led3_pin, HIGH);
  digitalWrite(led4_pin, HIGH);

}
void changeLed(){
  digitalWrite(ledky[pos], OFF);
  if(direction){
    pos++;
  }
  else{
    pos--;
  }
  pos = (pos) % ledky_count;
  digitalWrite(ledky[pos], ON);
}
void checkDirection(){
  if(pos == ledky_count - 1 || pos == 0){
    direction = !direction;
  }
}
void loop() {

  if(millis()-start > interval){
    changeLed();
    checkDirection();
    start = millis();
  }

  

}

