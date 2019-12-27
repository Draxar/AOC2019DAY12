def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

class moon:
  def __init__(self,x,y,z):
    #coords
    self.x = x
    self.y = y
    self.z = z
    #velos
    self.vx = 0
    self.vy = 0
    self.vz = 0

  def getxstr(self):
    return "" + str(self.x) + ":" + str(self.vx)

  def getystr(self):
    return "" + str(self.y) + ":" + str(self.vy)

  def getzstr(self):
    return "" + str(self.z) + ":" + str(self.vz)

  
  def influence(self, other):
    #x
    if self.x < other.x:
      self.vx += 1
    if self.x > other.x:
      self.vx -= 1
    #y
    if self.y < other.y:
      self.vy += 1
    if self.y > other.y:
      self.vy -= 1
    #z
    if self.z < other.z:
      self.vz += 1
    if self.z > other.z:
      self.vz -= 1
  
  def move(self):
    self.x += self.vx
    self.z += self.vz
    self.y += self.vy

  def getEnergy(self):
    pot = abs(self.x) + abs(self.y) + abs(self.z)
    kin = abs(self.vx) + abs(self.vy) + abs(self.vz)
    return pot * kin


#input
#<x=4, y=12, z=13>
#<x=-9, y=14, z=-3>
#<x=-7, y=-1, z=2>
#<x=-11, y=17, z=-1>
moons = list()
moons.append(moon(4,12,13))
moons.append(moon(-9,14,-3))
moons.append(moon(-7,-1,2))
moons.append(moon(-11,17,-1))

xs = -1
ys = -1
zs = -1

xset = set()
yset = set()
zset = set()

for itr in range(10000000000):
  done = True
  #influence
  for m1 in moons:
    for m2 in moons:
      if m1 != m2: #not necessary because moon will not influence itself
        m1.influence(m2)
  #move
  for m1 in moons:
    m1.move()
  xstr = ""
  ystr = ""
  zstr = ""
  if xs == -1:
    for m1 in moons:
      xstr = xstr + m1.getxstr()
    llen = len(xset)
    xset.add(xstr)
    if llen == len(xset):
      print("X:")
      print(itr)
      xs = itr

  if ys == -1:
    for m1 in moons:
      ystr = ystr + m1.getystr()
    llen = len(yset)
    yset.add(ystr)
    if llen == len(yset):
      print("Y:")
      print(itr)
      ys = itr

  if zs == -1:
    for m1 in moons:
      zstr = zstr + m1.getzstr()
    llen = len(zset)
    zset.add(zstr)
    if llen == len(zset):
      print("Z:")
      print(itr)
      zs = itr
  
  if itr % 10000 == 0:
    print(itr)

  if xs != -1 and ys != -1 and zs != -1:
    ans = lcm(xs,lcm(ys,zs))
    break
      

print(ans)
