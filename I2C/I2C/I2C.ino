/*
 Name:		I2C.ino
 Created:	1/31/2018 8:48:24 PM
 Author:	marcd
*/

#include <StandardCplusplus.h>
#include <vector>
#include <iterator>


#include <Wire.h>




#define i2c_ADDRESS 0x04


char holder[10];

void receiveData(int byteCount) 
{
	int i = 0;
	while (Wire.available()) 
	{
		holder[i] = Wire.read();
		i++;
	}
	holder[i] = ('\0');
	Serial.print(holder);
}  // end while


void setup()
{


	Serial.begin(9600);
	Wire.begin(i2c_ADDRESS);

	Wire.onReceive(receiveData);

}
void loop()
{
	delay(100);
}