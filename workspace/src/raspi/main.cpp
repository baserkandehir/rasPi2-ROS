#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "math.h"
#include "stdio.h"

float angle_max = 2.0923497676849365;
float angle_min = -2.0862138271331787;
float angle_increment = 0.00613592332229;
float min_range = 0.02;

// angle offset between robot and the sensor
float angle_offset = 12;

// threshold distance for moving robot
float dist_threshold = 0.2;

void laserScanCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
  //ROS_INFO("Entered laser scan callback.");

  // find the angle at which distance is smallest
  float angle, val;
  float min = 9999;
  float i = angle_min;
  float j = 0;
  float Vx, Vy;

  for (; i <= angle_max; i = i + angle_increment, j++)
  {
    val = scan->ranges[j];
    if (val < min && val > min_range)
    {
      min = val;
      angle = i;
    }
  }

  // convert angle from radian to deg
  angle = angle * 57.3;
  ROS_INFO("Angle: %f", angle);

  // calculate robot commands based on angle
  if (min < dist_threshold)
  {
    Vx = 0.25*sin((angle - angle_offset)/57.3);
    Vy = 0.25*cos((angle - angle_offset)/57.3);
  }
  else
  {
    Vx = 0;
    Vy = 0;
  }
  std::cout << "Vx: " << Vx << " Vy: " << Vy << " " << std::endl;
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "main");

  ros::NodeHandle nh;
  ros::Subscriber scanSub;

  ROS_INFO("Program has started.");

  // adjust Hokuyo laser limits
  nh.setParam("/hokuyo_node/max_ang", angle_max);                                              
  nh.setParam("/hokuyo_node/min_ang", angle_min); 

  scanSub = nh.subscribe("/scan", 1000, laserScanCallback);

  ros::spin();

  return 0;
}
