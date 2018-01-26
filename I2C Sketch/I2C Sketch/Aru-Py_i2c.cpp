#include <Wire.h>
//#define address 50


long distance;

int trigpin = 10;
int echopin = 9;
int led = 7; //light 
int rled = 5;

void setup() {
	// put your setup code here, to run once:
	Serial.begin(9600);
	pinMode(led, OUTPUT);
	pinMode(rled, OUTPUT);
	pinMode(trigpin, OUTPUT);
	pinMode(echopin, INPUT);

	Wire.begin(84);

	//   Wire.onReceive(receiveEvent);
}

void loop() {
	// put your main code here, to run repeatedly:
	long duration;
	digitalWrite(trigpin, HIGH);
	delayMicroseconds(1000);
	digitalWrite(trigpin, LOW);
	duration = pulseIn(echopin, HIGH);
	distance = (duration / 2) / 29.1;
	Serial.print(distance);
	//Wire.write(distance);
	Serial.println("CM");


	if (distance <= 20 && distance >5)
	{
		digitalWrite(led, HIGH);
		digitalWrite(rled, LOW);
	}
	else if (distance > 20)
	{
		digitalWrite(led, LOW);
		digitalWrite(rled, LOW);
	}
	else if (distance < 5)
	{
		digitalWrite(led, LOW);
		digitalWrite(rled, HIGH);
	}
	Wire.onRequest(sendData);
	delay(100);

}

void sendData()
{
	Wire.write(distance);
}

void requestEvent() {
	/*long duration, distance;
	digitalWrite(trigpin,HIGH);
	delayMicroseconds(1000);
	digitalWrite(trigpin,LOW);
	duration = pulseIn(echopin,HIGH);
	distance = (duration /2) / 29.1;
	Serial.print(distance);
	//Wire.write(distance);
	Serial.println("CM");


	if (distance <= 20 && distance >5)
	{
	digitalWrite(led,HIGH);
	digitalWrite(rled,LOW);
	}
	else if (distance > 20)
	{
	digitalWrite(led,LOW);
	digitalWrite(rled,LOW);
	}
	else if(distance < 5)
	{
	digitalWrite(led,LOW);
	digitalWrite(rled,HIGH);
	}
	Wire.write(distance); // respond with message of 6 bytes
	// as expected by master*/
	Wire.write("Hello");
	// Wire.write(distance); 
}

/*void receiveEvent(int howMany)
{
while(Wire.available())
{
char c =Wire.read();
if(c == 72) digitalWrite(13,HIGH);
else if(c == 76) digitalWrite(13,LOW);
}
/* String LED = "";

while ( Wire.available() > 0 )
{
char n=(char)Wire.read();
if(((int)n)>((int)(' ')))
LED += n;
}

if (LED == "go")
{
digitalWrite (13, HIGH);
}
}*/