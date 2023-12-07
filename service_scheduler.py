import random
import time
from .customer import Customer

## Service Scheduler Class ##
class ServiceScheduler:
    def __init__(self, workers):
        self.ticketId = 1
        self.customerQueue = []
        self.VIPQueue = []
        self.numWorkers = workers
        self.workers = [(0, 0, None)] * workers
        self.customersServed = 0
        self.VIPCustomersServed = 0
        openTime = 60
        custTime = random.randrange(1, 5, 1)
        while openTime > 0:
            if openTime % custTime == 0:
                self.newCustomer()
                custTime = random.randrange(1, 5, 1)
            self.getNextCustomer()
            self.progressWorkers()
            openTime -= 1
            time.sleep(1)

    def newCustomer(self):
        VIP = self.ticketId % 3 != 0
        cust = Customer(VIP, self.ticketId)
        self.ticketId += 1
        if VIP:
            self.VIPQueue.append(cust)
            print("VIP Customer", cust.name, "is now in line.")
        else:
            print("Customer", cust.name, "is now in line.")
            self.customerQueue.append(cust)
        return
    
    def getNextCustomer(self):
        if [i[0] for i in self.workers].count(1) == self.numWorkers:
            print("No workers available...")
            return
        else:
            for i in range(self.numWorkers):
                cust = None
                if self.workers[i][0] == 0:
                    try:
                        cust = self.VIPQueue.pop(0)
                        print("Now serving ticket number:",cust.ticketId)
                    except:
                        try:
                            cust = self.customerQueue.pop(0)
                            print("Now serving ticket number:",cust.ticketId)
                        except:
                            print("No customers waiting...")
                            break
                    self.workers[i] = (1, 0, cust)
        return 
    
    def progressWorkers(self):
        for i in range(self.numWorkers):
            if self.workers[i][0] == 1:
                tmp = list(self.workers[i])
                tmp[1] += 1
                self.workers[i] = tuple(tmp)
                if self.workers[i][1] == 10:
                    print("Finished serving customer number:",self.workers[i][2].ticketId,"--",self.workers[i][2].name)
                    if self.workers[i][2].isVIP:
                        self.VIPCustomersServed += 1
                    else:
                        self.customersServed += 1
                    self.workers[i] = (0, 0, None)
        return

    def __str__(self):
        overTime = 0
        numOTWorkers = 0
        for i in range(self.numWorkers):
            if self.workers[i][0] == 1:
                overTime += (10 - self.workers[i][1])
                numOTWorkers += 1
                if self.workers[i][2].isVIP:
                    self.VIPCustomersServed += 1
                else:
                    self.customersServed += 1
        return f'{self.VIPCustomersServed} VIP customer(s) were served and {self.customersServed} regular customer(s) were served.\n{numOTWorkers} worker(s) had to work a total of {overTime} seconds overtime to finish the day.'
        