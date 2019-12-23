
import numpy as np
import itertools

def day16():



  input16File   = open("inputDay16","r")
  input = input16File.readlines()
  print(f"length of number:{len(input[0])} : {input[0]}")

  pattern = [0,1,0,-1]

  def processNum(elementNum, stringToWorkOn) :
    l = list(np.repeat(pattern, elementNum))
    r = itertools.cycle(l);
    sum = 0;
    next(r);
    for i in stringToWorkOn:
        sum += (int(i)*next(r));
    #print(f"sum is {sum} result to return {abs(sum)%10}")
    return abs(sum)%10
  
  stringToWorkOn = input[0];
  print(f"string to work on {stringToWorkOn}")
  count = 0
  while count <=99:
    numstr = "";
    for index in range(len(stringToWorkOn)):
      element = index+1;
      numstr += str(processNum(element, stringToWorkOn))
    stringToWorkOn = numstr;
    #print(f"NEW string to work on {stringToWorkOn}")
    count+=1;
  print(f"FINAL output: {stringToWorkOn}")
