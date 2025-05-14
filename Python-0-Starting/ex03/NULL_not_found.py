import math

def NULL_not_found(object: any) -> int:

    if object is None:
        print(f"Nothing: {object}")
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object}")
        return 0
    elif object == 0:
        print(f"Zero: {object}")
        return 0
    elif object == '':
        print(f"Empty: {object}")
        return 0
    elif object is False:
        print(f"Fake: {object}")
        return 0
    else:
        print("Type not Found")
        return 1