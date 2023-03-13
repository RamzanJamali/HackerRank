import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.task.Task import Task
import random

tilesEgg = loader.loadModel("tiles.egg")

plain = tilesEgg.find('**/plain')
city = tilesEgg.find('**/city')
hill = tilesEgg.find('**/hill')

tiles = [plain,plain,plain,plain,city,hill,hill,hill]
print(tiles)

map = NodePath('map')
map.reparentTo(render)
for x in xrange(-15,15):
    for y in xrange(-15,15):
        tile = random.choice(tiles)
        tile.copyTo(map)
        tile.setPos(.75*(x*2),.8*(x%2+y*2),0)
        tile.setH(tile.getH()+60*random.randint(0,6))
map.flattenStrong()
