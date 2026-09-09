class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):                                          # single inheritance
        print("you can upload the status for 24 hrs")

lohitha = whatsappv1()
lohitha.message()       

usharani = whatsappv2()
usharani.message()
usharani.status()





'''class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):                                          # multilevel inheritance
        print("you can upload the status for 24 hrs")


class whatsappv3(whatsappv2):
    def groups(self):
        print("you can create groups and communicate with multiple people at atime")        

lohitha = whatsappv1()
lohitha.message()       

usharani = whatsappv2()
usharani.message()
usharani.status()

mounasri = whatsappv3()
mounasri.message()
mounasri.status()
mounasri.groups()'''


class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):                                          # multilevel inheritance
        print("you can upload the status for 24 hrs")          #multiple inheritance
                                                               # hybrid inheritance 


class whatsappv3(whatsappv2):
    def groups(self):
        print("you can create groups and communicate with multiple people at atime")    


class  whatsappv4:
    def community(self):
        print("you can combine multiple groups")

class whatsappv5(whatsappv3,whatsappv4):
    def channels(self):
        print("you can access to different channels")


mounasri = whatsappv5()
mounasri.message()
mounasri.status()
mounasri.groups()
mounasri.community()
mounasri.channels()



class whatsappv1:
    def message(self):
        print("you can send a message")
S
class whatsappv2(whatsappv1):
    def status(self):                                          
        print("you can upload the status for 24 hrs")          # hirarchial inheritance
                                                            


class whatsappv3(whatsappv1):
    def groups(self):
        print("you can create groups and communicate with multiple people at atime")    


class  whatsappv4(whatsappv1):
    def community(self):
        print("you can combine multiple groups")




mounasri = whatsappv1()
mounasri.message()
mounasri = whatsappv2()
mounasri.message()
mounasri.status()
mounasri = whatsappv3()
mounasri.message()
mounasri.groups()
mounasri = whatsappv4()
mounasri.message()
mounasri.community()
