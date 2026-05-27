from shape_manager import ShapeManager


def get_shape_params_():
    user_input=input("enter shape param(if more ten 1, add spase!):")
    return tuple(user_input.split())


def add_shape(manager_class):
    shape = input("enter shape: ")
    param_s = get_shape_params_()
    manager_class.create_shape(shape, param_s)


def show_all_shapes():
    pass


def update_shape():
    pass


def delete_shape():
    pass


def menu():
     return input("to add shape enter 1\n"
          "to show all shapes enter 2\n"
          "to update shape enter 3\n"
          "to delete sape enter 4\n"
          "to exit enter 5\n: ")


def main():
    SHAPEMANAGER = ShapeManager()
    flag = True

    while flag:
        user_input = menu()
        if user_input == "1":
            add_shape(SHAPEMANAGER)
        elif user_input == "2":
            show_all_shapes()
        elif user_input == "3":
            update_shape()
        elif user_input == "4":
            delete_shape()

        elif user_input == "5":
            flag = False
        else:
            pass