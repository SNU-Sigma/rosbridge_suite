import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
from rosbridge_client.client import RosbridgeClient
from rospy_message_converter import message_converter


handle_publisher = rospy.Publisher("/handle", Float32, queue_size=10)
motor_speed_publisher = rospy.Publisher("/motor/speed", Float32, queue_size=10)


def joystick_callback(msg):
    speed_msg = Float32(data=msg.axes[0])
    handle_msg = Float32(data=msg.axes[1])
    motor_speed_publisher.publish(speed_msg)
    handle_publisher.publish(handle_msg)


if __name__ == "__main__":
    rospy.init_node("joystick_subscriber")

    ros_server = RosbridgeClient()
    ros_server.connect("147.46.242.59")
    ros_server.subscribe("sensor_msgs/Joy",
                         "/lotteria2/joystick",
                         joystick_callback)
