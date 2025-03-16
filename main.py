if __name__ == "__main__":

    from classes import * 
    
    print(" \nTEST 1\n")
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)



    print(" \nTEST 2\n")
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practicing mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.all_programmers():
        print(programmer) 

    

    print(" \nTEST 3\n")
    orders.add_order("program mobile app for woorkload accounting", "Adele", 25)
    orders.mark_finished(4)
    orders.mark_finished(7)

    for order in orders.all_orders():
        print(order)


    print(" \nTEST 4\n")
    status = orders.status_of_programmer("Adele")
    print(status)


    print(" \nTEST 5\n")
    manage_orders()