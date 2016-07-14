import rospy
from rosbridge_client.client import RosbridgeClient
from sensor_msgs.msg import CompressedImage
from rospy_message_converter import *


def camImageCallback(msg):
    p.publish(msg)


rospy.init_node("cameraSubscribe")
p = rospy.Publisher("/remote_cam/compressed", CompressedImage, queue_size=100)
ros_server = RosbridgeClient()
ros_server.connect("ineedcaffeine.xyz")

ros_server.subscribe("sensor_msgs/CompressedImage", "/remote_cam/compressed", camImageCallback)
