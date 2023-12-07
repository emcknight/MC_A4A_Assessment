from service_scheduler import ServiceScheduler

'''
Mailchimp Backend Service Scheduler Assignment
----------------------------------------------
This program acts as a first come first serve service scheduler with both regular customers and VIP customers.
Assumptions made are as follows:
    1. Multiple Employees can be working during the same day.
    2. A service takes 10 seconds to complete.
    3. A customer enters randomly every 1 to 5 seconds.
    4. Two VIP customers enter for every One regular customer.
'''

if __name__ == "__main__":
     print("Welcome to the scheduler!")
     workers = int(input("How many employees are working today?: "))
     runTime = int(input("How many seconds will the store operate today?: "))
     scheduler = ServiceScheduler(workers, runTime)
     print("The day is done!")
     print(scheduler)
     