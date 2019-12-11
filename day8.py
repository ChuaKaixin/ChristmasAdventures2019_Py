
def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

inputFile = open("input","r")
inputString = inputFile.read()
inputFile.close()
width = 25
height = 6

noOfPixelsPerLayer = width*height;
layers = split_len(inputString, noOfPixelsPerLayer);
print(f"No of layers {len(layers)}")

layerWithMinZero = 0;
minNoOfZero = 1000;
index = 0;
for layer in layers:
  layerZeroCount = layer.count('0');
  if layerZeroCount < minNoOfZero:
    layerWithMinZero = index;
    minNoOfZero = layerZeroCount;
  index+=1;

  
print(f"Layer with min zero: {layerWithMinZero}, Zero count: {minNoOfZero}")

numOfOnes = layers[layerWithMinZero].count('1')
numOfTwos = layers[layerWithMinZero].count('2')

print(f"Answer part 1: {numOfOnes*numOfTwos}")

image = "";
currentIndex = 0;
pixelDefinition = '';
for currentIndex in range(noOfPixelsPerLayer):
  currentLayer = 0;
  pixelDefined = False;
  while not pixelDefined:
    if layers[currentLayer][currentIndex] == '0':
      image+='X';
      pixelDefined = True;
    elif layers[currentLayer][currentIndex] == '1':
      image+=' ';
      pixelDefined = True;
    else:
      currentLayer+=1;
  currentIndex+=1;

decryptedImage = split_len(image, width);
for line in decryptedImage:
  print(f"{line}")
