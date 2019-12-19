import math

class resource:
  def __init__(self, name, units):
    self.name = name
    self.units = units
    self.oresRequired = 0
    self.sources = {}
    self.rawMaterials = {}
    self.inExcess = 0;

  def addResource(self, name, units):
    self.sources[name] = units

def day14_1() :

  def processInputList() :
    resourceDict = {}
    for line in inputs:
      parts = line.split(" => ")
      endResourceInfo = parts[1].split();
      resourceDict[endResourceInfo[1]] = resource(endResourceInfo[1], int(endResourceInfo[0])); 
      sourceResoureInfo = parts[0].split(", ");
      for source in sourceResoureInfo:
        sourceInfo = source.split();
        resourceDict[endResourceInfo[1]].addResource(sourceInfo[1], int(sourceInfo[0])); 
    return resourceDict;

  def computeResourceRequirement(resourceName, unitsRequired) :
    sources = resourceDict[resourceName].sources
    required = updateResourceUsage(resourceName, unitsRequired)
    if required > 0:
      factor = deriveFactor(resourceName, required, resourceDict[resourceName].units);
      print(f"resource {resourceName} needed - {unitsRequired} actual to generate {required} - excess {resourceDict[resourceName].inExcess}")
      for source in sources.keys():
        if source == "ORE":
          updateRawResourceRequirement(resourceName, factor*resourceDict[resourceName].units);
          print(f"reach end");
        else :
          print(f"source {source} units {factor*sources[source]}")
          computeResourceRequirement(source, factor*sources[source])

  def updateResourceUsage(resourceName, unitsRequired) :
    if resourceDict[resourceName].inExcess >= unitsRequired:
      resourceDict[resourceName].inExcess-=unitsRequired;
      return 0;
    else:
      required = unitsRequired - resourceDict[resourceName].inExcess;
      resourceDict[resourceName].inExcess = 0;
      return required;

  def deriveFactor(resourceName, required, generated) :
    factor = 0;
    if required > generated:
      factor = math.ceil(required/generated);
    elif required > 0:
      factor =  1;
    actualGenerated = factor*generated;
    if actualGenerated > required:
      resourceDict[resourceName].inExcess = actualGenerated - required;
    return factor;

  def updateRawResourceRequirement(resource, count) :
    if resource in rawResourceDict:
      rawResourceDict[resource] +=count;
    else:
      rawResourceDict[resource] = count;
    print(f"raw resource req {resource} - {rawResourceDict[resource]}")

  input14File   = open("inputDay14","r")
  inputs = input14File.readlines()  
  print(f"input lines {len(inputs)}")
  resourceDict = processInputList();
  rawResourceDict = {}
  computeResourceRequirement("FUEL", 1)

  ore = 0;
  for r in rawResourceDict.keys():
    print(f"raw resource {r} required {rawResourceDict[r]} units")
    ore+=(resourceDict[r].sources["ORE"]*(math.ceil(rawResourceDict[r]/resourceDict[r].units)))
  
  print(f"total ore required: {ore}")


 


