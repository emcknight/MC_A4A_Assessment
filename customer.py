import names
import random

## Customer Class ##
class Customer:
    def __init__(self, ticketId = None):
        self.name = names.get_full_name()  # Random Name of customer 
        self.phoneNum = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 9)])  # Random Phone Number of customer
        self.isVIP = random.getrandbits(1) == 1  # Randomized Boolean Indicating if a customer is a VIP customer or not
        self.ticketId = ticketId # Ticket ID auto assigned at customer creation