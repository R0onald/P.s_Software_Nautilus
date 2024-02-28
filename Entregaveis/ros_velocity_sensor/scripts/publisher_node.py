#!/usr/bin/env python

import rospy
from sensor_velocity_publisher.msg import Velocity
from random import uniform

def publisher():
    rospy.init_node('velocity_publisher', anonymous=True)
    pub = rospy.Publisher('velocity', Velocity, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        vel_msg = Velocity()
        vel_msg.linear_x = uniform(0, 10)
        vel_msg.linear_y = uniform(0, 10)
        vel_msg.linear_z = uniform(0, 10)
        vel_msg.angular_x = uniform(0, 5)
        vel_msg.angular_y = uniform(0, 5)
        vel_msg.angular_z = uniform(0, 5)
        rospy.loginfo(vel_msg)
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
