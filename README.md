<a name="readme-top"></a>

## About The Project
This is my project used to complete Intuit Mailchimp's A4A technical assesment. This is a mock service scheduler that handles much like the Apple Genius bar or an old school deli counter where customers are served in order of arrival. This code is written 100% in python. The output shows a second by second counter of what is happening in the shop.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Service Scheduler

## Description
Design and implement a service scheduler for an in-person customer service center (Very similar to genius bar at the Apple centers or Xfinity store service).

1. Customer walks into the store and checks in. They are given a ticket with a sequential service number.
2. The service number is called by the staff in the order determined by the scheduler.
3. There are 2 different tiers of customers:

   1) Regular customers are serviced in the order they arrive.

   2) VIP customers. VIP customers are given higher priorities compared to Regular customers.

### Part 1
Design class for customer and ServiceScheduler with required high-level characteristics.

#### Important notes & answers to common questions:
* Scheduler only need to handle in person scheduling. There is no other type of scheduling, such as online scheduling, phone calls, etc.
* All customers have their information records in the system.
* To schedule, we need customer’s name and phone number.
* For simplicity, all service requests go through the same scheduling/service process.

### Part 2
Implement the ServiceScheduler to serve ALL VIP customers before serving regular customers. Implement two methods checkIn(Customer) and getNextCustomer()

#### Important notes & answers to common questions:
* Serving a customer is an atomic operation, i.e., we do not stop serving a regular customer in the middle of the service when a VIP customer walks in.

### Part 3
Implement the scheduler to make sure 2:1 VIP vs. Regular customer processing rate. Modify getNextCustomer() method to implement the customer processing rate.

---
<p align="right">(<a href="#readme-top">back to top</a>)</p>
