#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def draw_square():
    rospy.init_node('draw_square', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)
    
    side_length = 2.0
    linear_speed = 1.0
    angular_speed = 1.57
    
    print("开始画正方形...")
    
    for i in range(4):
        # 走直线
        twist = Twist()
        twist.linear.x = linear_speed
        twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(side_length / linear_speed)
        
        # 转90度
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = angular_speed
        pub.publish(twist)
        rospy.sleep(1.0)
    
    # 停止
    pub.publish(Twist())
    print("正方形画完了！")

if __name__ == '__main__':
    try:
        draw_square()
    except rospy.ROSInterruptException:
        pass
