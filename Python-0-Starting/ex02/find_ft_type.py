def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List :")
    elif isinstance(object, tuple):
        print("Tuple :")
    elif isinstance(object, set):
        print("Set :")
    elif isinstance(object, dict):
        print("Dict :")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen :")
    else:
        print("Type not found")
    
    return 42