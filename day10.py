from decimal import Decimal
from collections import OrderedDict
class Asteroid:
  def __init__(self, asteroidName, xint, yint):
    self.name = asteroidName
    self.x = xint
    self.y = yint
    self.connections = {}
  
  def addConnection(self, connection, line):
    print(f"connection {connection} line {line}")  
    if not line in self.connections:
      self.connections[line] = []
    self.connections[line].append(connection); 

def day10():
  
  '''
  methods
  '''
  def computeLineEquation(x1, y1, x2, y2) :
    if x2-x1==0:
      return "x=" + str(x1);
    else:
      m = Decimal((y2 - y1)) / Decimal(x2 - x1)
      c = (y2 - (m * x2))
      return str(round(m, 2))+"|" + str(round(c,2));

  def lineFromPoints(x1, y1, x2, y2): 
    a = y2 - y1 
    b = x1 - x2  
    c = a*(x1) + b*(y1)  
    if(b<0):  
        equation = str(a)+ "x" + str(b) + "y=" + str(c);
    else: 
        equation = str(a) + "x+" + str(b) + "y=" + str(c);
    return equation;

  input10File   = open("inputDay10","r")
  inputs = input10File.readlines()

  asteroidMap = OrderedDict()

  for y in range(len(inputs)):
    for x in range(len(inputs[0])-1):
      if inputs[y][x] == "#":
        asteroidMap[str(x)+"-"+str(y)] = Asteroid(str(x)+"-"+str(y), x, y);

  index = 1
  asteroidKeyList = list(asteroidMap);
  for asteroid in asteroidMap.keys():
    for anotherAsteroid in range(index, len(asteroidMap.keys())) :
      equation = computeLineEquation(asteroidMap[asteroid].x, asteroidMap[asteroid].y, 
        asteroidMap[asteroidKeyList[anotherAsteroid]].x, 
        asteroidMap[asteroidKeyList[anotherAsteroid]].y);
        
      asteroidMap[asteroid].addConnection(
        asteroidKeyList[anotherAsteroid],
        equation + "[D]")
      asteroidMap[asteroidKeyList[anotherAsteroid]].addConnection(
        asteroid,
        equation+ "[U]")  
    index+=1
    
  bestAsteroidCount = 0
  for asteroid in asteroidMap.values():
    if len(asteroid.connections) > bestAsteroidCount:
      bestAsteroidCount = len(asteroid.connections);
  print(f"BEST ASTEROID COUNT: {bestAsteroidCount}")
  input10File.close()

  
