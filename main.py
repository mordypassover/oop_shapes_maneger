from shape_manager import ShapeManager, logger


def get_shape_params():
    user_input = input("enter shape param (if more than 1, add space!): ")

    try:
        user_params = tuple(int(num) for num in user_input.split())
        return user_params

    except ValueError:
        logger.error("param not a number!")



def add_shape(manager_class):
    shape = input("enter shape ( square, circle, rectangle): ")
    param_s = get_shape_params()
    if param_s is not None:
        manager_class.create_shape(shape, param_s)


def show_all_shapes(manager_class):
    print(manager_class.show_shapes_as_dicts())


def update_shape(manager_class):
    id_to_update = int(input("enter id to update: "))
    new_param_s = get_shape_params()
    if new_param_s is not None:
        manager_class.update_shape(id_to_update, new_param_s)


def delete_shape(manager_class):
    id_to_remove = int(input("enter id to remove: "))
    manager_class.delete_shape(id_to_remove)


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
            show_all_shapes(SHAPEMANAGER)
        elif user_input == "3":
            update_shape(SHAPEMANAGER)
        elif user_input == "4":
            delete_shape(SHAPEMANAGER)

        elif user_input == "5":
            flag = False
        else:
            logger.warning("user entered bad input")
        SHAPEMANAGER.save_to_json()
    logger.info("run ended")


if __name__ == "__main__":
    main()