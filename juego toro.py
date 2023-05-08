# Importamos el módulo random para generar números aleatorios
import random

# Definimos una clase Torero que tiene los atributos nombre, valor, arte y suerte
class Torero:
  def __init__(self, nombre, valor, arte, condición, suerte):
    self.nombre = nombre
    self.valor = valor
    self.arte = arte
    self.condición = condición
    self.suerte = suerte
    #self.otros_factores = otros_factores podria poner otro factor que fuera "Otros factores"

  def __str__(self):
    return f"{self.nombre} (Valentía: {self.valor}, Arte: {self.arte}, Condición: {self.condición}, Suerte: {self.suerte})"

# Definimos una clase Toro que tiene los atributos nombre, bravura, nobleza y peso
class Toro:
  def __init__(self, nombre, bravura, nobleza, peso, hechura):
    self.nombre = nombre
    self.bravura = bravura # Indica la bravura del toro
    self.nobleza = nobleza # Indica la nobleza del toro
    self.peso = peso # Un número entre 500 y 630 que indica el peso del toro en kg
    self.hechura = hechura

  def __str__(self):
    return f"{self.nombre} (Bravura: {self.bravura}, Nobleza: {self.nobleza}, Hechura: {hechura}, Peso: {self.peso} kilos)"


# Definimos una función que calcula la puntuación de un enfrentamiento entre un torero y un toro
def puntuacion(torero, toro):
  # La puntuación inicial es cero
  p = 0
  # Sumamos el valor y el arte del torero
  p += (torero.valor + torero.arte + torero.suerte)
  # Sumamos la bravura y la nobleza del toro
  p += (toro.bravura + toro.nobleza + toro.hechura)
  # Sumamos o restamos un número aleatorio entre -2 y 2 para simular la forma física del torero
  p += (torero.condición)
  # Sumamos o restamos un número aleatorio entre -1 y 1 debido al peso más o menos idóneo del toro
  """ p += random.randint(-1, 1) """
  # Devolvemos la puntuación redondeada al entero más cercano
  return round(p)

# Definimos una función que determina el resultado de un enfrentamiento en función de la puntuación
def resultado(p):
  if p <= -6:
    return "El público pita por la pésima actuación."
  elif -5 <= p <= -2:
    return "Parte del público pita."
  elif -1 <= p <= 0:
    return "No hay nada, ni pitos ni aplausos."
  elif 1 <= p <=4:
    return "Aplausos en el público."
  elif 5 <= p <=6:
    return "Se corta una oreja."
  elif 7 <= p <=8:
    return "Se corta una oreja y parte del público pide la vuelta al ruedo"
  elif 9 <= p <=13:
     return "Se cortan dos orejas y el toro da la vuelta al ruedo."
  elif 14 <= p <=18:
     return "¡Dos orejas y rabo!"
  else:
    return "¡INDULTO!"


# Definimos una función que simula un factor externo aleatorio que puede afectar al enfrentamiento
def factor_externo():
  # Elegimos un número aleatorio
  n = random.randint(-3, 3)
  # Si el número es 0, está lloviendo y eso resta un punto
  if n == -3:
    return "Llueve en la plaza, lo que entorpece la faena del diestro, -3 puntos.", -3
  # Si el número es 1, hace mucha calor y eso resta dos puntos
  elif n == -2:
    return "Hace mucho calor en la plaza, -2 puntos.", -2 #Hace mucho calor en la plaza y los toros se resienten
  elif n == -1:
    return "Hace viento, -1 punto.", -1 # Hace viento y eso resta dos puntos
  elif n == 1:
    return "Temperatura idónea para el toreo, 1 punto extra.", 1 # Buena temperatura para torear
  else:
    return "Cielo despejado.", 0


# Definimos una función que simula el tercio de varas, donde el toro recibe un puyazo del picador
def tercio_de_varas(toro):
  n = random.randint(-2, 3)
  if n == 3:
    return f"¡Puyazo muy bueno! Saluda el picador al público. {n} puntos a la lidia.", n
  elif 2 <= n <= 1:
    return f"El puyazo es bueno, {n} puntos a la lidia.", n
  elif n == -1:
    return f"El puyazo es malo, {n} puntos a la lidia.", n
  elif n == -2:
    return f"El público pide el cambio del toro, {n} puntos.", n
  else:
    return f"El puyazo es normal.", 0


