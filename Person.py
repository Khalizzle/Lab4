class Person:
  lastIDUsed = 100
  def __init__(self, fName, lName):
    self._fName = fName
    self._lName = lName
    self._ID = Person.lastIDUsed
    Person.lastIDUsed += 1

  def __str__(self):
    tmp = ''
    tmp += 'Name' + str(self._lName) + ',' + str(self._fName)
    return tmp

print(Person('Greg', 'Mandice'))
p1 = Person('Josh', 'Nichols')
print(p1)
