class Vector:

    def __init__(self, array):
        self.array = array

    def equals(self, another_vector):
        if len(self.array) == len(another_vector.array):
            for i in range(len(self.array)):
                if self.array[i] != another_vector.array[i]:
                    return False
            return True
        return False

    def add(self, another_vector):
        if len(self.array) == len(another_vector.array):
            after_add = []
            for i in range(len(self.array)):
                after_add.append(self.array[i] + another_vector.array[i])
            return Vector(after_add)
        else:
            return False

    def subtract(self, another_vector):
        if len(self.array) == len(another_vector.array):
            after_sub = []
            for i in range(len(self.array)):
                after_sub.append(self.array[i] - another_vector.array[i])
            return Vector(after_sub)
        else:
            return False

    def dot(self, another_vector):
        if len(self.array) == len(another_vector.array):
            suma = 0
            for i in range(len(self.array)):
                suma += self.array[i] * another_vector.array[i]
            return suma
        else:
            return False

    def norm(self):
        suma = 0
        for i in self.array:
            suma += i ** 2
        return suma ** 0.5
    
    def __str__(self):
        string = ""
        for i in self.array:
            string += str(i) + ','
        return f'({string[0:-1]})'
