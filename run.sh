#!/bin/bash
# Bash script to run them all

# colors
r='\033[0;31m'
g='\033[0;32m'
b='\033[0;34m'
w='\033[1;37m'

# make sure our package can be recognized by ROS
source ~/rasPi2-ROS/workspace/devel/setup.bash

echo -e "${g}Running roscore...${w}"
roscore &
sleep 3
echo -e "${g}Running main node...${w}" 
# redirect stdout to a file
rosrun raspi main &> ~/rasPi2-ROS/out.txt &
sleep 3
echo -e "${g}Running hokuyo_node...${w}"
rosrun hokuyo_node hokuyo_node &
sleep 3
echo -e "${g}Running serial node...${w}" 
python ~/rasPi2-ROS/serialTiva.py
