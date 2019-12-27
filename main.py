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
for itr in range(1000):
  #influence
  for m1 in moons:
    for m2 in moons:
      if m1 != m2: #not necessary because moon will not influence itself
        m1.influence(m2)
  #move
  for m1 in moons:
    m1.move()

ans = 0
for m1 in moons:
  ans += m1.getEnergy()
print(ans)
