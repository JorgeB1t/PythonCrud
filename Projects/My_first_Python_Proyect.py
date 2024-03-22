import sqlite3
from getpass import getuser

# Programar una app que me permite crear un estudiante, editarlo, eliminarlo, buscarlo y mostrar todos.
# Para ello hay que crear una BBDD sqlite con las columnas id (primary key), asignatura, nombre y teléfono: por ejemplo:
# CREATE TABLE IF NOT EXISTS student(
#    id INTEGER PRIMARY KEY,
#    subject TEXT,
#    name TEXT,
#    phone TEXT)


# funcion para insertar datos en la tabka
def insert_into_table(id, subject, name, phone):
    query = f"INSERT INTO student VALUES('{int(id)}','{subject}','{name}','{phone}')"
    return cur.execute(query)


# metodo que hace la peticion al usuario
def peticion_user():
    print(f"Bienvenido a mi aplicación {getuser()}")
    print("¿Qué quiere hacer?")
    peticion = input(
        "1. Crear un estudiante \n"
        "2. Editar un estudiante \n"
        "3. Eliminar un estudiante \n"
        "4. Buscar a un estudiante \n"
        "5. Mostrar a todos los estudiantes\n"
        "6. Salir\n"
        "(Ingrese el identificador del indice)\n"
    )

    return int(peticion)


# metodo para verificar la existencia de los alumnos
def name_exits():
    cur.execute("SELECT name FROM student")
    names = [i[0] for i in cur.fetchall()]
    return names


# metodo para insertar los datos inciales en la tabla

"""def insert_initial_data():
    insert_into_table("1", "English", "Oscar Arroyo", "123456789")
    insert_into_table("2", "Math", "Luis Antonio", "234567891")
    insert_into_table("3", "Technology", "Daniel Martín", "345678912")
    insert_into_table("4", "Biology", "Jorge Gallego", "456789123")
    insert_into_table("5", "Music", "Alonso Morenas", "567891234")
    insert_into_table("6", "History", "Eloy Ojeda", "678912345")"""


# metodo para ingresar a un estudiante
def insert_student():

    id = int(input("Ingrese el id.\n"))
    subject = input("Ingrese la asignatura del estudiante.\n")
    name = input("Ingrese el nombre del estudiante.\n")
    phone = int(input("Ingrese el numero del estudiante.\n"))
    insert_into_table(id, subject, name, phone)
    con.commit()


# metodo para editar a un estudiante
def edit_student():
    nombres_exist = name_exits()
    o_name = input("Ingresa el nombre original:\n")

    if o_name in nombres_exist:
        n_name = input("Ingresa el nuevo nombre:\n")
        cur.execute(
            "UPDATE estudiante SET nombre = ? WHERE nombre = ?", (n_name, o_name)
        )
        con.commit()
    else:
        print("Nombre no encontrado")


# metodo para eliminar a un estudiante
def delete_stuent():
    nombres_exist = name_exits()
    name = input("Que estudiante quiere eliminar?\n")
    if name in nombres_exist:
        cur.execute("DELETE FROM student WHERE name = ?", (name,))
        con.commit()
    else:
        print("Nombre no encontrado")


# metodo para buscar a un estudiante
def select_student():
    nombres_exist = name_exits()
    name = input("Dime el nombre del estudiante \n")
    if name in nombres_exist:
        res = cur.execute(f"SELECT * FROM student WHERE name = '{name}'")
        print(res.fetchone())
    else:
        print("Nombre no encontrado")


# metodo para mostrar a todos los estudiantes
def select_all():
    res = cur.execute("SELECT * FROM student")
    dataFile = res.fetchall()
    for i in dataFile:
        print(i)


con = sqlite3.connect("students.db")
cur = con.cursor()

cur.execute("PRAGMA SERIALIZABLE = true;")
# Creacion de la tabla con las columnas correspondientes
cur.execute(
    "CREATE TABLE IF NOT EXISTS student(id INTEGER auto_increment PRIMARY KEY,subject TEXT,name TEXT,phone TEXT)"
)


# ============================================================Interaccion con el usuario========================================================================


peticion = peticion_user()


while peticion != 6:
    if peticion == 1:
        peticion = 0
        insert_student()
    elif peticion == 2:
        peticion = 0
        edit_student()
    elif peticion == 3:
        peticion = 0
        delete_stuent()
    elif peticion == 4:
        peticion = 0
        select_student()
    elif peticion == 5:
        peticion = 0
        select_all()
    elif peticion == 6:
        con.close()
        break
    else:

        peticion = peticion_user()
