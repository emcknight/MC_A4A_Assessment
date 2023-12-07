import random
import time
from customer import Customer

## Service Scheduler Class ##
class ServiceScheduler:
    def __init__(self, workers, runTime):
        # Defining main features/variables of the Service Scheduler
        self.ticketId = 1
        self.customerQueue = [] # List operating as a queue for regular customers
        self.VIPQueue = [] # List operating as a queue for VIP Customers
        self.numWorkers = workers
        self.workers = [(False, 0, None)] * workers # Using a tuple to represent each worker. (Boolean is working with a customer, seconds working, customer working with))
        self.customersServed = 0
        self.VIPCustomersServed = 0
        self.openTime = runTime
        self.VIPCounter = 0
        self.openStore()
        
    # The store is run by calling this method
    def openStore(self):
        custTime = random.randrange(1, 5, 1) # Defining a random integer between 1 & 5 for the first customer

        # While loop to represent operational time
        while self.openTime > 0:
            # If its time for the customer to come in, new customer added and random next customer time is set
            if self.openTime % custTime == 0:
                self.checkIn()
                custTime = random.randrange(1, 5, 1)
            self.getNextCustomer()
            self.progressWorkers()
            self.openTime -= 1
            time.sleep(1)
        return

    # New customer function
    def checkIn(self):
        cust = Customer(self.ticketId)
        self.ticketId += 1 # Increment ticket ID for next customer

        # Print out the name of the customer in line
        if cust.isVIP:
            self.VIPQueue.append(cust)
            print("VIP Customer", cust.name, "is now in line.")
        else:
            print("Customer", cust.name, "is now in line.")
            self.customerQueue.append(cust)

        return
    
    # Assigns the next available customer to an available worker.
    def getNextCustomer(self):
        # If all workers are currently serving someone, end this function
        if [i[0] for i in self.workers].count(True) == self.numWorkers:
            print("No workers available...")
            return
        # Otherwise, find the first available worker and assign them the next customer prioritizing VIP over Regular 2:1.
        else:
            # Check each worker for availability
            for i in range(self.numWorkers):
                # If the worker is available...
                if self.workers[i][0] == 0:
                    cust = None
                    # VIPCounter keeps track of how many VIPs have come in sequentially.
                    # If the VIPCounter is less than 2, either none or one VIP customer has come through last
                    if self.VIPCounter < 2:
                            # Try to serve the next VIP customer and increase the VIP Counter by 1
                            try:
                                cust = self.VIPQueue.pop(0)
                                self.VIPCounter += 1
                                print("Employee",i+1,"will now serve ticket number:",cust.ticketId)
                            except:
                                # If no VIP customers are waiting, check the regular customer queue
                                try:
                                    cust = self.customerQueue.pop(0)
                                    self.VIPCounter = 0 # Reset VIP counter to 0 to prioritize VIPs next
                                    print("Employee",i+1,"will now serve ticket number:",cust.ticketId)
                                except:
                                    # If no customers are waiting, end the loop
                                    print("No customers waiting...")
                                    break
                    # Else do the opposite of the above and prioritize the regular customer queue.
                    else:
                            try:
                                cust = self.customerQueue.pop(0)
                                self.VIPCounter = 0
                                print("Employee",i+1,"will now serve ticket number:",cust.ticketId)
                            except:
                                try:
                                    cust = self.VIPQueue.pop(0)
                                    self.VIPCounter += 1
                                    print("Employee",i+1,"will now serve ticket number:",cust.ticketId)
                                except:
                                    # If no customers are waiting, end the loop
                                    print("No customers waiting...")
                                    break
                    self.workers[i] = (True, 0, cust) # Worker assigned a customer and set to active
        return 
    
    # Incrementer function to increase the amount of time a customer has been working.
    def progressWorkers(self):
        for i in range(self.numWorkers):
            # If the worker is active...
            if self.workers[i][0]:
                # Increase their current work time by 1
                tmp = list(self.workers[i])
                tmp[1] += 1
                self.workers[i] = tuple(tmp)

                # If current work time gets to 10, reset the worker to inactive and remove the customer
                if self.workers[i][1] == 10:
                    print("Finished serving customer number:",self.workers[i][2].ticketId,"--",self.workers[i][2].name,"\nEmployee",i+1,"is now available.")
                    if self.workers[i][2].isVIP:
                        self.VIPCustomersServed += 1
                    else:
                        self.customersServed += 1
                    self.workers[i] = (False, 0, None)
        return

    # Finish out all customers currently with a worker and print final stats.
    def __str__(self):
        # Overtime calculation for workers going past closing bell
        overTime = 0
        numOTWorkers = 0
        for i in range(self.numWorkers):
            if self.workers[i][0]:
                overTime += (10 - self.workers[i][1])
                numOTWorkers += 1
                if self.workers[i][2].isVIP:
                    self.VIPCustomersServed += 1
                else:
                    self.customersServed += 1
        stillInLine = len(self.customerQueue) + len(self.VIPQueue)

        return f'{self.VIPCustomersServed} VIP customer(s) were served and {self.customersServed} regular customer(s) were served.\n{numOTWorkers} worker(s) had to work a total of {overTime} seconds overtime to finish the day.\n{stillInLine} customer(s) were still in line when the day was finished.'
        