import random

type = ["preset","hybrid"][1]
width = 10
height = 10
# unitRotation = 0
terrainType = ["land","forest","building","road","water"]
# unitType = ["BasicInf","BasicCalv","12lbArty","MedInf","MedCalv","4lbArty","AdvInf","AdvCalv","6inArty"]
heightValues = range(0,7)

# # makes all units rotate with the standard rotational directions
# unitRotation = unitRotation+270

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
player1UnitList = []
player2UnitList = []
for 

if type == "hybrid":
    # {"type":"type",map:{"width":1000,"height":1000,"terrains":terrainTypeList,"heightMap":heightList}},
    hybridMap = f"{'{'}\"type\":\"{type}\",\"map\":{'{'}\"width\":{width},\"height\":{height},\"terrains\":{terrainTypeList},\"heightMap\":{heightList}{'}}'}"
    print(hybridMap)
    with open("Auto.json","w") as scenario:
        scenario.write(hybridMap)
else:
    presetMap = f"{'{'}\"type\":\"{type}\",\"map\":{'{'}\"width\":{width},\"height\":{height},\"terrains\":{terrainTypeList},\"heightMap\":{heightList}{'},'}"
    print(presetMap)
    with open("Auto.json","w") as scenario:
        scenario.write(presetMap)