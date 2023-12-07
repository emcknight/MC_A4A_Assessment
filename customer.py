import names
import random

## Customer Class ##
class Customer:
    def __init__(self, isVIP = False, ticketId = None):
        self.name = names.get_full_name()  # Random Name of customer 
        self.phoneNum = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, )])  # Random Phone Number of customer
        self.isVIP = isVIP  # Boolean Indicating if a customer is a VIP customer or not
        self.ticketId = ticketId # Ticket ID auto assigned at customer creation