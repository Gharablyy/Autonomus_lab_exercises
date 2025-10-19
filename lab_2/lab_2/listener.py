import rclpy
from rclpy.node import Node 
from std_msgs.msg import String
from lab_2_msgs.msg import Num


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        #self.subscriber= self.create_subscription(String,'/published_topic',self.callback,10)
        self.subscriber= self.create_subscription(Num,'/published_topic',self.callback,10)
        self.subscriber  # prevent unused variable warning

    def callback(self,msg):
        self.get_logger().info('I heard, count is : "%s"' % msg.num)

def main(args=None):
    rclpy.init(args=args)
    
    listener_node = Listener()
    rclpy.spin(listener_node)
    listener_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()