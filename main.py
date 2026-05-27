import shape_manager


def add_shape(shape):
    SHAPEMANAGER.create_shape(shape)


def show_all_shapes():
    pass


def update_shape():
    pass


def delete_shape():
    pass


def menu():
    print("to add shape enter 1\n"
          "to show all shapes enter 2\n"
          "to update shape enter 3\n"
          "to delete sape enter 4\n"
          "to exit enter 5")


def main():
    SHAPEMANAGER = shape_manager.ShapeManager()
    flag = True
    while flag:
        menu()
        if 1:
            add_shape()
        elif 2:
            show_all_shapes()
        elif 3:
            update_shape()
        elif 4:
            delete_shape()

        elif 5:
            flag = False
        else:
            pass