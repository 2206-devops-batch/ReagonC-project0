import sys
import pandas

class ShoppingStoreProgram:

    def interface(self): 
        print("Please select which department you would like to shop in.")
        print("Enter 1 for clothing department.")
        print("Enter 2 for pets department.")
        print("Enter 3 for electronics department.")
        print("Enter 0 to leave Shopping Store.")


    def start(self):
        print("Welcome to Shopping Store!")
        self.interface()


        list = []
        cost_list = []
        total = 0
        while True:
            selection = input()
            if selection == '1':
                clothing_department = ClothingDepartment("Clothing Department")
                print("Welcome to the " + clothing_department.get_name())
                print(clothing_department.get_clothing_list())
                print("Which items you would like to purchase? Type ok to shop in other departments.")
                while True:
                    item_selection = input()
                    for item in clothing_department.get_clothing_list():
                        if(item_selection == item):
                            list.append(item_selection)
                            cost_list.append(clothing_department.get_clothing_list()[item_selection])
                            total +=  clothing_department.get_clothing_list()[item_selection]
                            
                            print("Your current shopping cart:")
                            print(list)
                    if(item_selection == 'ok'):
                        self.interface()
                        break;
            elif selection == '2':
                pet_department = PetDepartment("Pet Department")
                print("Welcome to the " + pet_department.get_name())
                print(pet_department.get_pet_list())
                print("Which items you would like to purchase? Type ok to shop in other departments.")
                while True:
                    item_selection = input()
                    for item in pet_department.get_pet_list():
                        if(item_selection == item):
                            list.append(item_selection)
                            cost_list.append(pet_department.get_pet_list()[item_selection])
                            total +=  pet_department.get_pet_list()[item_selection]
                            
                            print("Your current shopping cart:")
                            print(list)
                    if(item_selection == 'ok'):
                        self.interface()
                        break;
            elif selection == '3':
                electronics_department = ElectronicsDepartment("Electronics Department")
                print("Welcome to the " + electronics_department.get_name())
                print(electronics_department.get_electronics_list())
                print("Which items you would like to purchase? Type ok to shop in other departments.")
                while True:
                    item_selection = input()
                    for item in electronics_department.get_electronics_list():
                        if(item_selection == item):
                            list.append(item_selection)
                            cost_list.append(electronics_department.get_electronics_list()[item_selection])
                            total +=  electronics_department.get_electronics_list()[item_selection]
                            
                            print("Your current shopping cart:")
                            print(list)
                    if(item_selection == 'ok'):
                        self.interface()
                        break;
            elif selection == '0':
                print("Leaving Shopping Store. Thank You!")
                list.append('Total: ')
                cost_list.append(str(total))
                df = pandas.DataFrame(data={"Product": list, "Price": cost_list})
                df.to_csv("./file.csv", sep=',',index=False)
                break
            else:
                print("That is not a vaild selection.")

        return 0

class Department:

    __name = None

    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

class ClothingDepartment(Department):

    __clothing_list = {
        "Shirts": 15,
        "Pants": 20,
        "Sweatshirts": 36,
        "Jackets": 27
    }

    def __init__(self, name):
        super().__init__(name)


    def get_clothing_list(self):
        return self.__clothing_list

class PetDepartment(Department):

    __pet_list = {
        "DogFood": 60,
        "CatFood": 60
    }

    def __init__(self, name):
        super().__init__(name)


    def get_pet_list(self):
        return self.__pet_list

class ElectronicsDepartment(Department):

    __electronics_list = {
        "iPhone": 999,
        "Laptop": 400,
        "Headphones": 50
    }

    def __init__(self, name):
        super().__init__(name)


    def get_electronics_list(self):
        return self.__electronics_list


def item_count_in_departments(first, second, thrid):
    return first + second + thrid

def main():
    shopping_store_program = ShoppingStoreProgram()
    shopping_store_program.start()
    return 0


main()