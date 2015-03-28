class Parent(object):
    """ Class about parents """

    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye Color - {}".format(self.eye_color))

class Child(Parent):
    """ A Child class that inherits from Parent class """

    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        super(Child, self).__init__(last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye Color - {}".format(self.eye_color))
        print("Number of Toys - {}".format(self.number_of_toys))

p = Parent("Lant", "Hazel")
p.show_info()
c = Child("Smith-Lant", "Brown", "100")
c.show_info()

