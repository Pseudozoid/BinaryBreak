void setup() {
  Serial.begin(9600);
  pinMode(BUILTIN_LED, OUTPUT);

}

void loop() {
  
  if(Serial.available()){
    String msg = Serial.readString();

    if(msg == "ON"){
      digitalWrite(BUILTIN_LED,LOW);
      Serial.write("ANte ole Wapa\n");
    }else{
      digitalWrite(BUILTIN_LED,HIGH);
    }
  }

}

