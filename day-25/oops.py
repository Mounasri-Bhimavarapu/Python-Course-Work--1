'''class Flipkart:                # class[keyword]  class name
    pass                         # variable = class name()

lohitha = Flipkart()
usha = Flipkart() 
mounasri = Flipkart()   '''   

class Flipkart:
    discount = 30
    
    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print('updatedSdiscount:',cls.discount)



    def info(self, name, phoneno,address):
        self.name =name                                  # @instancemethod
        self.phoneno =phoneno
        self.address = address
        print(f'Welcome to the Flipkart',self.name)

    @staticmethod

    def banner():
        print(f'{Flipkart.discount}% dicount is goining,grab the product....')




lohitha = Flipkart()
lohitha.info('lohitha',8106732779,'hyd')
lohitha.updatediscount()
lohitha.banner()

usharani = Flipkart()
usharani.info('uasharani',1234567891,'benglr')
usharani.updatediscount()
usharani.banner()
mounasri = Flipkart()
mounasri.info('mounasri',2346789890,'chen')
mounasri.updatediscount()
mounasri.banner()

