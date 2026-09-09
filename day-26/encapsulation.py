#POVIDNG SECURITY TO DATA
'''1. Public Proctection : allowe  inclass , inchildclass ,outsideClass
2. private Protection : allowed inclass [we use double underscore "__"]
3. protected method   : allowed inclass, inChildClass,outsideClass(not recommended)  [we use single underscoe " _"]'''



'''class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._post        

mounasri = Instagram('mounasri','12345')

print(mounasri.username)
print(mounasri.getpassword())
print(mounasri.accesspost) '''



class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    def setpassword(self,setpassword):
        self.__password  = setpassword   

    @property
    def accesspost(self):
        return self._post   

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)


mounasri = Instagram('mounasri','12345')

mounasri.username = "mounasri_123"
print(mounasri.username)

mounasri.setpassword('mouna#123')
print(mounasri.getpassword())

mounasri.accesspost ="python"
mounasri.accesspost ="strings"
mounasri.accesspost ="project" 
print(mounasri.accesspost)