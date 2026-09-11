
class redbus:
    bus = {i: "available" for i in range(1, 11)}

    userbooking = {}

    def viewbooking(self):
        print("----- BOOKED SEATS -----")

        for seatno in redbus.userbooking:
            print("Seat No:", seatno,
                  "Username:", redbus.userbooking[seatno])

    def displayseats(self):
        print("---------xyz-----------")
        for i in redbus.bus:
            if i in redbus.bus:
                print(i, redbus.bus[i])

    def booking(self, seatno, username):
        for i in redbus.bus:
            if i == seatno and redbus.bus[i] == "available":
                redbus.bus[i] = "booked"
                redbus.userbooking[seatno] = username

                print(f"Your seat - {seatno} is successfully booked")
                break

        else:
            print(f"Your seat - {seatno} is already booked")


class driver(redbus):
    def __init__(self, name, phoneno, driverlicense, salary):
        self.name = name
        self.phoneno = phoneno
        self.driverlicense = driverlicense
        self.__salary = salary

    def display(self):
        print("----------driver details----------")
        print("name:", self.name)
        print("phoneno:", self.phoneno)
        print("driverlicense:", self.driverlicense)


class users(redbus):
    def __init__(self, name, gmail, phoneno):
        self.name = name
        self.gmail = gmail
        self.phoneno = phoneno


mounasri = users("mounasri", "mounasri@gmail.com", 234516789)

mounasri.displayseats()

mounasri.booking(6, mounasri.name)

mounasri.viewbooking()


