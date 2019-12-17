def day12() :
  moons = [];
 
  moons.append([16, -11, 2]);
  moons.append([0, -4, 7]);
  moons.append([6, 4, -10]);
  moons.append([-3, -2, -4]);
  '''
  moons.append([-1, 0, 2]);
  moons.append([2, -10, -7]);
  moons.append([4, -8, 8]);
  moons.append([3, 5, -1]);
   '''
  velocity = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

  print(f"moon count {len(moons)}")
  print(f"velocity count {len(velocity)}")

  steps = 1;
  while steps <=1000:
    for dimension in range(3) :
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


  
