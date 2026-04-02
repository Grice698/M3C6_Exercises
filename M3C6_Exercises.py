"""
Cree una clase de Python llamada Usuario que use 
el método init y cree un nombre de usuario y una contraseña. 
Crea un objeto usando la clase.
"""

class Usuario:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        
usuario1 = Usuario('John', 'contraseñ4')
print(f'User name: {usuario1.name}, password: {usuario1.password}')

