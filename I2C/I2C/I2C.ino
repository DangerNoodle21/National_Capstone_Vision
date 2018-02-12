/*
 Name:		I2C.ino
 Created:	1/31/2018 8:48:24 PM
 Author:	marcd
*/


#include <Wire.h>

#define i2c_ADDRESS 0x04

char input_numbers[1000];

void receiveData(int byteCount) {
	int i = 0;
	while (Wire.available()) {
		input_numbers[i] = Wire.read();
		i++;
	}
	input_numbers[i] = '\0';
	Serial.print(input_numbers);
}  // end while


void setup()
{
	pinMode(LED_BUILTIN, OUTPUT);


	Serial.begin(9600);
	Wire.begin(i2c_ADDRESS);

	Wire.onReceive(receiveData);


void loop()
{
}