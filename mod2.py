def CheckAcc(YN):
  if YN == 'Y':
    value = True
  else:
    value = False
  return value
    
class user:
    __id = 0
    __passcode:none


    def __init__(self, id, passcode):
        self.__id = id
        self.__passcode= passcode
  
def login(id,passcode):
  id = user(id,passcode)
  
