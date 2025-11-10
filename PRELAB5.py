import datetime
from typing import List

# f) Clase Horario (RELACIÓN DE COMPOSICIÓN con Biblioteca)
class Horario:
    def __init__(self, dias_apertura: str, hora_apertura: int, hora_cierre: int):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrarHorario(self):
        """Muestra el horario de atención."""
        print(f"Horario de Atención: {self.dias_apertura} de {self.hora_apertura}:00 a {self.hora_cierre}:00.")

# g) Clase Pagina (RELACIÓN DE COMPOSICIÓN con Libro)
class Pagina:
    def __init__(self, numero_pagina: int, contenido_pagina: str):
        self.numero_pagina = numero_pagina 
        self.contenido_pagina = contenido_pagina 

    def mostrarHorario(self):
        """Muestra el número y contenido de la página. (Se usa 'mostrarHorario()' según la especificación del método)."""
        print(f"Página {self.numero_pagina}: {self.contenido_pagina}")


# c) Clase Autor (RELACIÓN DE AGREGACIÓN con Biblioteca)
class Autor:
    def __init__(self, nombre: str, nacionalidad: str):
        self.nombre = nombre 
        self.nacionalidad = nacionalidad 

    def mostrarInfo(self):
        """Muestra los datos del autor."""
        print(f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}")

# d) Clase Estudiante (RELACIÓN DE ASOCIACIÓN con Préstamo)
class Estudiante:
    def __init__(self, codigo_estudiante: str, nombre: str):
        self.codigo_estudiante = codigo_estudiante 
        self.nombre = nombre 

    def mostrarInfo(self):
        """Muestra los datos del estudiante."""
        print(f"Estudiante: {self.nombre}, Código: {self.codigo_estudiante}")

# b) Clase Libro (AGREGACIÓN con Biblioteca y COMPOSICIÓN con Pagina)
class Libro:
    def __init__(self, titulo: str, isbn: str, contenido_paginas: List[str]):
        self.titulo = titulo 
        self.isbn = isbn     
        
        # Composición: Las páginas se crean y existen solo dentro de Libro.
        self.paginas = [Pagina(i + 1, contenido) for i, contenido in enumerate(contenido_paginas)]

    def leer(self):
        """Muestra todas las páginas del libro."""
        print(f"\n-- Leyendo Libro: {self.titulo} (ISBN: {self.isbn}) --")
        for pagina in self.paginas:
            pagina.mostrarHorario() 
        print("-- Fin del Libro --")
        
    # Métodos para que el objeto se pueda manejar en listas de Biblioteca
    def __eq__(self, other):
        if isinstance(other, Libro):
            return self.isbn == other.isbn
        return False
        
    def __hash__(self):
        return hash(self.isbn)

# e) Clase Prestamo (RELACIÓN DE ASOCIACIÓN con Estudiante y Libro)
class Prestamo:
    def __init__(self, estudiante: Estudiante, libro: Libro):
        self.fecha_prestamo = datetime.date.today() 
        self.fecha_devolucion = None                
        self.referencia_estudiante = estudiante     
        self.referencia_libro = libro               

    def mostrarInfo(self):
        dev = self.fecha_devolucion if self.fecha_devolucion else "PENDIENTE"
        print("\n--- Detalle del Préstamo ---")
        print(f"Fecha Préstamo: {self.fecha_prestamo}")
        print(f"Fecha Devolución: {dev}")
        print(f"Estudiante: {self.referencia_estudiante.nombre} ({self.referencia_estudiante.codigo_estudiante})")
        print(f"Libro Prestado: {self.referencia_libro.titulo}")

# a) Clase Biblioteca (COMPOSICIÓN con Horario, AGREGACIÓN con Libro y Autor)
class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre_biblioteca = nombre             
        self.libros_disponibles = []                
        self.autores_registrados = []               
        self.prestamos_activos = []                 
        
        # Composición: Horario de atención (como clase interna).
        self.horario = Horario("Lunes-Viernes", 8, 18) 

    def agregarLibro(self, libro: Libro):
        if libro not in self.libros_disponibles:
            self.libros_disponibles.append(libro)
            print(f"Libro '{libro.titulo}' agregado a la colección.")
        else:
            print(f"Advertencia: El libro '{libro.titulo}' ya está en la colección.")

    def agregarAutor(self, autor: Autor):
        self.autores_registrados.append(autor)
        print(f"Autor '{autor.nombre}' registrado.")
    
    def prestarLibro(self, estudiante: Estudiante, libro: Libro):
        if libro in self.libros_disponibles:
            self.libros_disponibles.remove(libro)
            prestamo = Prestamo(estudiante, libro)
            self.prestamos_activos.append(prestamo)
            print(f"\nPRÉSTAMO CREADO para {estudiante.nombre} por el libro {libro.titulo}")
            return prestamo
        else:
            print(f"ERROR: El libro '{libro.titulo}' no está disponible.")
            return None

    def mostrarEstado(self):
        print(f"\n=== ESTADO DE LA BIBLIOTECA: {self.nombre_biblioteca} ===")
        self.horario.mostrarHorario()
        print(f"Libros disponibles: {len(self.libros_disponibles)}")
        print(f"Autores registrados: {len(self.autores_registrados)}")
        print(f"Préstamos activos: {len(self.prestamos_activos)}")
        print("==================================")
    
    def cerrarBiblioteca(self):
        self.prestamos_activos.clear() 
        try:
            del self.horario
        except AttributeError:
             pass 
        print(f"\nLa biblioteca {self.nombre_biblioteca} ha cerrado. Se cancelan los préstamos activos.")

# ===============================================
# C) EJECUCIÓN DE PRUEBA DE LAS TRES RELACIONES
# ===============================================

# 1. COMPOSICIÓN (Libro-Pagina)
contenido_libro = ["Página 1: Introducción", "Página 2: Desarrollo", "Página 3: Conclusiones"]
libro1 = Libro("POO Avanzada", "978-1234567890", contenido_libro) 
libro1.leer() 

# Creación de otros objetos para las relaciones
autor1 = Autor("Dr. Max Pardo", "Peruana")
estudiante1 = Estudiante("E1001", "Ana Mamani")

biblioteca_central = Biblioteca("Biblioteca Central") 
biblioteca_central.mostrarEstado()

# 2. AGREGACIÓN (Biblioteca-Autor, Biblioteca-Libro)
biblioteca_central.agregarAutor(autor1)
biblioteca_central.agregarLibro(libro1)

# 3. ASOCIACIÓN (Prestamo-Estudiante, Prestamo-Libro)
prestamo1 = biblioteca_central.prestarLibro(estudiante1, libro1)
if prestamo1:
    prestamo1.mostrarInfo()

biblioteca_central.mostrarEstado()

# COMPOSICIÓN y cierre de la biblioteca
biblioteca_central.cerrarBiblioteca()
