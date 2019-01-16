#!/usr/bin/env python

## Node to publish sensor information to topic.

import rospy
from pkg_2.msg import JhormanSensorInformation
from hrwros_utilities.sim_sensor_data import distSensorData as getSensorData

def sensor_info_publisher():
    simple_publisher = rospy.Publisher('jhorsensor_info', JhormanSensorInformation, queue_size=10)
    rospy.init_node('jhorsensor_info_publisher', anonymous=False)
    rate = rospy.Rate(10)

    # Create the msg data structure template
    jhorinfo = JhormanSensorInformation()

    # Fill in the header information
    jhorinfo.sensor_data.header.stamp = rospy.Time.now()
    jhorinfo.sensor_data.header.frame_id = 'distance_sensor_frame'

    # Fill in the sensor data information
    jhorinfo.sensor_data.radiation_type = jhorinfo.sensor_data.ULTRASOUND
    jhorinfo.sensor_data.field_of_view = 0.5
    jhorinfo.sensor_data.min_range = 0.02
    jhorinfo.sensor_data.max_range = 2.00

    # Fill in the manufacturer name and part number
    jhorinfo.maker_name = 'Jhorman Sensor Inc'
    jhorinfo.part_number = 123456

    while not rospy.is_shutdown():
        # Read the sensor data from a simulated sensor.
        jhorinfo.sensor_data.range = getSensorData(jhorinfo.sensor_data.radiation_type,
            jhorinfo.sensor_data.min_range, jhorinfo.sensor_data.max_range)

        simple_publisher.publish(jhorinfo)
        rospy.loginfo('Everythin is okay with publishing')
        rate.sleep()

if __name__ == '__main__':
    try:
        sensor_info_publisher()
    except rospy.ROSInterruptException:
        pass
