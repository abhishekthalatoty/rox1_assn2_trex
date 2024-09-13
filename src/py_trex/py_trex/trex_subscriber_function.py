import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32



class TREXSubscriber(Node):

    def __init__(self):
        super().__init__('trex_subscriber')
        self.fl_subscriber = self.create_subscription(Int32, 'fl_count', self.fl_listener_callback, 10) 
        self.fr_subscriber = self.create_subscription(Int32, 'fr_count', self.fr_listener_callback, 10) 
        self.bl_subscriber = self.create_subscription(Int32, 'bl_count', self.bl_listener_callback, 10) 
        self.br_subscriber = self.create_subscription(Int32, 'br_count', self.br_listener_callback, 10) 

    
    def fl_listener_callback(self, msg):
        self.get_logger().info('FL : "%i"' % msg.data)
    
    def fr_listener_callback(self, msg):
        self.get_logger().info('FR : "%i"' % msg.data)

    def bl_listener_callback(self, msg):
        self.get_logger().info('BL : "%i"' % msg.data)

    def br_listener_callback(self, msg):
        self.get_logger().info('BR : "%i"' % msg.data)
    



def main(args=None):
    rclpy.init(args=args)

    trex_subsriber = TREXSubscriber()
    rclpy.spin(trex_subsriber)
    trex_subsriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()