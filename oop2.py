class Fruit :
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"I like eating {self.name}. Each costs {self.price}.")

fruit1 = Fruit("apples", "30 shillings")
fruit2 = Fruit("mangoes", "50 shillings")
fruit3 = Fruit("oranges", "20 shillings")
fruit4 = Fruit("pineapples", "150 shillings")
fruit5 = Fruit("pears", "45 shillings")

fruit1.display()
fruit2.display()
fruit3.display()
fruit4.display()
fruit5.display()