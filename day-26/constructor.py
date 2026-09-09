
# constructor: it is aspecial method used to call automatically when ever we are creating an object


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to Instagram,{self.username}')
mounasri = Instagram('mounasri','12345')
lohitha = Instagram('mounasri','12345')
usharani  = Instagram('mounasri','12345')
syamala  = Instagram('mounasri','12345')