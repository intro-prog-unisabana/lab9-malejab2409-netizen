[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SniAAGoq)
# Laboratorio 9

---

## Pregunta 1 — Clase `Song` básica

**Archivo a modificar:** `song.py`

Crea una clase llamada `Song` que cumpla las siguientes especificaciones.

### Atributos

| Atributo | Tipo    | Descripción                        |
|----------|---------|------------------------------------|
| `name`   | `str`   | El título de la canción            |
| `artist` | `str`   | El nombre del artista              |
| `length` | `float` | La duración de la canción en minutos |

### Métodos

#### `__init__(self, name, artist, length)`

Inicializa un nuevo objeto `Song` con los valores proporcionados.

#### `get_length_in_seconds(self)`

Devuelve la duración de la canción convertida de minutos a segundos.

**Ejemplo:**

```python
my_song = Song("tv off", "Kendrick Lamar", 3.7)
print(my_song.get_length_in_seconds())
```

```
222.0
```

---

## Pregunta 2 — Método `__str__` en la clase `Movie`

**Archivo a modificar:** `movie.py`

Se te proporciona una clase `Movie` que ya tiene un constructor. Tu tarea es definir el método `__str__` para que al imprimir un objeto `Movie`, muestre una descripción formateada de la película.

### Instrucciones

1. Define el método `__str__` dentro de la clase `Movie`. Debe retornar una cadena con el siguiente formato:

   ```
   Movie: <title> (Directed by <director>, <year>)
   ```

2. Crea un objeto `Movie` a partir de la entrada del usuario.
3. Imprime el objeto usando `print()`, lo cual llamará a tu método `__str__` automáticamente.

---

## Pregunta 3 — Clase `Song` expandida y función `print_songs`

> **Nota:** Esta pregunta expande el trabajo de la Pregunta 1. Actualiza `song.py` con el nuevo método y crea el archivo `practice.py` desde cero.

**Archivos a modificar:** `song.py` (actualizar), `practice.py` (crear)

### Parte 3a — Actualizar `song.py`

Agrega el método `__str__` a la clase `Song` que ya creaste en la Pregunta 1.

#### `__str__(self)`

Devuelve una cadena con el siguiente formato:

```
'<name>' by <artist> (<length>)
```

> **Nota:** No usarás `get_length_in_seconds()` en esta pregunta.

### Parte 3b — Crear `practice.py`

En `practice.py`, haz lo siguiente:

1. Importa la clase `Song` desde `song.py`.
2. Crea una función llamada `print_songs(song_list)` que reciba una lista de objetos `Song` e imprima cada uno.

**Ejemplo:**

```python
from song import Song

def print_songs(song_list):
    for song in song_list:
        print(song)

songs = [
    Song("tv off", "Kendrick Lamar", 3.7),
    Song("Alright", "Kendrick Lamar", 3.5)
]

print_songs(songs)
```

**Salida esperada:**

```
'tv off' by Kendrick Lamar (3.7)
'Alright' by Kendrick Lamar (3.5)
```

---

## Pregunta 4 — Sistema de gestión de autos

**Archivos a modificar:** `car.py` (crear), `car_utils.py` (crear), `overall.py` (completar)

El objetivo es modelar vehículos con una clase `Car`, apoyarte en funciones auxiliares definidas en `car_utils.py`, y completar un programa interactivo en `overall.py`.

---

### Parte 4a — Definir la clase `Car` en `car.py`

#### Atributos

| Atributo  | Tipo    | Descripción                            |
|-----------|---------|----------------------------------------|
| `car_id`  | `str`   | Identificador único (ej. `"CAR001"`)   |
| `brand`   | `str`   | Marca del fabricante (ej. `"Toyota"`)  |
| `year`    | `int`   | Año de fabricación                     |
| `color`   | `str`   | Color del auto                         |
| `mileage` | `float` | Kilómetros recorridos. Por defecto: `0.0` |

#### Métodos

- **`__init__(self, car_id, brand, year, color, mileage=0.0)`** — Inicializa todos los atributos.
- **`change_color(self, new_color)`** — Actualiza el color del auto.
- **`drive(self, miles)`** — Incrementa el kilometraje en `miles`.
- **`__str__(self)`** — Devuelve una descripción con el siguiente formato:

  ```
  CAR001 - 2020 Red Toyota with 15000.0 miles
  ```

---

### Parte 4b — Revisar las funciones auxiliares en `car_utils.py`

Este archivo ya está escrito. Léelo con atención antes de usarlo en `overall.py`.

