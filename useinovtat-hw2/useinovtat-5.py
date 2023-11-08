def get_root_property(object, value):
    if type(object) != dict:
        for i in object:
            if i == value:
                return 1
        return None
    else:
        for key in object:
            if get_root_property(object.get(key), value):
                return key
        return None
