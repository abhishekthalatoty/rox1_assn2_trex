# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Int32


class TREXPublisher(Node):
    
    def __init__(self):
        super().__init__('trex_publisher')

        self.fl_count = 0
        self.fr_count = 0
        self.bl_count = 0
        self.br_count = 0

        self.run_count = 0
        
        self.fl_publisher_ = self.create_publisher(Int32, 'fl_count', 10)
        self.fr_publisher_ = self.create_publisher(Int32, 'fr_count', 10)
        self.bl_publisher_ = self.create_publisher(Int32, 'bl_count', 10)
        self.br_publisher_ = self.create_publisher(Int32, 'br_count', 10)
        
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = String()
        msg = Int32()
        if(self.run_count %4 == 0):
            msg.data = self.fl_count
            self.fl_count+=1
            self.fl_publisher_.publish(msg)
        elif(self.run_count %4 == 1 ):
            msg.data = self.fr_count
            self.fr_publisher_.publish(msg)
            self.fr_count+=1
        elif(self.run_count %4 == 2 ):
            msg.data = self.bl_count
            self.bl_publisher_.publish(msg)
            self.bl_count+=1 
        elif(self.run_count %4 == 3 ):
            msg.data = self.br_count
            self.br_publisher_.publish(msg)
            self.br_count+=1 

        self.fl_publisher_.publish(msg)
        self.get_logger().info('Publishing: "%i"' % msg.data)
        self.get_logger().info('Run Count: "%i"' % self.run_count)
        self.run_count+=1




def main(args=None):
    rclpy.init(args=args)

    trex_pub_node = TREXPublisher()
    rclpy.spin(trex_pub_node)

    trex_pub_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()