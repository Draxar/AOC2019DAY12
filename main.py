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
    if self.x < other.x:
      self.vx += 1
    if self.x < other.x:
      self.vx -= 1