class Task(object):
     
    id = 0   
        
    def __init__(self, description, programmer, workload):  
        type(self).id += 1 
        self.id = type(self).id
        self.description = str(description)
        self.programmer = str(programmer)
        self.workload = int(workload)
        self.finished = False  
    
    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}:{self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook(Task):
    
    def __init__(self):
        self.orders = []
        self.programmers = []
        

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.orders.append(task)
        self.programmers.append(programmer)


    def all_orders(self):
        return self.orders
    
    
    def all_programmers(self):
        return set(self.programmers)
    
    
    def programmers_orders(self):
        orders_by_prog = {}
        for programmer in self.all_programmers():
            orders_by_prog[programmer] = [str(order.description) for order in self.orders if order.programmer == programmer]
        return orders_by_prog
      

    def mark_finished(self, id):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
            
    
    def finished_orders(self):
        finished = [order for order in self.orders if order.is_finished()]
        return finished if len(finished) != 0 else ["No finished orders"]

    
    def unfinished_orders(self):
        unfinished = [order for order in self.orders if not order.is_finished()]
        return unfinished if len(unfinished) != 0 else ["No unfinished orders"]
    
    
    def status_of_programmer(self, programmer):
        nb_finished_ord = len([order for order in self.orders if order.programmer == programmer and order.is_finished()])
        nb_unfinished_ord = len([order for order in self.orders if order.programmer == programmer and not order.is_finished()])
        nb_finished_workload = sum([order.workload for order in self.orders if order.programmer == programmer and order.is_finished()])
        nb_unfinished_workload = sum([order.workload for order in self.orders if order.programmer == programmer and not order.is_finished()])
        return (nb_finished_ord, nb_unfinished_ord, nb_finished_workload, nb_unfinished_workload)
                

error_message= "Erroneous input.\n"

def manage_orders():

    orders = OrderBook()

    print("Commands:")
    print("0: Exit")
    print("1: Add order")
    print("2: List finished tasks")
    print("3: List unfinished tasks")
    print("4: Mark task as finished")
    print("5: Programmers")
    print("6: Status of programmer \n" )

    while True:

        command = input("Enter command: ")

        if command == "0":
            print(f"command: {command}")
            print("Exited")
            break
        
        elif command == "1":
            description = input("Enter description: ")
            programmer = input("Enter programmer: ")
            workload = input("Enter workload: ")
            
            print(f"command: {command}")
            print(f"description: {description}")
            print(f"programmer and workload estimate: {programmer}  {workload}")

            try:
                workload = int(workload)
                if workload <= 0:
                    raise ValueError
                orders.add_order(description, programmer, workload)
                print("Order added. \n")
            except ValueError:
                print(error_message)

        elif command == "2":
            print(f"command: {command}")
            for order in orders.finished_orders():
                print(order)

        elif command == "3":
            print(f"command: {command}")
            for order in orders.unfinished_orders():
                print(order)
                print("")


        elif command == "4":
            print(f"command: {command}")
            id = input("Enter id: ")
            try:
                id = int(id)
                if id in [order.id for order in orders.all_orders()]: 
                    orders.mark_finished(id)
                    print("Task marked as finished. \n")
                else:
                    print(f"id: {id}")
                    print(error_message)
            except ValueError:
                print(error_message)



        elif command == "5":
            print(f"command: {command}")
            for programmer in orders.all_programmers():
                print(programmer)
            print("")

        elif command == "6":
            print(f"command: {command}")
            programmer = input("Enter programmer: ")
            print(f"programmer: {programmer}")
            if programmer in orders.all_programmers():
                status = orders.status_of_programmer(programmer)
                print(f"programmer : {programmer}")
                print(f"tasks: finished: {status[0]} , not finished: {status[1]} , hours: done {status[2]} ,  scheduled {status[3]} \n")
            else:
                 print(error_message)

        else:
            print("Invalid command")
    