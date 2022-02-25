import random

class Vehicle:
    """Defines a vehicle with its id."""

    def __init__(self, vehiclNo, isAvailable=True):
        """
        Takes vehicle id and
        controls availability.
        """
        self.vehiclNo = vehiclNo
        self.isAvailable = isAvailable


class LogisticSystem:
    """Controls operations with orders."""

    def __init__(self, vehicles):
        """
        Takes a list of orders
        and assigned vehicle
        """
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order):
        """
        Assigns transport for order
        """

        self.orders.append(order)
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                order.assignVehicle(vehicle)
                vehicle.isAvailable = False
                return f"{vehicle} is ready to go."
        print("There is no available vehicle to deliver an order.")

    def trackOrder(self, orderID):
        """
        Tracks user's order.

        """
        for order in self.orders:
            if order.order_id == orderID:
                return f"Your order #{order.order_id} is sent to {order.location.city}. Total price: {order.calculateAmount()} UAH."
        print("No such order!")


class Item:
    """Defines an item"""

    def __init__(self, name, price):
        """Takes item's name and price."""
        self.name = name
        self.price = price


class Order:
    """Defines an order"""

    def __init__(self, user_name, city, postoffice, items):
        """
        Takes order's location, items,
        who did that order and
        gives order unique id.
        """
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.order_id = random.randint(0, 100000)

    def __str__(self):
        """
        User-friendly order message
        """
        return f"Your order number is {self.order_id}."

    def assignVehicle(self, vehicle):
        """Assigns vehicle to order."""
        self.vehicle = vehicle

    def calculateAmount(self):
        """Calculates total price of order."""
        total = 0
        for item in self.items:
            total += item.price

        return total


class Location:
    """Defines location of order"""

    def __init__(self, city, postoffice):
        """
        Takes order's city and postoffice.
        """
        self.city = city
        self.postoffice = postoffice


if __name__ == "__main__":
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order(user_name='Oleg', city='Lviv', postoffice=53, items=my_items)
    print(my_order)
    logSystem.placeOrder(my_order)
    print(logSystem.trackOrder(logSystem.orders[0].order_id))

    my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    print(my_order2)
    logSystem.placeOrder(my_order2)
    print(logSystem.trackOrder(logSystem.orders[1].order_id))

    my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]
    my_order3 = Order("Olesya", 'Kharkiv', 17, my_items3)
    print(my_order3)
    logSystem.placeOrder(my_order3)
    logSystem.trackOrder(485932990)
