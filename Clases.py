class lunch:
  def __init__(self, type, descp,status):
    self.type = type
    self.descp = descp
    self.status= status

class mealDay:
  def __init__(self, breakFast, snack,lunch,dinner):
    self.breakFast = breakFast
    self.snack = snack
    self.lunch= lunch
    self.dinner= dinner 

class day:
  def __init__(self, mealDay, dayName,type):
    self.mealDay = mealDay
    self.dayName = dayName
    self.type=type