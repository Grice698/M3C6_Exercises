# Checkpoint 6

## ¿Para qué usamos Clases en Python?

En Python, una clase es similar a un plano que nos sirve para crear objetos y que proporciona propiedades e implementaciones de comportamiento (métodos). 

Ilustremos esto con una clase llamada Book. Digamos que eres un coleccionista de libros digitales y quieres organizar tus libros. Podrías hacer una tabla de Excel, pero también es posible almacenar tus libros en objetos en Python, y cada objeto tendría algunos atributos que son importantes de conocer. 

Primero, deberías crear el plano del objeto (la clase) y escribir al final dos puntos. Las clases en se escriben con mayúscula inicial por convención de estilo (según el __[PEP 8](https://peps.python.org/pep-0008/#class-names))__, no por una regla estricta del lenguaje. Esto es debido a que mejora la legibilidad, permitiendo diferenciar rápidamente entre clases y objetos/variables: 

```
class Book:
```

Una vez definida la clase, crearemos el método constructor \_\_init\_\_. Esto inicializa los atributos de cada clase. Continuaremos más adelante con el mismo ejemplo hasta completar nuestra clase Book así que no os preocupéis si la sintaxis resulta nueva.

#### Algunos aspectos a tener en cuenta sobre las clases:

* Algunas ventajas que nos ofrecen las clases en la programación serían, por un lado, la no repetición de código a lo largo de nuestro documento. Si las necesitásemos podríamos llamar a la clase que se usará una y otra vez en otros lugares. 

* No obstante, debemos considerar su implementación ya que puede complicar el código sin necesidad en según qué casos. Generalmente, si te encuentras escribiendo funciones dentro de funciones, deberías considerar escribir una clase en su lugar. Si solo tienes una función en una clase, quédate con solo escribir una función.  

Para más información sobre las clases en Python recomiendo indagar en la página de [documentación oficial.](https://docs.python.org/es/3/tutorial/classes.html)

--- 
## ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
Como acabamos de ver, se ejecutaría el término 'init'.
Esto se debe a que, en la programación orientada a objetos, nos centramos en los datos y el comportamiento. El comportamiento se gestiona mediante funciones, mientras que los datos se manejan de forma diferente. 

En Python, en particular, los datos se gestionan con una función constructora. Esto se hace escribiendo `def` seguido de `init`. 
La forma correcta de escribirlo es \_\_init_\_\, con dos guiones bajos al principio y al final. Como son dobles, los llaman __double underscore__ o __dunder__. Hablaremos de ellos más adelante.
Cabe mencionar que, el primer parámetro de \_\_init_\_\() es self, que representa la instancia actual de la clase. Se utiliza para acceder a los atributos y métodos de la instancia dentro del propio método y en otros métodos de la clase. Vamos a continuar con el ejemplo y a establecer los atributos uno por uno:

```
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
```

Ahora, instanciaremos los libros que queremos añadir a la colección creando una variable e introduciendo sus datos en orden. Aquí, book_one y book_two serían una instancia de la clase Book:
```
book_one = Book("1984", "George Orwell", "Dystopian")
book_two = Book("The Stranger", "Albert Camus", "Philosophical novel")


# Por último los imprimiremos para comprobar el resultado: 

print(f"{book_one.title} - {book_one.author}, {book_one.genre}")
print(f"{book_two.title} - {book_two.author}, {book_two.genre}")
```
> 1984 - George Orwell, Dystopian <br>
The Stranger - Albert Camus, Philosophical novel

Para más información, no dudes en consultar cualquiera de estos documentos:
+ https://www.luisllamas.es/constructores-en-python/ 
+ https://youtu.be/aXmiKgOc4pI

---

## ¿Cuáles son los tres verbos de API?
Los verbos HTTP indican la acción que se desea realizar sobre un recurso en una API. Estos verbos ayudan a las aplicaciones a comunicarse entre sí y cada uno comparte y manipula datos de manera específica.
Aquellos involucrados en un sistema REST son GET, POST, PUT, PATCH y DELETE:

-	GET se utiliza para consultar recursos, por ejemplo, podríamos hacer una solicitud para obtener todos los usuarios. Una de sus características principales es que no debe causar efectos secundarios en el servidor, producir nuevos registros ni modificar lo que ya estaba establecido. Cualquier cambio que hagamos en una petición GET, no establecerá ningún resultado diferente. A esta cualidad se le conoce como idempotencia.
-	POST se utiliza para crear nuevos recursos que se vayan a producir por primera vez. Al contrario que en las estructuras GET, pueden establecerse cambios al enviarse, pero puede crear duplicados. Algunos escenarios más complejos para el uso de POST son los inicios de sesión, agregar a un carrito de compras, procesar un pago nuevo, etc
-	PUT y PATCH son similares ya que ambos se utilizan para modificar o actualizar recursos existentes. PUT actualiza el recurso enviando todos sus atributos, mientras que PATCH podría modificar ciertos atributos específicos, como por ejemplo si necesitamos cambiar sólo el nombre de algún usuario de una aplicación.

-	DELETE se utiliza para borrar un recurso del servidor, o bien si necesitamos eliminar registros completos.

Si necesitas más información relevante, no dudes en hacer click en [esta publicación](https://www.actian.com/es/blog/data-intelligence/what-are-apis/) de Actian y este [vídeo explicativo](https://www.youtube.com/watch?v=OHBHeAPoZ8E&t=106s) sobre los verbos principales.


## ¿Es MongoDB una base de datos SQL o NoSQL?
Para entender de qué trata MongoDB, debemos tener una noción básica de lo que son las bases de datos. Estas son sistemas que permiten almacenar, organizar y gestionar información de manera eficiente para poder consultarla, modificarla y analizarla cuando sea necesario. Son una pieza fundamental en casi cualquier aplicación, ya que permiten guardar datos como usuarios, productos, pedidos o cualquier otro tipo de información relevante. 

Existen distintos tipos de bases de datos, pero una de las clasificaciones más importantes es entre bases de datos relacionales (SQL) y no relacionales (NoSQL). Elegir entre SQL y NoSQL dependerá de las necesidades del proyecto.

* Las bases de datos SQL, en inglés Structured query language, organizan la información en tablas con filas y columnas, y requieren un esquema fijo. Esto garantiza consistencia y facilita las consultas, pero también hace que sean menos flexibles ante cambios. 

* Por otro lado, las bases de datos NoSQL son sistemas de almacenamiento no relacionales, flexibles y distribuidos, diseñados para manejar grandes volúmenes de datos no estructurados. __MongoDB__ es una base de datos no relacional que está orientada a documentos y almacena la información en objetos similares a JavaScript. 

En MongoDB no tenemos exactamente el mismo tipo de nomenclatura que en SQL pero sí tenemos bases de datos. Dentro de estas tenemos lo que se llama colecciones. Las colecciones son la analogía más cercana a una tabla. Antes de poder empezar a guardar los documentos, necesitamos crear colecciones para almacenarlos. En Mongo, obtienes un objeto JSON de clave-valor, donde la clave es "ok" y un integer como 1

Así se vería una consulta en MongoDB en la que creamos una colección de libros:

![coleccion](https://github.com/Grice698/M3C6_Exercises/blob/1d647d9bbc712527a80d34443724a4139386fca3/markdown_images/Captura%20de%20pantalla%202026-04-01%20162010.png)
 
> La sintaxis de Mongo, tanto por cómo se escribe como por los valores que devuelve, es muy familiar a Javascript. Si estuvieras haciendo esto en un entorno de API y acabaras de crear una colección, podrías obtener este objeto y tratarlo como un JSON puro. 

Ahora podemos escribir ‘show collections’ y nos mostrará las colecciones que hemos creado: 

![resultado](https://github.com/Grice698/M3C6_Exercises/blob/1d647d9bbc712527a80d34443724a4139386fca3/markdown_images/Captura%20de%20pantalla%202026-04-01%20162105.png)

#### Ventajas y desventajas de usar MongoDB
*	Entre las ventajas de MongoDB destacan su flexibilidad, rapidez en el desarrollo, facilidad para escalar y buen rendimiento con grandes volúmenes de datos.

*	Sin embargo, hay una posible falta de consistencia si no se sigue una buena estructura. Hay mayor responsabilidad en el desarrollador y no siempre es la mejor opción para aplicaciones con muchas relaciones complejas.

La documentación oficial de [MongoDB](https://www.mongodb.com/es/resources/basics/databases/nosql-explained/nosql-vs-sql) añadirá toda la información que necesites si con estos apuntes no es suficiente. Además de eso, la [ESIC University](https://www.esic.edu/rethink/tecnologia/que-son-las-bases-de-datos-nosql-ejemplos-c) tiene una publicación muy interesante y formativa sobre las bases de datos y varios ejemplos. 

## ¿Qué es una API?
API constituye las siglas de Interfaz de Programación de Aplicaciones. Las API permiten conectar aplicaciones de forma sencilla y rápida. Gracias a ellas, los desarrolladores pueden usar funciones de otros sistemas sin necesidad de entender cómo están hechas por dentro. 
Un ejemplo muy práctico y del día a día: Cuando un usuario compra entradas para ir al cine a través de una página web. Este tiene que introducir sus datos bancarios, por lo que en ese momento interviene la API enviando dicha información a la entidad bancaria para comprobar que los datos son correctos y que se puede proseguir con la acción. Cuando la entidad le da el OK a la API, esta le pasa la información a la aplicación y se emite la entrada. En definitiva, facilitan que distintas aplicaciones trabajen juntas, mejorando la eficiencia. 
Además, permiten reutilizar código ya existente, lo que ahorra tiempo y dinero. Otro punto positivo es que se pueden hacer cambios en una API sin afectar a quienes la usan.
Por otro lado, como desventaja, depender de APIs externas puede ser un problema si fallan o cambian. También pueden requerir mantenimiento y control para evitar errores o problemas de seguridad.
En resumen, las API hacen el desarrollo más rápido y flexible, pero es importante usarlas con cuidado y control.

#### Recursos y Herramientas Recomendadas
También existen bibliotecas y herramientas muy útiles para el uso y creación de APIs como *flask* o *Django REST framework*. Adicionalmente, es útil familiarizarse con herramientas como *Postman* para probar APIs de una forma visual e interactiva. 

Otras bibliotecas destacadas serían *requests* y *httpx*. 
Si necesitas más documentación, los recursos proporcionados por [Datacamp](https://www.datacamp.com/es/tutorial/python-api), son excelentes puntos de partida para aprender sobre APIs y Python en general. También puedes consultar la [Introducción a las APIs web](https://developer.mozilla.org/es/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction) de MDN.


## ¿Qué es Postman?

[Postman](https://www.postman.com/) es una aplicación muy útil que nos permite leer y estructurar APIs desarrolladas externamente de manera legible y sencilla. Postman nos permite enviar solicitudes HTTP a sus API, observar las respuestas y colaborar con otros miembros del equipo en el desarrollo de API. Como hemos mencionado antes, una API es un servicio similar a un sitio web o servidor con el que puedes comunicarte, pero en lugar de recibir una página web, recibes datos. 

En el caso de Postman, esta funciona independientemente del tipo de proceso que estés realizando, ya que no está limitado a un lenguaje de programación, un framework ni nada por el estilo. Es decir, al desarrollar una aplicación API con Flask, o una aplicación con React, es posible usar Postman para todas ellas porque solo se ocupa de la solicitud de datos.

![Pantallazo de Postman en un entorno POST](https://support.travelport.com/webhelp/JSONAPIs/Airv6/Content/Resources/Images/postman/postman_samples.png)
> Pantallazo de Postman en un entorno POST con una colección a la izquierda. Después de importar una colección, debes [configurar un entorno](https://support.travelport.com/webhelp/JSONAPIs/Airv6/Content/GeneralProject/UsingPostman.htm#environ) antes de poder ejecutar los datos.

Si te interesa iniciarte en Postman y saber cómo instalarlo, la [guía web](https://learning.postman.com/docs/getting-started/overview) facilita muchos datos al respecto.

## ¿Qué es el polimorfismo?
El polimorfismo es la capacidad de un objeto para responder al mismo según el contexto y comportarse de manera distinta. Polimorfismo es un término compuesto en el que *poli* significa muchos y *morfo* significa formas. Esto significa que podemos llamar a un método exactamente igual a otro y el intérprete automáticamente detectará a cual de ellos nos referimos.
En Python, esto se logra a través del [__“duck typing”__](https://realpython.com/duck-typing-python/#duck-typing-and-polymorphism), lo que significa que el funcionamiento de un objeto se determina por su comportamiento, en lugar de su tipo específico. 

Podemos crear un ejemplo con polimorfismo y herencia en una clase llamada Ave. Por otro lado, crearemos otras dos clases (Pato y Pollito) que heredarán el comportamiento de la anterior, e implementarán el método ruido() de forma diferente:

```
class Ave: # Clase padre
    def __init__(self, nombre):
        self.nombre = nombre

    def ruido(self):
    print("El ave hace un sonido")


# Clase hija 1
class Pato(Ave):
    def ruido(self):
        print(self.nombre + " dice: Cuac cuac")


# Clase hija 2
class Pollito(Ave):
    def ruido(self):
        print(self.nombre + " dice: Pío pío")


# Programa principal
ave1 = Pato("Donald")
ave2 = Pollito("Piolín")

ave1.ruido()
ave2.ruido()
```
> Donald dice: Cuac cuac <br> Piolín dice: Pío pío

#### Buenas prácticas en la implementación del polimorfismo

-	Estas requieren seguir un conjunto de principios de diseño para evitar errores.
-	En primer lugar, es necesario programar por comportamientos y no para tipos concretos, es decir, el código debe interactuar con interfaces abstractas definidas por comportamientos esperados. Esto reduce el acoplamiento entre componentes, y permite la integración de nuevos tipos sin la necesidad de modificar el código existente.
-	Uno de los aspectos más importantes a tener en cuenta es que las interfaces deben ser coherentes. Los métodos polimórficos deben ser consistentes y uniformes entre si. Se debe respetar no solo el nombre y parámetros del mismo, sino también su funcionalidad, pre-condiciones y post-condiciones. 
-	Se deben evitar herencias de más de tres niveles ya que aumentan la complejidad y reducen la claridad del código. El uso de [mixins](https://juncotic.com/poo-herencia-en-python/#htoc-herencia-m-ltiple) es recomendado para reutilizar comportamiento sin crear jerarquías. 

Para más documentación, os aconsejo leer este post de [Factoriacreativa](https://www.factoriacreativabarcelona.es/blog/que-es-polimorfismo-en-python/#h2_toc_3) y la siguiente publicación de [Luis Llamas](https://www.luisllamas.es/polimorfismo-en-python/)



## ¿Qué es un método dunder?

Los métodos Dunder son aquellos que especifican el comportamiento de los objetos y se definen como parte de la clase del objeto.  Dado que forman parte de la clase del objeto, toman como primer argumento 'self', que es una referencia al propio objeto.  

Comienzan y terminan con doble guion bajo y tienen nombres como `init` (tal y como hemos visto en anteriore ejemplos). Si eres relativamente nuevo en Python o en la programación en general, esta sintaxis puede parecerte extraña. 

Esto se debe a cómo Python maneja los métodos privados y protegidos dentro de sus clases. En muchos otros lenguajes de programación, no es necesario usar esta estructura. Debido a que los métodos dunder son privados y protegidos, recibirías una advertencia si intentaras hacer algo como usar `def` seguido de mayúsculas, que indicaría que parece que estás intentando sobrescribir un método integrado y no deberías hacerlo, ya que podría provocar que otras partes del programa se comporten de forma inesperada. No se utilizan estos guiones bajos, ya que cuentan con métodos privados. En Python, en cambio, estos métodos están integrados de base.



| Método | ¿Qué hace? |
|--------------|--------------|
| \_\_init\_\_       | Inicializa una nueva instancia de clase       |
|  \_\_str\_\_      | Devuelve una string de un objeto       |
|  \_\_iter\_\_      | Devuelve un iterador para el objeto       | 
|  \_\_next\_\_      | Devuelve el siguiente elemento del iterador       | 
|  \_\_repr\_\_      | Proporciona detalles técnicos para identificar problemas en el código       | 
|  \_\_len\_\_      | Permite devolver la longitud de un objeto       | 
|  \_\_getitem\_\_      | Permite acceder a elementos mediante índices       | 
|  \_\_setitem\_\_      | Permite asignar valores a elementos mediante índices       | 
|  \_\_delitem\_\_      | Permite eliminar valores mediante índices       |  


Vamos a crear un ejemplo breve utilizando el método mágico \_\_len\_\_. El objetivo es obtener la longitud de una instancia de una clase, en este caso una lista: 

```
class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

lista = Lista([1, 2, 3, 4])
print(len(lista))
```
> Salida: 4 

Para más información útil, recomiendo el [siguiente enlace](https://geekflare.com/es/magic-methods-in-python/). Además, si os interesa aprender sobre métodos dunder menos convencionales, hacer click [aquí](https://www.geeksforgeeks.org/python/dunder-magic-methods-python/)

----

## ¿Qué es un decorador de python?
Un decorador es un código que se puede usar para envolver métodos o clases y, tomando otra función como argumento, ayuda a modificarlas y les añaden funcionalidades (las decoran) sin necesidad de alterar su código. Los decoradores empiezan con un @ seguido del nombre de la función decoradora. Se colocan encima de la definición de la función o clase, así que cuando se llama, esta función se ejecuta primero. 

Ya que es difícil de visualizar sin un ejemplo, vamos a crear una función sencilla que 'gritará' convirtiendo las frases en mayúsculas:

```
# Definimos el decorador
def gritar(funcion):
    def modificar():
        return funcion().upper()  # convierte a MAYÚSCULAS
    return modificar

# Usamos el decorador
@gritar
def mensaje():
    return "¡me duele la cabeza!"

print(mensaje())
```
> Salida: ¡ME DUELE LA CABEZA!

Hay que tener en cuenta que los decoradores devuelven una versión modificada de esa función o clase, no la exacta misma función a la que nos referimos. Por lo tanto, tendrán otro ID. Los decoradores pueden apilarse/anidarse, lo que significa que pueden aplicarse varios decoradores a una misma función o clase. Como curiosidad, los decoradores también se pueden aplicar a métodos de clase y métodos estáticos en Python.

Para más información no dudes en consultar este artículo de [Anesu Kafesu](https://geekflare.com/es/python-decorators/) y el [Libro de Python](https://ellibrodepython.com/decoradores-python) que indaga en el tema.