# Definimos una función que simula el tercio de banderillas, donde el torero clava dos pares de banderillas al toro
def tercio_de_banderillas(torero):
  n = random.randint(-2, 4)
  if n == 4:
    return f"Banderillas muy buenas, se desmontera el banderillero. {n} puntos a la lidia.", n
  elif 1 <= n <= 2:
    return f"Las banderillas son buenas, {n} puntos a la lidia.", n
  elif -2 <= n <= -1:
    return f"Las banderillas son malas, {n} puntos a la lidia.", n
  else:
    return f"Banderillas algo desplazadas.", 0

# Definimos una función que simula el tercio de muerte, donde el torero mata al toro con la espada
def tercio_de_muerte(torero):
   n = random.randint(-6,6)
   if -6 <= n <= -4:
    return f"Mal con la muleta, resta {n} puntos.", n
   elif -3 <= n <= -1:
    return f"El torero y el toro no terminan de conectar, resta {n} puntos.", n
   elif 1 <= n <= 2:
    return f"El torero hace buenas tandas, suma {n} puntos a la lidia.", n
   elif 3 <= n <= 6:
    return f"¡Gran conexión entre torero y toro! La plaza en pie, {n} más a la lidia.", n
   else:
    return f"Buena faena.", 0


# Tres toreros con atributos aleatorios
toreros = []  #Toreros: random.choice(["Braulio Gilabert", "Vicente Sol \"El Maestro\"", "Antonio Marquerie", "José Miguel", "Pilar Cortés \"La Granera\"", "Pedro Gilabert \"El sompo\"", "Carlos Riera \"El Otaku\"", "Iñaki \"El Suizo\""])
for i in range(3):
  nombre = random.choice(["Braulio Gilabert", "Vicente Sol \"El Maestro\"", "Antonio Marquerie", "José Miguel", "Pilar Cortés \"La Granera\"", "Pedro Gilabert \"El sompo\"", "Carlos Riera \"El Otaku\"", "Iñaki \"El Suizo\""])
  valor = random.randint(0, 2) #valor del torero
  arte = random.randint(0, 2) #arte del torero
  condición = random.randint(0, 2) #condicion del torero
  suerte = random.randint(-3, 3) #suerte del torero
  torero = Torero(nombre, valor, arte, condición, suerte)
  """ torero2 = Torero("Braulio Gilabert", valor, arte, condición, suerte)
  torero3 = Torero("Clarita", valor, arte, condición, suerte) """
  toreros.append(torero) #cuando son aleatorios



# Seis toros con nombres y atributos aleatorios
toros = []
for i in range(6):
  nombre = random.choice(["Rocky", "Claritus", "Carlus", "Martus", "Iñakus", "Braulius", "Pilarus", "Cobradiezmos", "Arrojado", "Pablus", "Antonius"])
  bravura = random.randint(-3, 3) #bravura del toro
  nobleza = random.randint(-3, 3) #nobleza del toro
  peso = random.randint(500, 630) #peso del toro
  hechura = random.randint(-3, 3) #hechura del toro
  ganaderia = random.choice(["El Teular", "Benalúa", "Cantalar", "Ruiz de la Cuesta", "Riera", "San Blas", "Aigües", "Segura", "Bon Repós"])
  toro = Toro(nombre, bravura, nobleza, peso, hechura)
  toros.append(toro)


