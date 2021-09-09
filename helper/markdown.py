from functools import wraps

def markdown(type):
    def inner_function(function):
        @wraps(function)
        def wrapper(entry):
            if type == "subtitle":
                return function('##' + entry)
            elif type == "unordered-list":
                return function('- ' + entry)
            elif type == "script":
                return function('\n~~~~\n' + entry + '\n~~~~\n')
            # unlike the others needs to be a list with len = 3
            elif type == "table-entry" and type(entry) == list:
                return function("| " + entry[0] + " | " + entry[1] + " | " + entry[2] + " | \n")
        return wrapper
    return inner_function

if __name__ == "__main__":
    @markdown(type="subtitle")
    def f(text):
        print(text)

    f('larissa')
