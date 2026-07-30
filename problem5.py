'''
Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
fare information of train running under Bangladesh Railways
'''

class Train:
    Station = "Welcome to Bangladesh Railways"
    info = "Destination: Pabna to Dhaka"
    def __init__(self, ticket_book, status, info):
        self.ticket_book = ticket_book
        self.status = status
        
        
    
    def booking(self):
        import random
        num = random.randint(100, 500)
        book = input("Do You Wanna book a ticket? write yes or no: ")
        if(book == "yes"):
            self.ticket_book = num
            self.status = "Booked"
            print(f"your ticket has been booked.  your ticket number is {num}")
        else:
            print("Booking Cnacelled")

a = Train(ticket_book=None, status="Not Booked", info="Pabna to Dhaka")
print(a.Station)
print(a.info)
a.booking()

input("\nPress Ctrl to exit...")

            
        