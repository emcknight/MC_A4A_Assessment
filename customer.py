import names
import random

'''
Mailchimp Backend Service Scheduler Assignment - Customer Class
---------------------------------------------------------------
This is the prescribed customer class used to store information about each customer being checked in. Information includes a fully randomized name,
phone number, and whether or not the customer is a VIP or not. Ticket ID is then only piece of data passed into the function for storage.
'''
class Customer:
    def __init__(self, ticketId = None):
        self.name = names.get_full_name()  # Random Name of customer 
        self.phoneNum = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 10)])  # Random 10 digit Phone Number of customer
        self.isVIP = random.getrandbits(1) == 1  # Randomized Boolean Indicating if a customer is a VIP customer or not
        self.ticketId = ticketId # Ticket ID auto assigned at customer creation