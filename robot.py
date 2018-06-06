import roomba.create as create


class RoombaClient(object):
  def __init__(self, port):
    self.robot = create.Create(port)
    self.toSafeMode()
    self.moving = False
    self.pause()

  def __del__(self):
    self.robot.close()

  def toSafeMode(self):
    print("to safe mode")
    self.robot.toSafeMode()

  def toFullMode(self):
    print("to full mode")
    self.robot.toFullMode()

  def pause(self):
    if self.moving:
      self.move(0, 0)
      self.moving = False

  def move(self, x, theta):
    print("move: %f[m/s], %f[deg/s]" % (x, theta))
    self.robot.go(x * 100, theta)
    self.moving = True

  def moveToward(self, x, theta):
    max_x = 0.2 # m/s
    max_theta = 40 # deg/s
    self.move(x * max_x, theta * max_theta)