```python
from car import Car

def create_car_from_input():
    car_id = input("Enter car ID (e.g., CAR001):\n")
    brand = input("Enter car brand:\n")
    year = int(input("Enter car year:\n"))
    color = input("Enter car color:\n")
    mileage = float(input("Enter mileage:\n"))
    return Car(car_id, brand, year, color, mileage)

def display_cars(car_dict):
    for car in car_dict.values():
        print(car)
```

- Usa `create_car_from_input()` en la **Opción 1** del menú.
- Usa `display_cars(car_dict)` en la **Opción 2** del menú.

---

### Parte 4c — Completar el programa principal en `overall.py`

Se te da un programa parcialmente escrito con un menú interactivo. Debes completar las partes marcadas con `# TODO`.

#### Configuración inicial

Al comienzo de `overall.py`, importa `car_utils.py` y `car.py`. El diccionario `cars` ya está declarado:

```python
cars = {}
```

Las claves son los `car_id` y los valores son objetos `Car`.

#### Opciones del menú

**Opción 1 — Agregar un auto nuevo**

Llama a `create_car_from_input()` para obtener un nuevo objeto `Car`. Guárdalo en `cars` usando su `car_id` como clave. Imprime el objeto y luego:

```
Car added.
```

**Opción 2 — Ver todos los autos**

Llama a `display_cars(cars)`.

**Opción 3 — Conducir un auto**

El programa ya pide el `car_id` y las millas. Busca el auto en el diccionario, llama a `drive()` e imprime:

```
Mileage updated.
```

Luego imprime la información actualizada del auto.

**Opción 4 — Pintar un auto**

El programa ya pide el `car_id` y el nuevo color. Busca el auto en el diccionario, llama a `change_color()` e imprime:

```
Color updated.
```

Luego imprime la información actualizada del auto.

**Opción 5 — Salir** *(ya implementada)*

```
Goodbye!
```

#### Ejemplos de ejecución

**Opción 1 — Agregar un auto**

Entrada:
```
1
CAR001
Toyota
2020
Red
15000
```
Salida:
```
CAR001 - 2020 Red Toyota with 15000.0 miles
Car added.
```

**Opción 3 — Conducir**

Entrada:
```
3
CAR001
200
```
Salida:
```
Mileage updated.
CAR001 - 2020 Red Toyota with 15200.0 miles
```

**Opción 4 — Pintar**

Entrada:
```
4
CAR001
Blue
```
Salida:
```
Color updated.
CAR001 - 2020 Blue Toyota with 15200.0 miles
```

---

## Pregunta 5 — Sistema bancario

**Archivos a modificar:** `bank_account.py` (Parte 5a), `person.py` (Parte 5b), `utils.py` (Parte 5c), `main.py` (Parte 5d)

El objetivo es construir un sistema bancario orientado a objetos que gestione múltiples usuarios, cada uno con una o más cuentas bancarias.

---

### Parte 5a — Clase `BankAccount` en `bank_account.py`

#### Atributos

| Atributo         | Tipo    | Descripción                             |
|------------------|---------|-----------------------------------------|
| `account_number` | `int`   | Número de cuenta único de cuatro dígitos |
| `balance`        | `float` | Saldo actual. Por defecto: `0.0`        |

#### Métodos

- **`__init__(self, account_number, balance=0.0)`** — Inicializa los atributos. El saldo por defecto es `0.0`.

- **`deposit(self, amount)`** — Suma `amount` al saldo actual.

- **`withdraw(self, amount)`** — Intenta retirar `amount`.
  - Si `amount > balance`: devuelve `-1` (fondos insuficientes).
  - Si hay saldo suficiente: resta `amount` y devuelve `0` (retiro exitoso).

- **`__str__(self)`** — Devuelve una cadena con el siguiente formato (solo se muestran los **últimos dos dígitos** del número de cuenta):

  ```
  Account Number: **<ultimos_dos_digitos>
  Current Balance: <saldo>
  ```

  > **Pista:** Para obtener los últimos caracteres de una cadena usa slicing: `str[-2:]`.

**Ejemplo de uso:**

```python
account = BankAccount(1234, 100.0)
print(account)
# Account Number: **34
# Current Balance: 100.00

account.deposit(50.0)
result = account.withdraw(120.0)
print("Withdrawal status:", "Success" if result == 0 else "Failed")
# Withdrawal status: Success

result = account.withdraw(50.0)
print("Withdrawal status:", "Success" if result == 0 else "Failed")
# Withdrawal status: Failed
```

---

### Parte 5b — Clase `Person` en `person.py`

#### Atributos

