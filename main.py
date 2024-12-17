# Teoría Musical: Una Metáfora Pythonica

class TeoriaMusical:
    """
    Teoría Musical como Metáfora de Programación Python.
    Donde cada concepto musical es explicado como un concepto de programación.
    """

    # Escala Cromática como Diccionario de 12 Tonos
    ESCALA_CROMATIC = {
        0: 'Do', 1: 'Do#', 2: 'Re', 3: 'Re#', 
        4: 'Mi', 5: 'Fa', 6: 'Fa#', 
        7: 'Sol', 8: 'Sol#', 9: 'La', 
        10: 'La#', 11: 'Si'
    }
    
    # Fórmulas de Intervalos como Patrones Matemáticos
    FORMULAS_ESCALAS = {
        # Escala Cromática
        'cromatica': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],  # Las 12 notas, separadas por semitonos entre sí.

        # Escalas mayores y menores

        'mayor':     [0, 2, 4, 5, 7, 9, 11],  # Patrón de Intervalos Mayor
        'menor':     [0, 2, 3, 5, 7, 8, 10],  # Variación Menor Natural
        'armonica':  [0, 2, 3, 5, 7, 8, 11],  # Variación Menor Armónica
        
        # Escalas Modales
                    # 1, 2, 3, 4, 5, 6, 7
        'jonica':    [0, 2, 4, 5, 7, 9, 11],  # Jónico (1, 2, 3, 4, 5, 6, 7)

                    # 1, 2, 3b,4, 5, 6, 7b
        'dorica':    [0, 2, 3, 5, 7, 9, 10],  # Dórico (1, 2, 3b, 4, 5, 6, 7b)

                    # 1, 2b,3b,4, 5, 6b,7b        
        'frigia':    [0, 1, 3, 5, 7, 8, 10],  # Frigio (1, 2b, 3b, 4, 5, 6b, 7b)

                    # 1, 2, 3, 4#, 5, 6, 7
        'lidia':     [0, 2, 4, 6, 7, 9, 11],  # Lidio (1, 2, 3, 4#, 5, 6, 7)

                    # 1, 2, 3, 4, 5, 6, 7b        
        'mixolidia': [0, 2, 4, 5, 7, 9, 10],  # Mixolidio (1, 2, 3, 4, 5, 6, 7b)

                    # 1, 2, 3b,4, 5, 6b, 7b        
        'eolio':     [0, 2, 3, 5, 7, 8, 10],  # Eolio (1, 2, 3b, 4, 5, 6b, 7b)

                    # 1, 2b,3b,4, 5b,6b,7b        
        'locrio':    [0, 1, 3, 5, 6, 8, 10]   # Locrio (1, 2b, 3b, 4, 5b, 6b, 7b)
    }
    



    @classmethod
    def generar_escala(cls, nota_raiz, tipo='mayor'):
        """
        Generación de Escala: Comprensión de Lista como Transformación Musical

        Demuestra: 
        - map() como transformador de secuencias
        - list comprehension como filtro musical
        - tuple como estructura inmutable de escala
        """
        # Encontrar índice de la nota raíz
        indice_raiz = list(cls.ESCALA_CROMATIC.keys())[
            list(cls.ESCALA_CROMATIC.values()).index(nota_raiz)
        ]
        
        # Transformación funcional de intervalos
        def mapear_nota(intervalo):
            return cls.ESCALA_CROMATIC[
                (indice_raiz + intervalo) % 12
            ]
        
        # Conversión a tupla: estructura inmutable
        return tuple(
            mapear_nota(intervalo) 
            for intervalo in cls.FORMULAS_ESCALAS.get(tipo, cls.FORMULAS_ESCALAS['mayor'])
        )
    
    @classmethod
    def generar_armonicos_basicos(cls, nota_raiz):
        """
        Genera armónicos básicos de la nota raíz con relaciones de frecuencia y semitonos.
        """
        # Encontrar índice de la nota raíz
        indice_raiz = list(cls.ESCALA_CROMATIC.keys())[
            list(cls.ESCALA_CROMATIC.values()).index(nota_raiz)
        ]

        # Función para obtener nota por intervalo
        def nota_por_intervalo(intervalo):
            return cls.ESCALA_CROMATIC[(indice_raiz + intervalo) % 12]

        return {
            'Tónica': nota_por_intervalo(0),        # Relación 1:1 (0 semitonos)
            'Octava': nota_por_intervalo(12),       # Relación 2:1 (+12 semitonos)
            'Quinta Justa': nota_por_intervalo(7),  # Relación 3:2 (+7 semitonos)
            'Tercera Mayor': nota_por_intervalo(4)  # Relación 4:3 (+4 semitonos)
        }



    @classmethod
    def generar_triadas_basicas(cls, nota_raiz):
        """
        Genera acordes básicos (Mayor, Menor, Disminuido) para una nota raíz
        """
        # Encontrar el índice de la nota raíz
        indice_raiz = list(cls.ESCALA_CROMATIC.keys())[
            list(cls.ESCALA_CROMATIC.values()).index(nota_raiz)
        ]
        
        # Función para obtener nota por intervalo
        def nota_por_intervalo(intervalo):
            return cls.ESCALA_CROMATIC[(indice_raiz + intervalo) % 12]
        
        return {
            f'Acorde Mayor de {nota_raiz}': set([
                nota_por_intervalo(0),   # Raíz
                nota_por_intervalo(4),   # Tercera Mayor
                nota_por_intervalo(7)    # Quinta Justa
            ]),
            f'Acorde Menor de {nota_raiz}': set([
                nota_por_intervalo(0),   # Raíz
                nota_por_intervalo(3),   # Tercera Menor
                nota_por_intervalo(7)    # Quinta Justa
            ]),
            f'Acorde Disminuido de {nota_raiz}': set([
                nota_por_intervalo(0),   # Raíz
                nota_por_intervalo(3),   # Tercera Menor
                nota_por_intervalo(6)    # Quinta Disminuida
            ])
        }

    @classmethod
    def generar_acordes_diatonicos(cls, escala):
        """
        Genera un diccionario de acordes diatónicos clasificados por tipo, con nombres dinámicos.
        """
        nombres_funcionales = {
            'I': 'Tónica',
            'ii': 'Supertónica',
            'iii': 'Mediante',
            'IV': 'Subdominante',
            'V': 'Dominante',
            'vi': 'Submediante',
            'vii°': 'Sensible'
        }
        tipos_acordes = {
            'I': 'Mayor', 'ii': 'Menor', 'iii': 'Menor',
            'IV': 'Mayor', 'V': 'Mayor', 'vi': 'Menor', 'vii°': 'Disminuido'
        }

        # Crear acordes con nombres dinámicos
        acordes = {}
        for i, grado in enumerate(['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']):
            notas = [escala[i], escala[(i + 2) % 7], escala[(i + 4) % 7]]
            tipo = tipos_acordes[grado]
            nombre_acorde = f"{escala[i]} {tipo}"  # Nombre dinámico: "Do Mayor", "Re Menor", etc.
            acordes[grado] = {
                'notas': set(notas),
                'nombre': nombre_acorde,
                'funcion': nombres_funcionales[grado]
            }
        return acordes

    @staticmethod
    def generar_progresion_armonica(acordes_diatonicos, progresion):
        """
        Genera una progresión armónica basada en una secuencia de grados.
        """
        return {
            grado: {
                'nombre': acordes_diatonicos[grado]['nombre'],
                'funcion': acordes_diatonicos[grado]['funcion'],
                'notas': acordes_diatonicos[grado]['notas']
            }
            for grado in progresion
        }

