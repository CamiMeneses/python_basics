# Los decoradores tienen como argumento una funcion
# y retornan otra funcion

# Se toma una funcion y la modifica
def announce(f):
  def wrapper():
    print("About to run the function...")
    f()
    print("Done with the function.")
  return wrapper

@announce
def hello():
  print("Hello, world!")

hello()
