class TeoriaMusical:
    """
    Teoría Musical como Conceptos de Python
    
    Imagina la música como un lenguaje de programación donde:
    - Notas son variables
    - Escalas son listas
    - Acordes son tuplas
    - Progresiones son funciones
    """
    
    # Variables de clase: nuestras constantes musicales en do, re, mi, etc.
    ESCALA_CROMATICA = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si']
    
    @classmethod
    def crear_escala(cls, nota_raiz, tipo_escala='mayor'):
        """
        Generación de Escala: Comprensión de Lista Musical
        
        Demuestra la fórmula prima para diferentes tipos de escalas
        """
        # Fórmula prima para escalas: definición de intervalos
        formulas_escalas = {
            'mayor': [0, 2, 4, 5, 7, 9, 11],  # Intervalos de escala mayor
            'menor': [0, 2, 3, 5, 7, 8, 10],  # Intervalos de escala menor natural
            'armonica': [0, 2, 3, 5, 7, 8, 11]  # Intervalos de escala menor armónica
        }
        
        # Validación y selección de fórmula de escala
        if tipo_escala not in formulas_escalas:
            raise ValueError("Tipo de escala no soportado.")
        
        # Generación de la escala usando la fórmula seleccionada
        intervalos = formulas_escalas[tipo_escala]
        indice_raiz = cls.ESCALA_CROMATICA.index(nota_raiz)
        
        return [
            cls.ESCALA_CROMATICA[(indice_raiz + intervalo) % 12] 
            for intervalo in intervalos
        ]
    
    @classmethod
    def generar_acorde(cls, nota_raiz, tipo_acorde='mayor'):
        """
        Acordes: Tuplas de Estado Armónico con mapeo explícito
        """
        # Definición explícita de construcción de acordes
        formulas_acordes = {
            'mayor': [0, 4, 7],      # Acorde mayor: raíz, tercera mayor, quinta
            'menor': [0, 3, 7],      # Acorde menor: raíz, tercera menor, quinta
            'disminuido': [0, 3, 6]  # Acorde disminuido: raíz, tercera menor, quinta disminuida
        }
        
        # Validación y selección de fórmula de acorde
        if tipo_acorde not in formulas_acordes:
            raise ValueError("Tipo de acorde no soportado.")
        
        # Generación de acordes con mapeo funcional explícito
        indice_raiz = cls.ESCALA_CROMATICA.index(nota_raiz)
        return tuple(
            cls.ESCALA_CROMATICA[(indice_raiz + intervalo) % 12] 
            for intervalo in formulas_acordes[tipo_acorde]
        )
    
    @staticmethod
    def progresion_armonica(escala):
        """
        Progresiones de Acordes: Funciones de Orden Superior con Mapeo Explicito
        
        Demuestra transformación funcional de la escala en progresión
        """
        # Mapeo explícito de funciones armónicas
        funciones_armonica = {
            'I': escala[0],    # Tónica: acorde de base
            'vi': escala[5],   # Relativo menor: giro emocional
            'ii': escala[1],   # Supertónica: movimiento preparatorio
            'V': escala[4]     # Dominante: constructor de tensión
        }
        
        return funciones_armonica

def demostracion_teoria_musical():
    """
    Conceptos Musicales como Patrones Pythonicos
    
    Presentación interactiva con transiciones tipo slides
    """
    print("🎵 Teoría Musical como Programación")
    input("Presiona Enter para continuar...")
    
    # 1. Escalas: Fórmulas Musicales como Comprensión de Lista
    print("\n🌈 Escalas: Fórmulas Musicales como Listas")
    escalas = {
        'Mayor': TeoriaMusical.crear_escala('Do'),
        'Menor': TeoriaMusical.crear_escala('Do', 'menor'),
        'Armónica': TeoriaMusical.crear_escala('Do', 'armonica')
    }
    
    for tipo, escala in escalas.items():
        print(f"Escala {tipo} de Do: {escala}")
    
    input("\nPresiona Enter para siguiente slide...")
    
    # 2. Acordes: Construcción Explícita
    print("\n🎸 Acordes: Estructuras de Datos Musicales")
    acordes = {
        'Mayor': TeoriaMusical.generar_acorde('Do'),
        'Menor': TeoriaMusical.generar_acorde('Do', 'menor'),
        'Disminuido': TeoriaMusical.generar_acorde('Do', 'disminuido')
    }
    
    for tipo, acorde in acordes.items():
        print(f"Acorde {tipo} de Do: {acorde}")
    
    input("\nPresiona Enter para siguiente slide...")
    
    # 3. Progresión Armónica: Transformación Funcional
    print("\n🌟 Progresión Armónica: I - vi - ii - V")
    escala_do_mayor = TeoriaMusical.crear_escala('Do')
    progresion = TeoriaMusical.progresion_armonica(escala_do_mayor)
    
    print("Progresión de Acordes:")
    for funcion, acorde in progresion.items():
        print(f"{funcion}: {acorde}")

# Ejecución como presentación
if __name__ == "__main__":
    demostracion_teoria_musical()