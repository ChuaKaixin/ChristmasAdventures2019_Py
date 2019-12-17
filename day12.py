from itertools import chain 
from math import gcd
from functools import reduce
def day12() :
  moons = [];
 
  '''
  moons = [[16, -11, 2],[0, -4, 7],[6, 4, -10],[-3, -2, -4]];
  restMoonState = [[16, -11, 2],[0, -4, 7],[6, 4, -10],[-3, -2, -4]];

  moons = [[-1, 0, 2],[2, -10, -7],[4, -8, 8],[3, 5, -1]];
  restMoonState = [[-1, 0, 2],[2, -10, -7],[4, -8, 8],[3, 5, -1]];

  moons = [[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]];
  restMoonState = [[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]];
  '''
  
  moons = [[16, -11, 2],[0, -4, 7],[6, 4, -10],[-3, -2, -4]];
  restMoonState = [[16, -11, 2],[0, -4, 7],[6, 4, -10],[-3, -2, -4]];

  velocity = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]];
  cycles = [0,0,0];
  dimensions = [0,1,2]
  steps = 0;
  dimensionCount = 0;

  print(f"moon count {len(moons)}")
  print(f"velocity count {len(velocity)}")


  def hasReturnedToOriginalState():
    dimensionCount =0;
    for dimension in dimensions:
      moonCount = 0;
      for moon in range(4):
        if moons[moon][dimension]== restMoonState[moon][dimension] and velocity[moon][dimension]== 0:
          moonCount+=1;
      if moonCount==4 and cycles[dimension]==0:
        cycles[dimension] = steps;
        dimensionCount+=1;
    return dimensionCount;

  def lcm(a, b):
    return (a * b) // gcd(a, b)

  steps = 0;
  while True:
    for dimension in dimensions :
      for moon in range(3):
        for anothermoon in range(moon+1, 4):
          if moons[moon][dimension] > moons[anothermoon][dimension]:
            velocity[moon][dimension]-=1;
            velocity[anothermoon][dimension]+=1;
          elif moons[moon][dimension] < moons[anothermoon][dimension]:
            velocity[moon][dimension]+=1;
            velocity[anothermoon][dimension]-=1;
        moons[moon][dimension]+=velocity[moon][dimension];
      moons[3][dimension]+=velocity[3][dimension];
    steps+=1;
    dimensionCount+=hasReturnedToOriginalState();
    if dimensionCount == 3:
      break;
  
  print(f"Completed all cycles with {steps} steps")
  print('ans:', reduce(lcm, cycles))
  '''
  PART 1
  totalEnergy = 0;

  def printInfo(info, description):
    print(f"--------PRINTING FOR {description}---------------")
    for i in info:
      for child in i:
        print (f"index - {i}:{child} ");
      print("--------------")

  printInfo(moons, "Moon");
  printInfo(velocity, "Velocity");
  for moon in range(4):
    pot = 0;
    kin = 0;
    for dimension in range(3):
      pot+=abs(moons[moon][dimension]);
      kin+=abs(velocity[moon][dimension]);
    totalEnergy+=(pot*kin)
  print(f"Total Energy : {totalEnergy}")
'''

  
