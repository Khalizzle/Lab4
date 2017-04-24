class Person:
  lastIDUsed = 100
  def __str__(self):
    tmp = ''
    tmp += 'Name' + str(self._lName) + ',' + str(self._fName)
    return tmp

print(Person('Greg', 'Mandice'))
