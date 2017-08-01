# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 15:12:49 2017

@author: Edwin
"""

import datetime
 
class Person(object):
    def __init__(self, name):
         """create a person called name"""
         self.name = name
         self.birthday = None
         self.lastName = name.split(' ')[-1]

    def getLastname(self):
        """return self's last name"""
        return self.lastName
    
    def setBirthday(self,month,day,year):
        """sets sefl's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
    
    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """return True if self's name is lexicographically less than the other's name
        and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.lastName
        return self.lastName < other.lastName
    

    # other moethods
    
    def __str__(self):
        """return self's name"""
        return self.name
    
class LizardPerson(Person):
    nextIdNum = 0 # next ID number to assign
        
    def __init__(self, name):
        Person.__init__(self, name) #initialize person attributes
        self.idNum = LizardPerson.nextIdNum # Lizard person attribute: unique ID
        LizardPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
    
    #sorting lizard poeple uses their ID number, not name.
    def __lt__(self, other):
        return self.idNum < other.idNum
        
    def speak(self,utterance):
        return (self.getLastname() + " says " + utterance)
        
        
class SuperLizard(LizardPerson):
    def __init__(self, name, year):
        LizardPerson.__init__(self, name)
        self.year = year
    def getYear(self):
        return self.year
    def speak(self, utterance):
        return LizardPerson.speak(self, " Dude " + utterance)
    
p1 = Person('Edwin Rhee')
p1.setBirthday(5, 3, 86)
p2 = Person('Sirah Yoo')
p2.setBirthday(10,1,88)
p3 = Person('Bryan Rhee')
p3.setBirthday(6,20,81)
p4 = Person('Sung Dong Kim')

l1 = LizardPerson('Barack Obama')
l2 = LizardPerson('Anderson Cooper')

personList = [p1, p2, p3, p4]
LizardList = [l1,l2]


for e in personList:
    print(e)
    
personList.sort()

print()

for e in personList:
    print(e)
    
for e in LizardList:
    print(e)
    
LizardList.sort()

for e in LizardList:
    print(e)