def print_result(func):
    def decorated_func(*args):
        if len(args) == 0:
            result = func()
        else:
            result = func(args[0])
        print(func.__name__)
        if type(result) == list:
            for i in result:
                print(i)
        elif type(result) == dict:
            for key in result:
                print(str(key) + " = " + str(result[key]))
        else:
            print(result)
        return result

    return decorated_func
