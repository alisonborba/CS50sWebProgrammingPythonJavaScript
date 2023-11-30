def announce(f):
    def wrapper():
        print("start wrapper function")
        f()
        print("finised wrapper function")
    return wrapper

@announce
def hello():
    print("hello")

hello()