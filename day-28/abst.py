# ABSTRACTION: hiding complexity and displating what is needed


from abc import ABC,abstractmethod



class payment(ABC):
    def source(self):
        print("sccaner /upIID/mobile number")
    def amount(self):
        print("enter the amount")
    def bank(self):
        print("select  the bank")
    def pin(self):
        print("enter the pin")
        

    @abstractmethod    
    def paymentprocess(self):
        pass 


    def paymentstatus(self):
        print("payment successful/payment failed")    

class HDFC(payment):
    def paymentprocess(self):
        print("payment process through HDFC bank")

class ICIC(payment):
    def paymentprocess(self):
        print("payment process through ICIC bank")

class AXIS(payment):
    def paymentprocess(self):
        print("payment process through AXIS bank")

class UNION(payment):
    def paymentprocess(self):
        print("payment process through UNION bank")


lohitha = HDFC()
lohitha.source()
lohitha.amount()        
lohitha.bank()
lohitha.pin()
lohitha.paymentprocess()
lohitha.paymentstatus()


mounasri= ICIC()
mounasri.source()
mounasri.amount()        
mounasri.bank()
mounasri.pin()
mounasri.paymentprocess()
mounasri.paymentstatus()


uasha= AXIS()
uasha.source()
uasha.amount()        
uasha.bank()
uasha.pin()
uasha.paymentprocess()
uasha.paymentstatus()


priya=UNION()
priya.source()
priya.amount()        
priya.bank()
priya.pin()
priya.paymentprocess()
priya.paymentstatus()


        
    
