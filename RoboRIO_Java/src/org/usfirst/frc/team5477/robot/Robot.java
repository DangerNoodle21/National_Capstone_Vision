/*----------------------------------------------------------------------------*/
/* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
/* Open Source Software - may be modified and shared by FRC teams. The code   */
/* must be accompanied by the FIRST BSD license file in the root directory of */
/* the project.                                                               */
/*----------------------------------------------------------------------------*/

package org.usfirst.frc.team5477.robot;

import edu.wpi.first.wpilibj.CameraServer;
import edu.wpi.cscore.UsbCamera;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;





public class Robot extends IterativeRobot()
{
	
	public void operatorControl()
	{
		double counter = 0.0;
		while(isOperatorControl() && isEnabled())
		{
			SmartDashboard.putNumber("Counter", counter++);
			Timer.delay(0.10);
		}
	
}


	public void robotInit() {
		
	
		CameraServer.getInstance().startAutomaticCapture();
		UsbCamera.enumerateUsbCameras();
		operatorControl();
		
		
	}

}
