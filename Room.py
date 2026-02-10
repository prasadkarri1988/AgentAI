class Room:

  def __init__(self,no,status):
      self.no=no
      self.status=status

  def getName(self):
      return self.no;
  def getStatus(self):
      return self.status;
  def setNo(self,no):
      self.no=no

  def setStatus(self,status):
      self.status=status

  def is_dirty(self):
      return self.status == "Dirty"

  def clean(self):
      self.status = "Clean"

  def show(self):
      print("Room", self.no, "is", self.status)


class CleanerAgent:
    def clean_rooms(self, rooms):
        for room in rooms:
            if room.is_dirty():
                print("Cleaning Room", room.no)
                room.clean()

# ----- MAIN PROGRAM -----
r1 = Room(1, "Clean")
r2 = Room(2, "Dirty")
r3 = Room(3, "Dirty")

rooms = [r1, r2, r3]

print("Before cleaning")
for room in rooms:
    room.show()

agent = CleanerAgent()
agent.clean_rooms(rooms)

print("\nAfter cleaning:")
for r in rooms:
    r.show()