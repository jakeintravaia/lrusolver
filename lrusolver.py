cache = []
cache_size = 4 # Amount of pages in cache
inserts = [0, 3, 4, 3, 8, 6, 9, 1, 4, 9, 7, 9, 5, 3, 1, 2, 4] # Change these values according to problem set
faults = 0 # Global variable used to count page faults

class Page:
  def __init__(self, value, age):
    self.value = value
    self.age = age

def main():
  global cache_size
  # Initialize empty slots
  for i in range((cache_size - 1), -1, -1):
    p = Page(-1, i)
    cache.append(p)
  insertPage()

def printPages():
  border = ("="*20)
  print(border)
  for p in cache:
    if p.value == -1:
      print("Value: EMPTY")
    else:
      print("Value: {}".format(p.value))
  print(border)
    

def insertPage():
  global faults
  for i in inserts:
    lru = max(cache, key=lambda x: x.age)
    if not checkExist(i) and cacheFull():
      print("***PAGE FAULT***")
      faults += 1
    if not checkExist(i):
      lru.value = i
      lru.age = 0
      updateAges(lru)
    else:
      p = getIndex(i)
      cache[p].value = i
      cache[p].age = 0
      updateAges(cache[p])
    print("INSERT PAGE {}".format(i))
    printPages()
  printSummary()

def printSummary():
  global faults
  print("Total Inserts: {}".format(len(inserts)))
  print("Total Faults: {}".format(faults))

def getIndex(i):
  for page in cache:
    if page.value == i:
      return cache.index(page)

def checkExist(value):
  for page in cache:
    if page.value == value:
      return True
  return False

def cacheFull():
  if all(x.value != -1 for x in cache):
    return True
  else:
    return False
    

def updateAges(lru):
  for page in cache:
    if page is not lru:
      page.age += 1


if __name__ == "__main__":
  main()