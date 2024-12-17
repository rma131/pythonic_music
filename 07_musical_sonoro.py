import numpy as np
import sounddevice as sd
import time

class TeoriaMusical:
    """
    Música como Código: Sintetizando Sonido con Python
    
    Conceptos musicales transformados en señales digitales
    """
    
    # Constantes musicales
    ESCALA_CROMATICA = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    FRECUENCIA_BASE = 440  # Frecuencia de referencia (A4)
    
    @classmethod
    def calcular_frecuencia(cls, nota):
        """
        Frecuencia como Función de Transformación
        
        Convierte notas en ondas de sonido usando logaritmos
        Como un map() para sonido
        """
        indice = cls.ESCALA_CROMATICA.index(nota)
        return cls.FRECUENCIA_BASE * (2 ** (indice / 12))
    
    @staticmethod
    def generar_onda(frecuencia, duracion=0.5, amplitud=0.5):
        """
        Generador de Ondas: Lista por Comprensión de Sonido
        
        Transforma frecuencia en array de sonido
        Como un generador, pero para audio
        """
        rate = 44100  # Frecuencia de muestreo
        t = np.linspace(0, duracion, int(rate * duracion), False)
        
        # Onda senoidal con envolvente
        onda = amplitud * np.sin(2 * np.pi * frecuencia * t)
        
        # Envolvente para suavizar inicio y fin
        envolvente = np.ones_like(t)
        ataque = int(rate * 0.05)
        decay = int(rate * 0.1)
        
        envolvente[:ataque] = np.linspace(0, 1, ataque)
        envolvente[-decay:] *= np.linspace(1, 0, decay)
        
        return (onda * envolvente).astype(np.float32)
    
    @classmethod
    def reproducir_escala(cls, nota_raiz):
        """
        Escala como Iterador Musical
        
        Reproduce una escala como si fuera un recorrido de lista
        """
        # Intervalos de escala mayor
        intervalos = [0, 2, 4, 5, 7, 9, 11]
        
        # Generamos ondas para cada nota de la escala
        ondas_escala = []
        indice_raiz = cls.ESCALA_CROMATICA.index(nota_raiz)
        
        for intervalo in intervalos:
            nota = cls.ESCALA_CROMATICA[(indice_raiz + intervalo) % 12]
            frecuencia = cls.calcular_frecuencia(nota)
            onda = cls.generar_onda(frecuencia)
            ondas_escala.append(onda)
            
            # Pequeña pausa entre notas
            ondas_escala.append(np.zeros(1000))
        
        # Concatenamos todas las ondas
        escala_completa = np.concatenate(ondas_escala)
        
        print(f"🎵 Reproduciendo Escala de {nota_raiz}")
        sd.play(escala_completa, 44100)
        sd.wait()
    
    @classmethod
    def reproducir_acorde(cls, nota_raiz, tipo='mayor'):
        """
        Acordes como Estructuras de Datos Armónicas
        
        Combina notas como si fueran elementos de una lista
        """
        indice_raiz = cls.ESCALA_CROMATICA.index(nota_raiz)
        
        # Intervalos para acordes
        intervalos = [0, 4, 7] if tipo == 'mayor' else [0, 3, 7]
        
        # Generamos ondas para cada nota del acorde
        ondas_acorde = []
        for intervalo in intervalos:
            nota = cls.ESCALA_CROMATICA[(indice_raiz + intervalo) % 12]
            frecuencia = cls.calcular_frecuencia(nota)
            onda = cls.generar_onda(frecuencia, duracion=1)
            ondas_acorde.append(onda)
        
        # Mezclamos las ondas como reduce()
        acorde_completo = np.mean(ondas_acorde, axis=0)
        
        print(f"🎸 Reproduciendo Acorde de {nota_raiz} {tipo.capitalize()}")
        sd.play(acorde_completo, 44100)
        sd.wait()

def demo_musica_pythonica():
    """
    Concierto Pythónico: Música como Código
    Demostración de conceptos musicales en 3 minutos
    """
    print("🐍 Teoría Musical en Código 🎵\n")
    
    # 1. Escala como Iteración
    TeoriaMusical.reproducir_escala('C')
    time.sleep(1)
    
    # 2. Acordes como Estructuras de Datos
    TeoriaMusical.reproducir_acorde('C')
    time.sleep(1)
    
    TeoriaMusical.reproducir_acorde('C', 'menor')
    
    print("\n🌈 Música: Un Lenguaje de Programación Sonoro!")

# Punto de entrada como en todo buen programa
if __name__ == "__main__":
    demo_musica_pythonica()