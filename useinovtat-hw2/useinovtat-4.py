# helper function to check for a sausage party
def is_sausages(product):
    if len(product) == 6:
        if product[0] == '[' and product[5] == ']':
            if product[1]*4 == product[1:5]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# main func
def unpack_sausages(truck):
    is_reward = 1
    is_first = 1
    unpacking = []
    answer = ""

    for box in truck:
        box = list(box)
        while box:
            product = box.pop(0)
            if is_sausages(product):
                unpacking.append(product)

    for pack in unpacking:
        if is_reward % 5 != 0:
            for sausage in pack[1:-1]:
                if is_first:
                    answer += sausage
                    is_first = 0
                else:
                    answer += " "
                    answer += sausage
        is_reward += 1

    return answer
