/*
  I2C Pinouts

  SDA -> A4
  SCL -> A5
*/

//Import the library required
#include <Wire.h>
#define SLAVE_ADDRESS 0x04 //Slave Address for the Communication

char data_number[50]; // Array for collecting number
int state = 0;


// callback for received data
void receiveData(int byteCount) {
  int i = 0;
  while (Wire.available()) {
	  data_number[i] = Wire.read();
    i++;
  }
  data_number[i] = '\0';
  Serial.print(data_number);
}  // end while

// callback for sending data
void sendData() {
  Wire.write(data_number);
}




void setup()
{

  Serial.begin(9600); // Serial Port Baud 9600

  Wire.begin(SLAVE_ADDRESS);// define call backs for i2c communication

  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
}

void loop()
{
  delay(100); // Loop to continouly monitor port
}


