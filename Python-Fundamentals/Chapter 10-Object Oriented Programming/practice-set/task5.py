#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Pakistani Railways
class Train:
    def __init__(self,name,total_seats,available_seats,fare):
        self.name = name;
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.fare = fare

    def book_tickets(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            print("Ticket Booked Successfully")
        else:
            print("We are very sorry no seats are available")
    def getStatus(self):
        print(f"The total number of seats for this train are {self.total_seats}\n")
        print(f"The available seats for this train are {self.available_seats}\n")
    def getFare(self):
        print(f"The fare for this train is {self.fare}")
KarachiExpress = Train("Karachi Express",100,0,1500)
KarachiExpress.getStatus()
KarachiExpress.getFare()
KarachiExpress.book_tickets()

        