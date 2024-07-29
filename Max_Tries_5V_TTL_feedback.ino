int state = 0;

const int TTLPin=12; //the Pin where the TTL trigger enters (default at low)

void setup() {
  Serial.begin(115200); 
	Serial.setTimeout(10);
 	Serial.println("MK CNC Shield Initialized");
}

////Interrupt doesnt work somehow. Also not with "sei();" in setup()
//void TTLregisterer() {
//  Serial.println("1");
//}

void loop() {
  while (true){
    int thisstate = digitalRead(12);
    if (thisstate != state && thisstate == 1){
      Serial.println("enable");
      state = thisstate;
    }else if(thisstate != state && thisstate == 0){
      Serial.println("disable");
      state = thisstate;
    }
    delay(100);
  }
}




