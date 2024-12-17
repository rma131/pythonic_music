# Teoría Musical: Una Metáfora Pythonica

class TeoriaMusical:
    """
    Teoría Musical como un Lenguaje de Programación
    Donde cada concepto musical es un patrón computacional
    """
    
    # Escala Cromática como Diccionario de 12 Tonos
    escala_cromatica = {
        0: 'Do', 1: 'Do#', 2: 'Re', 3: 'Re#', 
        4: 'Mi', 5: 'Fa', 6: 'Fa#', 
        7: 'Sol', 8: 'Sol#', 9: 'La', 
        10: 'La#', 11: 'Si'
    }
    
    # Fórmulas de Intervalos como Patrones Matemáticos
    formulas_escalas = {
        'mayor':     [0, 2, 4, 5, 7, 9, 11],  # Patrón de Intervalos
        'menor':     [0, 2, 3, 5, 7, 8, 10],  # Variación Natural
        'armonica':  [0, 2, 3, 5, 7, 8, 11]   # Variación Armónica
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
        indice_raiz = list(cls.escala_cromatica.keys())[
            list(cls.escala_cromatica.values()).index(nota_raiz)
        ]
        
        # Transformación funcional de intervalos
        def mapear_nota(intervalo):
            return cls.escala_cromatica[
                (indice_raiz + intervalo) % 12
            ]
        
        # Conversión a tupla: estructura inmutable
        return tuple(
            mapear_nota(intervalo) 
            for intervalo in cls.formulas_escalas.get(tipo, cls.formulas_escalas['mayor'])
        )
    
    @classmethod
    def generar_acordes(cls, escala):
        """
        Acordes: Conjuntos de Tonos como Estructuras de Datos
        
        Demuestra:
        - Diccionario como mapeo de nombres de acordes
        - Set como colección única de tonos
        - Derivación de acordes desde la escala
        """
        # Definición de construcción de acordes
        return {
            # Tríadas
            f'Acorde Mayor {escala[0]}': set([escala[0], escala[2], escala[4]]),
            f'Acorde Menor {escala[0]}': set([escala[0], escala[2], escala[4-1]]),
            f'Acorde Disminuido {escala[0]}': set([escala[0], escala[2-1], escala[4-1]]),
            
            # Acorde de Séptima
            f'Acorde de Séptima de {escala[0]}': set([escala[0], escala[2], escala[4], escala[6]])
        }
    
    @staticmethod
    def progresion_armonica(escala):
        """
        Progresión Armónica: Mapeo Funcional de Funciones Musicales
        
        Demuestra:
        - Mapeo funcional de roles armónicos
        - Descripción de la función de cada acorde
        """
        return {
            'Tónica': {
                'Acorde': escala[0],
                'Descripción': 'Base y punto de reposo de la tonalidad'
            },
            'Subdominante': {
                'Acorde': escala[3],
                'Descripción': 'Prepara el movimiento hacia la dominante'
            },
            'Dominante': {
                'Acorde': escala[4],
                'Descripción': 'Genera tensión y deseo de resolver'
            }
        }

def demostracion_teoria_musical():
    """
    Presentación Interactiva: Música como Código
    """
    print("🎵 Teoría Musical: Metáfora Pythonica 🐍")
    input("Presiona Enter para comenzar...")
    
    # Generación de Escala de Do Mayor
    print("\n🌈 Escalas: Transformación de Intervalos")
    escala_do_mayor = TeoriaMusical.generar_escala('Do')
    print(f"Estructura de Escala (Tupla Inmutable): {escala_do_mayor}")
    print(f"Tipo: {type(escala_do_mayor)}")
    input("Presiona Enter para siguiente slide...")
    
    # Generación de Acordes
    print("\n🎸 Acordes: Conjuntos de Tonos")
    acordes_do_mayor = TeoriaMusical.generar_acordes(escala_do_mayor)
    for nombre, tonos in acordes_do_mayor.items():
        print(f"{nombre}: {tonos}")
    input("Presiona Enter para siguiente slide...")
    
    # Progresión Armónica
    print("\n🌟 Progresión Armónica: Mapeo Funcional")
    progresion = TeoriaMusical.progresion_armonica(escala_do_mayor)
    for rol, detalles in progresion.items():
        print(f"{rol}:")
        print(f"  Acorde: {detalles['Acorde']}")
        print(f"  Función: {detalles['Descripción']}")

# Punto de entrada
if __name__ == "__main__":
    demostracion_teoria_musical()