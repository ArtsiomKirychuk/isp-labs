bool_variable = True
int_variable = 102
float_variable = 13.37
string = "hello"
lst = [0, 23.4, "hello", False]
dct = {"key1": 111, "key2": 222}


def func_simple(a, b):
    return a + b


def func_with_default(a=9, b=8):
    return a - b


def func_recursive(n):
    if n > 0:
        return func_recursive(n - 1)
    else:
        return 1


def func_with_tuple(a, b):
    a *= b
    return a, b


def func_with_set(a, b):
    a /= b
    return {a, b}


class Class1:
    a = 10

    def class_method(self):
        print(self.a)


class ClassWithStaticMethod:
    @staticmethod
    def static_method():
        print("nice")