PROGRESIONES_COMUNES = {
    'Tónica-Subdominante-Dominante': ['I', 'IV', 'V'],
    'ii-V-I': ['ii', 'V', 'I'],
    'Cadencia Rota': ['V', 'vi'],
    'Progresión Descendente': ['I', 'vii°', 'vi', 'V'],
    'Circular': ['I', 'vi', 'ii', 'V']
}

def demostracion_teoria_musical():
    """
    Presentación Interactiva: Música como Código
    """
    print("🎵 Teoría Musical: Metáfora Pythonica 🐍\n")
    input("Presiona Enter para comenzar...\n")
    print("\n")
    print("~"*75, end=" ")
    print("\n")

    # Mostrar notas disponibles
    print("\nNotas disponibles:")
    for nota in TeoriaMusical.ESCALA_CROMATIC.values():
        print(nota, end=" ")
    print("\n")
    
    # Entrada de la tonalidad
    while True:
        nota_raiz = input("Ingresa la nota raíz🎼: ").capitalize()
        
        if nota_raiz in TeoriaMusical.ESCALA_CROMATIC.values():
            break
        else:
            print("Nota no válida. Intenta de nuevo.")
    print("\n")
    print("~"*75, end=" ")

    # Demostración de Escalas Modales
    print("\n🎸🎵 Escalas: Secuencia de notas fija con intervalos establecidos.")
    print("... como las TUPLAS tienen un orden definido el cual les da su función. 🎵🐍")
    print("~"*75, end=" ")
    print("\n ")
    print(" "*16, end=" ")
    print("I  |  II  |  III  |  IV |  V  |  VI  |  VI  |")

    escalas_modales = ['jonica', 'dorica', 'frigia', 'lidia', 'mixolidia', 'eolio', 'locrio']
    
    for modo in escalas_modales:
        escala = TeoriaMusical.generar_escala(nota_raiz, modo)
        print(f"\nEscala {modo.capitalize()}: {escala}")
    
    input("\nPresiona Enter para seguir...\n")
    print("~"*75, end=" ")
    
    # Relación de Armónicos Naturales
    print("\n🔊🎶 Relación de Armónicos Naturales:")
    print("Los armónicos se obtienen multiplicando la frecuencia de la tónica. Son el principio de la armonía musical y su relación matemática.🎼")
    print("~"*75, end=" ")
    print("\n")
    
    armonicos = TeoriaMusical.generar_armonicos_basicos(nota_raiz)
    
    print(f"1️. Tónica: {armonicos['Tónica']}  (Relación 1:1, 0 semitonos)")
    print(f"2️. Octava: {armonicos['Octava']}  (Relación 2:1, +12 semitonos)")
    print(f"3️. Quinta Justa: {armonicos['Quinta Justa']}  (Relación 3:2, +7 semitonos)")
    print(f"4️. Tercera Mayor: {armonicos['Tercera Mayor']}  (Relación 4:3, +4 semitonos)")

    input("\nPresiona Enter para seguir...\n")
    print("~"*75, end=" ")


    # Generar y mostrar triadas básicas
    print("\n🎸🎶 Triadas Básicas: Conjuntos de notas en armonía entre sí con la misma tonalidad.")
    print("... como los SETS no se toma en cuenta ni el orden ni los duplicados. 🎵🐍")
    print("~"*75, end=" ")
    triadas_basicas = TeoriaMusical.generar_triadas_basicas(nota_raiz)
    for nombre, acorde in triadas_basicas.items():
        print(f"\n{nombre}: {acorde}")

    input("\nPresiona Enter para seguir...\n")
    print("~"*75, end=" ")

    # Generar Escala y Acordes Diatónicos
    print("\n🎹🎶 Acordes Diatónicos: Diccionario de conjuntos de notas dentro de la escala de la tónica.")
    print("~"*75, end=" ")
    escala = TeoriaMusical.generar_escala(nota_raiz)
    acordes_diatonicos = TeoriaMusical.generar_acordes_diatonicos(escala)

    for grado, info in acordes_diatonicos.items():
        print(f"\n{grado} ({info['funcion']}): {info['nombre']} - {info['notas']}")

    input("\nPresiona Enter para seguir...\n")
    print("~"*75, end=" ")

    # Progresión Armónica basada en los Acordes Diatónicos
    print("\n🌈🔀 Progresión Armónica: Combinación de acordes que en secucencia generan Tensión y Reposo usando la Tónica, Subdominante y Dominante.")
    print("~"*75, end=" ")
    
    for nombre, grados in PROGRESIONES_COMUNES.items():
        progresion = TeoriaMusical.generar_progresion_armonica(acordes_diatonicos, grados)
        print(f"\n{nombre}:")
        for grado, info in progresion.items():
            print(f"  {grado} ({info['funcion']}): {info['nombre']} - {info['notas']}")

    print("\n")
    print("~"*75, end=" ")
    print("\n")
    input("\nPresiona Enter para salir...\n")



# Punto de entrada
if __name__ == "__main__":
    demostracion_teoria_musical()