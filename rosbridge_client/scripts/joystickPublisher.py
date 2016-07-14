import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import Joy
from rosbridge_client.client import RosbridgeClient
from rospy_message_converter import message_converter

motor_speed_pub = rospy.Publisher("/motor/speed", Float32, queue_size=10)
handle_pub = rospy.Publisher("/handle", Float32, queue_size=10)


def joystick_callback(msg):
    ros_server.publish("lotteria2/joystick",
                       message_converter.convert_ros_message_to_dictionary(msg)
                       )



if __name__ == '__main__':
    rospy.init_node("server_to_joystick")

    ros_server = RosbridgeClient()
    ros_server.connect("ineedcaffeine.xyz")

    ros_server.advertise("sensor_msgs/Joy", "lotteria2/joystick")
    joystick_sub = rospy.Subscriber("/joystick", Joy, joystick_callback)

    rospy.spin()
