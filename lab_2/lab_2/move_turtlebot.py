import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist

class Move_turtlebot(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.publisher = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.timer = self.create_timer(1.0,self.publish_velocity)
        self.get_logger().info('Move turtlebot started. Publishing to /turtle1/cmd_vel')

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x=1.0
        msg.angular.z=0.5
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: linear.x=%.1f, angular.z=%.1f' % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    move_turtlebot= Move_turtlebot()
    try:
        rclpy.spin(move_turtlebot)
    except KeyboardInterrupt:
        pass
    finally:
        # Stop the turtle when the node is shut down
        stop_msg = Twist()
        move_turtlebot.publisher_.publish(stop_msg)
        move_turtlebot.get_logger().info('Stopping turtle...')
        
        move_turtlebot.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()