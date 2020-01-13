#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import String


"""
Called by listener() when ma message is received.
Publishes to the perceptions topic
"""
def callback(data):
    pub = rospy.Publisher('perceptions', String, queue_size=10)
    message = "accelerometer({},{},{})".format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z)
    rospy.loginfo(message)
    pub.publish(message)


"""
Listen for IMU data from "/mavros/imu/data"
"""
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/mavros/imu/data", Imu, callback)
    rospy.spin()


"""
Main method, calls listner()
"""
if __name__ == '__main__':
    listener()