import random
import math




type = ["preset","hybrid"][0]
width = 1000
height = 500
unitRotation = 0
terrainType = ["land","forest","building","road","water"]
unitType = ["null","BasicInf","BasicCalv","12lbArty","MedInf","MedCalv","4lbArty","AdvInf","AdvCalv","6inArty"]
heightValues = range(0,7)


# makes all units rotate with the standard rotational directions
unitRotation = unitRotation+270


#creates the basic tile row
tileRow = []
for tile in range(width):
   tileRow.append(0)


#generates the terrainTypeList
terrainTypeList = []
heightList = []
for row in range(height):
   terrainTypeList.append(tileRow)
   heightList.append(tileRow)


#generates the units
UnitList = []


for row in range(math.floor(height/4)):
   for unitInRow in range(math.floor(width/12)-1):
       #{"player":1,"pos":{"x":168.66,"y":310.31},"rotation":0,"type":9}
       UnitList.append(f"{'{'}\"player\":1,\"pos\":{'{'}\"x\":{unitInRow*10+10},\"y\":{row+10}{'}'},\"rotation\":{unitRotation},\"type\":{7}{'}'}")
for row in range(math.floor(height/4)):
   for unitInRow in range(math.floor(width/12)-1):
       #{"player":1,"pos":{"x":168.66,"y":310.31},"rotation":0,"type":9}
       UnitList.append(f"{'{'}\"player\":2,\"pos\":{'{'}\"x\":{unitInRow*10+10},\"y\":{height-row-10}{'}'},\"rotation\":{unitRotation},\"type\":{2}{'}'}")


if type == "hybrid":
   # {"type":"type",map:{"width":1000,"height":1000,"terrains":terrainTypeList,"heightMap":heightList}},
   hybridMap = f"{'{'}\"type\":\"{type}\",\"map\":{'{'}\"width\":{width},\"height\":{height},\"terrains\":{terrainTypeList},\"heightMap\":{heightList}{'}}'}"
   print(hybridMap)
   with open("Auto.json","w") as scenario:
       scenario.write(hybridMap)
else:
   presetMap = f"{'{'}\"type\":\"{type}\",\"map\":{'{'}\"width\":{width},\"height\":{height},\"terrains\":{terrainTypeList},\"heightMap\":{heightList}{'}'},\"units\":[{','.join(UnitList)}]{'}'}"
   print(presetMap)
   with open("Auto.json","w") as scenario:
       scenario.write(presetMap)

