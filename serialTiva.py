import serial
import sys
import signal
import struct

def signal_handler(signal, frame):
  print('Stopping the robot')
  send = 'c ' + str(0) + '\r' + str(0) + '\r' + str(0) + '\r'
  port.write(send)
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

#i = 0

# get the velocity commands from command line arguments
#Vx = float(sys.argv[1])
#Vy = float(sys.argv[2])
#Vang = float(sys.argv[3])

while True:
  
  # get the incoming data
  incomingData = port.read(31)

  # make sure some data is received
  if incomingData:
    # parse the incoming data
    ult_dist1 = struct.unpack('<f', incomingData[2:6])[0]
    ult_dist2 = struct.unpack('<f', incomingData[7:11])[0]
    posX = struct.unpack('<f', incomingData[14:18])[0]
    posY = struct.unpack('<f', incomingData[19:23])[0]
    posTheta = struct.unpack('<f', incomingData[24:28])[0]

    print "ult_dist1: ", ult_dist1, "\tult_dist2: ", ult_dist2, "\tposX: ", posX, "\tposY: ", posY, "\tposTheta: ", posTheta

  # prompt velocity commands from the terminal
  #input = raw_input("Enter velocity command: ")
  #velList = input.split(' ')
  #Vx = float(velList[0])
  #Vy = float(velList[1])
  #Vang = float(velList[2])
  #print "Vx: ", Vx, "Vy: ", Vy, "Vang: ", Vang

  # stop the robot after some time
  #if i > 10:
  #  send = 'c ' + str(0) + '\r' + str(0) + '\r' + str(0) + '\r'
  #  port.write(send)
  #  break;

  Vx = 0
  Vy = 0
  Vang = 0

  # read the velocity commands from the file
  fileHandle = open('/home/ubuntu/rasPi2-ROS/out.txt', 'r')
  lineList = fileHandle.readlines()
  if lineList:
    lastLine = lineList[-1]
    if lastLine[0] is "V":
      #print lastLine
      lastLineList = lastLine.split(' ');  
      #print lastLineList
      Vx = float(lastLineList[1])
      Vy = float(lastLineList[3])
      #print "Vx: ", Vx, " Vy: ", Vy, "\n"
  fileHandle.close()

  # send the velocity command to robot
  send = 'c ' + str(Vx) + '\r' + str(Vy) + '\r' + str(Vang) + '\r'
  port.write(send)

  # increment the index
  #i = i + 1
