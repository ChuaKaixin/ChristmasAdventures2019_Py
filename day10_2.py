import math;

def day10_2() :
  input10File   = open("inputDay10_2","r")
  inputs = input10File.readlines()
  inputs = [inputs[i].strip() for i in range(len(inputs)) if i % 2 != 0] 
  
  x = 26
  y = 36

  arrangedCoordinates = {};

  def findAngle(x1, y1) :
    adjustedX = int(x1) - x;
    adjustedY = int(y1) - y;
    return math.atan2(adjustedY, adjustedX);
  
  def sortCoordinates(coordinates) :
    coordinateDict = {}
    for coordinate in coordinates:
      coordinateDict[abs(int(coordinate[1]) - y) + abs(int(coordinate[0])-x)] = coordinate;
    sortedCoordinates = [];
    for key in sorted(coordinateDict.keys()):
      sortedCoordinates.append(coordinateDict[key])
    return sortedCoordinates;

  def deriveCoordinateOrders(coordinates) :
    coordinateList = coordinates.split();
    print(f"coordinate list[1]: {len(coordinateList)}")
    coordinatesArray = [];
    for c in coordinateList:
      c = c.split("-");
      coordinatesArray.append(c);
    angle = findAngle(coordinatesArray[0][0], coordinatesArray[0][1]);
    arrangedCoordinates[angle] = sortCoordinates(coordinatesArray);
    print(f"coordinate list[2]: {len(coordinatesArray)}")
  

  for input in inputs:
    print(f"{input}");
    deriveCoordinateOrders(input);
  
  asteroidCount = 1;
  while asteroidCount <= 200:
    for key in sorted(arrangedCoordinates.keys()):
      asteroid = arrangedCoordinates[key].pop(0);
      print(f"asteroid no. {asteroidCount}: {asteroid[0]}, {asteroid[1]} at angle {key}")
      asteroidCount+=1
    print("--------------------------------")
  

