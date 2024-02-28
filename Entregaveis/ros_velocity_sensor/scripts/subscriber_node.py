#!/usr/bin/env python

import rospy
from sensor_velocity_publisher.msg import Velocity
from math import sqrt

def callback(data):
    linear_vel_mod = sqrt(data.linear_x**2 + data.linear_y**2 + data.linear_z**2)
    angular_vel_mod = sqrt(data.angular_x**2 + data.angular_y**2 + data.angular_z**2)
    rospy.loginfo("Linear Velocity Module: %f", linear_vel_mod)
    rospy.loginfo("Angular Velocity Module: %f", angular_vel_mod)

def subscriber():
    rospy.init_node('velocity_subscriber', anonymous=True)
    rospy.Subscriber('velocity', Velocity, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