# Simulamos los enfrentamientos entre los toreros y los toros
for i in range(3):
   """ print("")
   print(f"El torero {toreros[i]} lidiará los toros {toros[2*i]} y {toros[2*i+1]} de la ganadería de {ganaderia}.") """
   print("")
   # Primer toro
   print(f"\tEl torero {toreros[i]} lidia su primer toro {toros[2*i]} de la ganadería de {ganaderia}.")

   # Calculamos la puntuación inicial del enfrentamiento
   p = puntuacion(toreros[i], toros[2*i]) #para cuando sean toreros aleatorios
   print(f"Puntuación tras la suerte del capote: {p}")

    # Simulamos la climatología que puede modificar la puntuación
   factor, modificador = factor_externo()
   print(f"{factor}")
 
  # Simulamos el tercio de varas
   varas, modificador_puntuacion = tercio_de_varas(toreros[i])
   print(f"Tercio de varas: {varas}")
   p += modificador_puntuacion

  # Tercio de banderillas
   banderillas, modificador_puntuacion = tercio_de_banderillas(toreros[i])
   print(f"Tercio de banderillas: {banderillas}")
   p += modificador_puntuacion

   # Tercio de muerte
   muerte, modificador_puntuacion = tercio_de_muerte(toreros[i])
   print(f"Tercio de muerte: {muerte}")
   p += modificador_puntuacion
  
   # Puntuación final
   p += modificador
   """ print(f"Puntuación final: {p} ") """
   p1 = p

   # Determinamos el resultado
   r = resultado(p)
   print(f"Resultado de la primera lidia: {r} ({p} puntos)")

   # Segundo toro
   print("")
   print(f"El torero {toreros[i]} lidia su segundo toro {toros[2*i+1]} de la ganadería de {ganaderia}.")
   """ print(f"Segundo toro: {toros[2*i+1]} de la ganadería de {ganaderia}.") """

   # Calculamos la puntuación inicial del enfrentamiento
   p = puntuacion(toreros[i], toros[2*i+1])
   print(f"Puntuación tras la suerte del capote: {p}")

 # Simulamos la climatología que puede modificar la puntuación
   factor, modificador = factor_externo()
   print(f"{factor}")

   # Simulamos el tercio de varas
   varas, modificador_puntuacion = tercio_de_varas(toreros[i])
   print(f"Tercio de varas: {varas}")
   p += modificador_puntuacion

  # Simulamos el tercio de banderillas
   banderillas, modificador_puntuacion = tercio_de_banderillas(toreros[i])
   print(f"Tercio de banderillas: {banderillas}")
   p += modificador_puntuacion

   # Simulamos el tercio de muerte
   muerte, modificador_puntuacion = tercio_de_muerte(toreros[i])
   print(f"Tercio de muerte: {muerte}")
   p += modificador_puntuacion

   # Puntuación final
   p += modificador
   """ print(f"Puntuación final: {p}") """
   p2 = p

   # Determinamos el resultado del enfrentamiento
   r = resultado(p)
   print(f"Resultado de la segunda lidia: {r} ({p} puntos)")

   # Celebración del torero en Sevilla
   print("")
   if p1 + p2 <= 0 and p1 <5 and p2 <5:
     print(f"\tEl torero se marcha abucheado por parte del público.")
   if (5 <= p1 + p2 <= 9 and (p1 <9 or p2 <9)) or (p1 >5 and p2 <5 or p2 >5 and p1 <5):
     print(f"\tEl torero se despide aplaudido por el público.")
   if (10 <= p1 + p2 <= 15 and p1 >= 5 and p2 >= 5) or (p1 >= 9 and p2 <= 4) or (p2 >=9 and p1 <= 4): #las dos finales son por la puerta del principe de sevilla
    print(f"\tEl torero {toreros[i]} sale a hombros por la Puerta Grande.") #toreros[i] cuando no sean elegidos
   if ((p1 >= 9 and p2 >= 5) or (p2 >= 9 and p1 >= 5)): #ambos han de tener mínimo 5, osea una oreja
    print(f"\tEl torero {toreros[i]} sale a hombros por la Puerta del Príncipe.")
   if p1 + p2 >= 18 or p1 >= 14 or p2 >= 14: # 14 o lo que marque las dos orejas y el rabo
     print(f"\t¡El torero {toreros[i]} es llevado a hombros al hotel!")
   else:
     print("")

     """ # Celebración del torero fuera de Sevilla. FALTA CAMBIAR CON LOS ARREGLOS NUEVOS
   print("")
   if 5 <= p1 + p2 <= 9:
     print(f"El torero se despide aplaudido por el público.")
   elif 10 <= p1 + p2 <= 35 and p1 >= 5 and p2 >= 5 or p1 >= 9 or p2 >= 9 #revisar
    print(f"El torero {toreros[i]} sale a hombros por la Puerta Grande.") #toreros[i] cuando no sean elegidos
   if p1 + p2 >= 18 or p1 >= 14 or p2 >= 14: # 14 o lo que marque las dos orejas y el rabo
     print(f"¡El torero {toreros[i]} es llevado a hombros a su hotel!")
   else:
     print("") """

     #hacer corridas en otros sitios que no sean Sevilla y luego en Sevilla jejeje