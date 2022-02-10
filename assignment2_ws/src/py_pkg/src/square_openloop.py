#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897
 
def drive():
 	rospy.init_node('square_node',anonymous=True)
 	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
 	velocity = Twist()
 	
 	#Drawing square by user
 	#print("Drive turtle in square")
 	speed = float(input("Input desired speed of the turtle: "))
 	distance = float(input("Input desired distance of the turtle: "))
 	ForwardCheck = float(input("Enter 1 for forward and 0 for not : "))
 	speed_ang= float(input("Input desired angular speed of the turtle: "))
 	angle = float(input("Input desired rotation degrees: "))
 	Clockwisecheck = float(input("Enter 1 for clockwise 0 for not: "))
 	
 	#Defining angular velocity of the turtle
 	ang_speed_turtle = speed_ang*2*PI/360
 	
 	#Defining angle of the turtle
 	turtle_angle = angle*2*PI/360
 	
 	#considering initial velocity zero except x linear 		
 	velocity.linear.y = 0
 	velocity.linear.z = 0
 	velocity.angular.x = 0
 	velocity.angular.y = 0
 	velocity.angular.z = 0
 	i=0
 	
 	while (i<4):
 	
 #code to move in the straight line
 
 		time0 = rospy.Time.now().to_sec()
 		distance_now = 0
 		
 		while(distance_now<distance):
 			if(ForwardCheck):
 				velocity.linear.x = abs(speed)
 			else:
 				velocity.linear.x = -abs(speed)
 				
 			velocity_publisher.publish(velocity)
 			time1 = rospy.Time.now().to_sec()
 			distance_now = speed*(time1-time0)
 		velocity.linear.x = 0
 		velocity_publisher.publish(velocity)
 
 #Code for rotation
  	
 		if(Clockwisecheck):
 			velocity.angular.z = -abs(ang_speed_turtle)
 		else:
 			velocity.angular.z = abs(ang_speed_turtle)
 			
 		
 		time2 = rospy.Time.now().to_sec()
 		angle_now = 0 
 	
 		while(angle_now<turtle_angle):
 			velocity_publisher.publish(velocity)
 			time3 = rospy.Time.now().to_sec()
 			angle_now = ang_speed_turtle *(time3-time2)
 	
 		velocity.angular.z = 0
 		velocity_publisher.publish(velocity)
 		#rospy.sleep(1)
 		#rospy.spin()
 		i=i+1
 	
if __name__ == '__main__':
 	try:
 		drive()
 	except rospy.ROSInterruptException: pass
 
