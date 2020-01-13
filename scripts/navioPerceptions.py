#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import String


"""
Called by listener() when ma message is received.
"""
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nlinear acceleration:\nx: [{}]\ny: [{}]\nz: [{}]"
    .format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z))
    
    # Publish to the perceptions topic
    pub = rospy.Publisher('perceptions', String, queue_size=10)
    rospy.init_node('navioPerceptionsTalker', anonymous=True)
    message = "accelerometer({},{},{})".format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z)
    rospy.loginfo(message)
    pub.publish(message)


"""
Publish to the 'perceptions' topic
@param  x   Accelerometer value in x dinmension
@param  y   Accelerometer value in y dinmension
@param  z   Accelerometer value in z dinmension
"""
def sendPerception(x, y, z):
    pub = rospy.Publisher('perceptions', String, queue_size=10)
    rospy.init_node('navioPerceptionsTalker', anonymous=True)
    message = "accelerometer({},{},{})".format(x,y,z)
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