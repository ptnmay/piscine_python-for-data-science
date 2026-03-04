def NULL_not_found(object: any) -> int:
    ty = object.__class__
    if object is None:
        print(f"Nothing: None {ty}")
        return 0
    elif object != object:
        print(f"Cheese: nan {ty}")
        return 0
    elif object is False:
        print(f"Fake: False {ty}")
        return 0
    elif object == 0:
        print(f"Zero: 0 {ty}")
        return 0
    elif object == "":
        print(f"Empty: {ty}")
        return 0
    else:
        print("Type not Found")
        return 1

"""
'.__class__' is an attribute of all obj in python, it's not a function

function is for do something. (verb)
attribute is value inside object. didn't do anything just show the value. (noun)

NaN (Not a Number) is value that we don't know.
NaN != Nan is true because we nerver know is it itself. behavior by IEEE.
"""
