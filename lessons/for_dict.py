"""Practicing with Dictionaries and for Loops"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples":True }
for key in in_stock:
    #key is going to be "carrots","beets","apples"
    #iin_stock[key] is going to be True, False, True
    value: bool = in_stock[key]
    if value:
        print(key)

def invert(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            raise KeyError("Encountered duplicate value while inverting the dictionary")
        inverted_dict[value] = key
    return inverted_dict


   