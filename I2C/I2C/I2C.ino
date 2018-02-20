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
std::vector<int> collector;

void receiveData(int byteCount) 
{
	int i = 0;
	int number;
	while (Wire.available()) 
	{
		collector.push_back(Wire.read());
	}
	Serial.print("\t");
	number = collector[i];
	collector.clear();
	Serial.print(number);
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