class TeoriaMusical:
    """
    Teoría Musical como Conceptos de Python
    
    Imagina la música como un lenguaje de programación donde:
    - Notas son variables
    - Escalas son listas
    - Acordes son tuplas
    - Progresiones son funciones
    """
    
    # Variables de clase: nuestras constantes musicales
    ESCALA_CROMATICA = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    @classmethod
    def crear_escala(cls, nota_raiz, tipo_escala='mayor'):
        """
        Generación de Escala: Comprensión de Lista Musical
        
        Las escalas son como listas cuidadosamente filtradas:
        - Escala mayor: comprensión de lista con indexación específica
        - Cada nota es un 'elemento' en nuestra secuencia musical
        """
        # Comprensión de lista musical: selección de índices específicos
        if tipo_escala == 'mayor':
            # Escala mayor: como un slice de lista con paso personalizado
            intervalos = [0, 2, 4, 5, 7, 9, 11]
            indice_raiz = cls.ESCALA_CROMATICA.index(nota_raiz)
            
            return [
                cls.ESCALA_CROMATICA[(indice_raiz + intervalo) % 12] 
                for intervalo in intervalos
            ]
        
        # Manejo de errores: como lanzar una excepción en código
        raise ValueError("Tipo de escala no soportado. Prueba 'mayor'.")
    
    @classmethod
    def generar_acorde(cls, nota_raiz, tipo_acorde='mayor'):
        """
        Acordes: Tuplas de Estado Armónico
        
        Los acordes son como estructuras de datos inmutables:
        - Composición fija
        - Representan un 'estado' completo de información musical
        """
        indice_raiz = cls.ESCALA_CROMATICA.index(nota_raiz)
        
        # Generación de acordes: como crear una named tuple
        if tipo_acorde == 'mayor':
            # Acorde mayor: raíz, tercera, quinta
            return tuple(
                cls.ESCALA_CROMATICA[(indice_raiz + intervalo) % 12] 
                for intervalo in [0, 4, 7]
            )
        elif tipo_acorde == 'menor':
            # Acorde menor: raíz, tercera menor, quinta
            return tuple(
                cls.ESCALA_CROMATICA[(indice_raiz + intervalo) % 12] 
                for intervalo in [0, 3, 7]
            )
    
    @staticmethod
    def progresion_armonica(escala):
        """
        Progresiones de Acordes: Funciones de Orden Superior de la Música
        
        Las progresiones son como programación funcional:
        - Transforman la entrada (escala)
        - Producen salida predecible (secuencia de acordes)
        - Cada acorde es una 'transformación' de la escala original
        """
        # Mapeo de progresión común: enfoque funcional
        return {
            'tonica': escala[0],          # Acorde I: base
            'subdominante': escala[3],    # Acorde IV: movimiento suave
            'dominante': escala[4],       # Acorde V: constructor de tensión
            'relativo_menor': escala[5]   # Acorde vi: giro emocional
        }

def demostracion_teoria_musical():
    """
    Conceptos Musicales como Patrones Pythonicos
    
    Demuestra cómo las ideas musicales se mapean a conceptos de programación
    """
    # 1. Generación de Escala: Magia de Comprensión de Lista
    print("🎵 Escala como Comprensión de Lista:")
    escala_do_mayor = TeoriaMusical.crear_escala('C')
    print(f"Escala de Do Mayor: {escala_do_mayor}")
    
    # 2. Creación de Acordes: Tuplas Inmutables
    print("\n🎸 Acordes como Tuplas Inmutables:")
    acorde_do_mayor = TeoriaMusical.generar_acorde('C')
    acorde_do_menor = TeoriaMusical.generar_acorde('C', 'menor')
    print(f"Acorde de Do Mayor: {acorde_do_mayor}")
    print(f"Acorde de Do Menor: {acorde_do_menor}")
    
    # 3. Progresión Armónica: Transformación Funcional
    print("\n🌈 Progresión Armónica: Mapeo Funcional:")
    progresion = TeoriaMusical.progresion_armonica(escala_do_mayor)
    for rol, acorde in progresion.items():
        print(f"{rol.replace('_', ' ').title()}: {acorde}")

# Meta-chiste de programación: la música es solo otro lenguaje de programación
if __name__ == "__main__":
    demostracion_teoria_musical()