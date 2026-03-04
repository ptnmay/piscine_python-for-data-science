def all_thing_is_obj(object: any) -> int:
    ty = object.__class__
    if ty == list:
        print(f"List : {ty}")
    elif ty == tuple:
        print(f"Tuple : {ty}")
    elif ty == set:
        print(f"Set : {ty}")
    elif ty == dict:
        print(f"Dict : {ty}")
    elif ty == str:
        print(f"{object} is in the kitchen : {ty}")
    else:
        print("Type not found")
    return 42

"""
'.__class__' is an attribute of all obj in python, it's not a function

function is for do something. (verb)
attribute is value inside object. didn't do anything just show the value. (noun)
"""
