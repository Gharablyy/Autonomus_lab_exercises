import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from lab_2_msgs.msg import Num

class Talker(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(Num, '/published_topic', 10)
        #self.publisher = self.create_publisher(String, '/published_topic', 10)
        time_period=1.0
        self.timer=self.create_timer(time_period,self.callback)
        self.i=0

    def callback(self):
        '''
        msg = String()
        msg.data = 'count is qual to: %d' % self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        '''
        msg = Num()
        msg.num =  self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publishing, I have recieved a count equal: "%s"' % msg.num)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    talker_node = Talker()
    rclpy.spin(talker_node)
    talker_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()  
