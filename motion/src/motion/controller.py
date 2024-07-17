#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class SpeedControlNode(Node):
    def __init__(self):
        super().__init__('speed_control_node')
        self.publisher = self.create_publisher(Float64, '/wheel_joint/command', 10)
        self.timer = self.create_timer(1.0, self.publish_speed)  # Adjust period as needed

    def publish_speed(self):
        msg = Float64()
        msg.data = 1.0  # Set desired angular velocity here
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    speed_control_node = SpeedControlNode()
    rclpy.spin(speed_control_node)
    speed_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