| Atributo   | Tipo   | Descripción                                      |
|------------|--------|--------------------------------------------------|
| `name`     | `str`  | Nombre de la persona                             |
| `accounts` | `list` | Lista de objetos `BankAccount` asociados a la persona |

#### Métodos

- **`__init__(self, name)`** — Inicializa el nombre e `accounts` como lista vacía.
- **`add_account(self, account)`** — Agrega un objeto `BankAccount` a `accounts`.
- **`__str__(self)`** — Devuelve:

  ```
  Name = <nombre>, Number of accounts = <numero_de_cuentas>
  ```

---

### Parte 5c — Funciones de utilidad en `utils.py`

#### `person_data()`

Esta función debe:

1. Pedir los siguientes datos al usuario:
   - Nombre → `Enter the person's name:`
   - Número de cuenta → `Enter a 4-digit account number:`
   - Saldo inicial → `Enter the initial balance:`
2. Crear un objeto `BankAccount` y agregarlo a la persona.
3. Preguntar si el usuario quiere agregar más cuentas:
   `Are you done adding accounts? (yes/no):`
   Repetir mientras la respuesta no sea `"yes"`.
4. Devolver el objeto `Person` completo.

#### `balance_summary(person_list)`

Recibe una lista de objetos `Person` e imprime el nombre de cada persona junto con la suma de todos sus saldos.

**Ejemplo de salida:**

```
Daniel : 90.00
Alice : 150.25
```

> **Pista:** Accede a los saldos con `person.accounts` y `account.balance`.

---

### Parte 5d — Programa principal en `main.py`

Escribe un programa interactivo con un menú que se repite hasta que el usuario elija salir. Importa todas las clases y funciones necesarias al inicio del archivo.

#### Menú

```
Choose an option:
1. Add a new person
2. Add an account to a person
3. Show all balances
4. Quit
```

#### Comportamiento de cada opción

**Opción 1 — Agregar una nueva persona**

Llama a `person_data()` y agrega el objeto `Person` devuelto a tu lista de personas.

**Opción 2 — Agregar una cuenta a una persona existente**

Pide el nombre de la persona (`Enter the person's name:`). Si existe, solicita el número de cuenta y el saldo inicial, crea un `BankAccount` y agrégalo a esa persona. Si no existe, imprime:

```
Person not found.
```

**Opción 3 — Mostrar todos los saldos**

Llama a `balance_summary(person_list)`. Si la lista está vacía, imprime:

```
No data to show.
```

**Opción 4 — Salir**

Termina el bucle e imprime:

```
Goodbye!
```

**Ejemplo de ejecución:**

Entrada:
```
1
Daniel
1234
100.0
yes
3
4
```

Salida:
```
Choose an option:
1. Add a new person
2. Add an account to a person
3. Show all balances
4. Quit
Enter the person's name:
Enter a 4-digit account number:
Enter the initial balance:
Are you done adding accounts? (yes/no):
Choose an option:
1. Add a new person
2. Add an account to a person
3. Show all balances
4. Quit
Daniel : 100.00
Choose an option:
1. Add a new person
2. Add an account to a person
3. Show all balances
4. Quit
Goodbye!
```

---

## Pregunta 6 — Control de altitud de una aeronave

**Archivos a modificar:** `aircraft_altitude.py` (crear)

> La clase `Aircraft` ya está implementada en `aircraft.py`. Impórtala al inicio de tu archivo.

Escribe un programa en `aircraft_altitude.py` que controle la altitud de un avión mediante comandos del usuario.

### Instrucciones

1. Pide al usuario el modelo de la aeronave y crea un objeto `Aircraft`:

   ```
   Enter aircraft model:
   ```

2. En un bucle, pide repetidamente un comando al usuario:

   ```
   Enter command (A for ascent, D for descent, X to exit):
   ```

   - `A <pies>` — sube la altitud (ej. `A 5000`)
   - `D <pies>` — baja la altitud (ej. `D 2000`)
   - `X` — termina el bucle

3. Al salir del bucle, imprime la altitud final.

### Pistas

- Usa `.split()` para separar el comando del número de pies.
- Convierte el valor de los pies a entero antes de llamar al método correspondiente.
- Usa un bucle `while True` y `break` para salir cuando el usuario ingrese `X`.

### Ejemplo de uso

```
Enter aircraft model: Boeing 747
Enter command (A for ascent, D for descent, X to exit): A 5000
Enter command (A for ascent, D for descent, X to exit): D 2000
Enter command (A for ascent, D for descent, X to exit): X
Final altitude: 3000 feet
```