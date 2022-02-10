Following a circular path by a turtlebot in turtlesim is based on the parameters defined for the linear and angular velocities.
Code is written by initiating a node and publishing respective velocity. the Twist() function is used to access the linear and angular velocities in x,y and z direction.
For a turtle to follow a perfect circular path of radius 1 the angular velocity and linear velocity needs to be equal based on v=r*omega formula
Thus a single input variable for angular and linear velocity works to generate a circular path of radius of 1
rate.sleep() command is used further to keep running the turtle in infinite loop
