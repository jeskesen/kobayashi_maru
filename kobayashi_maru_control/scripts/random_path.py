#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped,Point
import random
from asn1crypto.cms import Time

def random_path_publisher():
    pub = rospy.Publisher('path_to_follow', Path, queue_size=10)
    rospy.init_node('random_planner', anonymous=True)
    rate = rospy.Rate(1) # 10hz
            
    #hello_str = "hello world %s" % rospy.get_time()
    myPath = Path()
    myPath.header.frame_id="odom"
    myPath.header.stamp = rospy.Time.now()
    myPoses = []
    
    for i in range(10):
        newPose = PoseStamped()
        newPose.header.frame_id="odom"
        newPose.header.stamp = rospy.Time.now()
        newPose.pose.position = Point(random.uniform(-10,10), random.uniform(-10,10), 0)
        myPoses.append(newPose)

    myPath.poses = myPoses
    #pub2.publish(myPoses[0])
    rospy.loginfo(myPath)
    pub.publish(myPath)
    rate.sleep()

if __name__ == '__main__':
    try:
        random_path_publisher()
    except rospy.ROSInterruptException:
        pass

