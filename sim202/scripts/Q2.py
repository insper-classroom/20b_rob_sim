#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
O código para este exercício está em: `sub202/scripts/Q2.py`

Para rodar, recomendamos que faça:

    roslaunch turtlebot3_gazebo turtlebot3_stage_1.launch

Depois:

    rosrun sim202 Q2.py
"""


from __future__ import division, print_function


import rospy
from geometry_msgs.msg import Twist, Vector3

v = 10  # Velocidade linear
w = 5  # Velocidade angular

if __name__ == "__main__":
    rospy.init_node("Q2")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=3)

    try:
        while not rospy.is_shutdown():
            vel = Twist(Vector3(v,0,0), Vector3(0,0,w))
            pub.publish(vel)
            rospy.sleep(2.0)
    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")
