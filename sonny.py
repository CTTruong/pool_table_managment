class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = []


    def print_contact_info(self):
        print("Sonny's email: sonny@hotmail.com, Sonny's phone number: 483-485-4948")





    def greet(self, other_person):
        print ("Hello {0}, I am {1}".format(other_person.name, self.name))




Sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456" )

print(Sonny.email, Sonny.phone)
Sonny.print_contact_info()
Sonny.friend.append(Jordan)
Sonny.greet(Jordan)
print(len(Sonny.friend))


print(Jordan.email, Jordan.phone)
Jordan.friends.append(Sonny)
Jordan.greet(Sonny)
print(len(Jordan.friend))


class Vehicle:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("2015", "Nissan", "Leaf")



car = Vehicle("Nissan", "Leaf", "2015")
print (car.make, car.model, car.year)
car.print_info()
