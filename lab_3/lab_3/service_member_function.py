from lab_2_msgs.srv import MultiplyThreeInts

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(MultiplyThreeInts, 'multiply_three_ints', self.multiply_three_ints_callback)

    def multiply_three_ints_callback(self, request, response):
        response.product = request.a * request.b * request.c
        self.get_logger().info('Incoming request\n a: %d b: %d c: %d' % (request.a, request.b, request.c))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()