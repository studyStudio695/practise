# Main
"""
  author: STUDY STUDIO
  
"""
import mod1 as m1
import os
import mod2 as m2

m1.speak('welcome to our program')
m1.speak('Do You Have An Account')
AccYN = input('Answer In Y or N >> ')
if m2.CheckAcc(AccYN):
    m1.speak('So Enter Your Id')
    Id = input("ID >> ")
    m1.speak("And Enter Your pass")
    passcode = input("PASS >>")
    m2.login(Id,password)
elif m2.CheckAcc(AccYN) == False:
    input()
  
  
  
