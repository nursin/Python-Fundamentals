class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        return self.items

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor in self.flavors and scoops >= 1 and scoops <= 3:
            print("Order created!")
        elif flavor not in self.flavors:
            print("Flavor must be from list")
        elif scoops < 1 and scoops > 3:
            print("Scoops must be between 1 - 3")
        else:
            print("You entered an invalid response")
        
        order = {customer: customer, flavor: flavor, scoops: scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("All pending orders!")
        all_orders = self.orders.show_queue()
        for i in range(0, len(all_orders) - 1):
            print(all_orders[i])
        print("\n")

    def next_order(self):
        print("Next order up!")
        print(self.orders.dequeue())
        print("\n")



shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
print("\n")
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()