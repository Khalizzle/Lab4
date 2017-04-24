class Person:
  lastIDUsed = 100
  def __init__(self, fName, lName, ID):
    self._fName = fName
    self._lName = lName
    self._ID = Person.lastIDUsed
    Person.lastIDUsed += 1
