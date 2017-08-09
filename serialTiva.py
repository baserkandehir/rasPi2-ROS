import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

Vx = 0.1
Vy = 0.2
Vang = 0

i = 0

while True:
  
  # get the incoming data
  incomingData = port.readline()
  
  # parse the incoming data
  list = incomingData.split(' ');
  ult_dist1 = float(list[1]) / 1000.0
  ult_dist2 = float(list[2]) / 1000.0
  posX = float(list[4]) / 1000.0
  posY = float(list[5]) / 1000.0
  posTheta = float(list[6]) / 1000.0

  print "ult_dist1: ", ult_dist1, "\tult_dist2: ", ult_dist2, "\tposX: ", posX, "\tposY: ", posY, "\tposTheta: ", posTheta

  # prompt velocity commands from the terminal
  #input = raw_input("Enter velocity command: ")
  #velList = input.split(' ')
  #Vx = float(velList[0])
  #Vy = float(velList[1])
  #Vang = float(velList[2])
  #print "Vx: ", Vx, "Vy: ", Vy, "Vang: ", Vang

  # stop the robot after some time
  if i > 1000:
    Vx = 0
    Vy = 0
    Vang = 0

  # send the velocity command to robot
  send = 'c ' + str(int(Vx*1000)) + '\r' + str(int(Vy*1000)) + '\r' + str(int(Vang*1000)) + '\r'
  port.write(send)

  # increment the index
  i = i + 1
