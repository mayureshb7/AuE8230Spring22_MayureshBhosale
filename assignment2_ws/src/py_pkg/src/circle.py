#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys

def circle(Radius):
	rospy.init_node('New_node_turtle', anonymous =True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

	rate = rospy.Rate(10)

	velocity = Twist()

	while True:
		velocity.linear.x = Radius
		velocity.linear.y = 0
		velocity.linear.z = 0
		
		velocity.angular.x = 0
		velocity.angular.y = 0
		velocity.angular.z = Radius
		
		rospy.loginfo("Radius of the circle = %f", Radius)

		pub.publish(velocity)
		rate.sleep()
		
circle(4)
