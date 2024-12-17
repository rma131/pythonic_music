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
    def generar_acordes_basicos(cls, nota_raiz):
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
    def generar_acordes(cls, escala):
        """
        Acordes: Conjuntos de Tonos como Estructuras de Datos
        
        Demuestra:
        - Diccionario como mapeo de nombres de acordes
        - Set como colección única de tonos
        - Derivación de acordes desde la escala
        """
        # Construcción de acordes diatónicos
        return {
            # Tríadas Diatónicas (Triadas de cada grado)
            f'I - Mayor': set([escala[0], escala[2], escala[4]]),
            f'ii - Menor': set([escala[1], escala[3], escala[5]]),
            f'iii - Menor': set([escala[2], escala[4], escala[6]]),
            f'IV - Mayor': set([escala[3], escala[5], escala[0]]),
            f'V - Mayor': set([escala[4], escala[6], escala[1]]),
            f'vi - Menor': set([escala[5], escala[0], escala[2]]),
            f'vii° - Disminuido': set([escala[6], escala[1], escala[3]]),
            
            # Séptimas Diatónicas
            f'I7 - Dominante': set([escala[0], escala[2], escala[4], escala[6]]),
            f'ii7 - Menor': set([escala[1], escala[3], escala[5], escala[0]]),
            f'vii°7 - Menor': set([escala[6], escala[1], escala[3], escala[5]]),
        }
    
    @staticmethod
    def progresion_armonica(escala):
        """
        Progresión Armónica: Mapeo Funcional de Funciones Musicales

        Devuelve sets de los acordes
        """
        return {
            'Tónica': set([escala[0], escala[2], escala[4]]),
            'Subdominante': set([escala[3], escala[5], escala[0]]),
            'Dominante': set([escala[4], escala[6], escala[1]])
        }

def demostracion_teoria_musical():
    """
    Presentación Interactiva: Música como Código
    """
    print("🎵 Teoría Musical: Metáfora Pythonica 🐍")
    input("Presiona Enter para comenzar...")

    # Demostración de Escalas Modales
    print("\n🌈 Escalas: Secuencia de notas con diferentes intervalos.")
    escalas_modales = ['jonica', 'dorica', 'frigia', 'lidia', 'mixolidia', 'eolio', 'locrio', 'cromatica']
    
    for modo in escalas_modales:
        escala = TeoriaMusical.generar_escala('Do', modo)
        print(f"Escala {modo.capitalize()}: {escala}")
    
    input("\nPresiona Enter para siguiente slide...")
    
    # Generación de Acordes Diatónicos de Do Mayor
    print("\n🎸 Acordes Diatónicos: Conjuntos de notas resonantes entre sí.")
    escala_do_mayor = TeoriaMusical.generar_escala('Do')
    acordes_do_mayor = TeoriaMusical.generar_acordes(escala_do_mayor)
    
    for nombre, tonos in acordes_do_mayor.items():
        print(f"{nombre}: {tonos}")
    
    input("\nPresiona Enter para siguiente slide...")
    
    # Progresión Armónica con Sets de Acordes
    print("\n🌟 Progresión Armónica: Secuencia de Acordes que generan tensión y reposo.")
    progresion = TeoriaMusical.progresion_armonica(escala_do_mayor)
    
    for rol, acorde in progresion.items():
        print(f"{rol}: {acorde}")

# Punto de entrada
if __name__ == "__main__":
    demostracion_teoria_musical()