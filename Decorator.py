# Basicamente permite meter una funcion dentro de otra, permitiendo agregar cosas antes y despues de correrla

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the Function")
    return wrapper

@announce #Simplemente se pone arriba de la funcion
def hello():
    print(Hello World!"")

#------------------

hello()
