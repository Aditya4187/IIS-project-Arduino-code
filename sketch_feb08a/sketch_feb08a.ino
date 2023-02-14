int led = 4;
int sensor = A0;
int solenoid = 8;
int threshold = 100;
void setup(){
  pinMode(4,OUTPUT);
  pinMode(A0,INPUT);
  pinMode(8,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  int value = analogRead(sensor);
  if(value>=threshold)
  {
    digitalWrite(4,HIGH);
    digitalWrite(8,LOW);
    delay(1000);
  }
  else
  digitalWrite(4,LOW);
  digitalWrite(8,HIGH);
  delay(100);
}