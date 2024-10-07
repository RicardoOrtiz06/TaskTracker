class MyClass:
    def __init__(self, name):
        self.name = name  # 'self.name' es un atributo del objeto, y se le asigna el valor del parámetro 'name'

    def greet(self):
        print(f'Hello, {self.name}!')  # Aquí, 'self.name' accede al atributo 'name' del objeto

# Creando una instancia de MyClass
obj = MyClass('Alice')  # 'obj' es una instancia de MyClass con 'name' igual a 'Alice'
obj2 = MyClass('Ricardo')

obj.greet()  # Llama al método greet, que usa 'self.name' para imprimir 'Hello, Alice!'
obj2.greet()