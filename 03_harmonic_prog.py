import numpy as np
import sounddevice as sd
import time

class MusicTheory:
    CHROMATIC_SCALE = [
        "C", "C#/Db", "D", "D#/Eb", "E", "F", 
        "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"
    ]
    
    @staticmethod
    def generate_sine_wave(frequency, duration=0.5, sample_rate=44100, amplitude=0.5):
        """
        Generate a sine wave with a simple envelope for more musical sound.
        """
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        
        # Simple attack-decay envelope
        envelope = np.ones_like(t)
        attack_time = int(sample_rate * 0.05)  # 50ms attack
        decay_time = int(sample_rate * 0.2)    # 200ms decay
        
        envelope[:attack_time] = np.linspace(0, 1, attack_time)
        envelope[-decay_time:] *= np.linspace(1, 0, decay_time)
        
        note = amplitude * envelope * np.sin(2 * np.pi * frequency * t)
        return note
    
    @staticmethod
    def get_pitch_frequency(note_index, base_freq=440):
        """
        Calculate frequency for a given note using equal temperament.
        """
        return base_freq * (2 ** (note_index / 12))
    
    @staticmethod
    def triad(root_note, chord_type='major'):
        """
        Generate frequencies for a triad.
        """
        root_index = MusicTheory.CHROMATIC_SCALE.index(root_note)
        
        if chord_type == 'major':
            # Major triad: root, major third, perfect fifth
            intervals = [0, 4, 7]
        elif chord_type == 'minor':
            # Minor triad: root, minor third, perfect fifth
            intervals = [0, 3, 7]
        else:
            raise ValueError("Supported chord types are 'major' and 'minor'")
        
        return [
            MusicTheory.get_pitch_frequency((root_index + interval) % 12) 
            for interval in intervals
        ]
    
    @staticmethod
    def play_harmonic_progression(root_note, duration=1):
        """
        Play a classic I-ii-V-I chord progression to demonstrate tension and release.
        
        :param root_note: Root note of the progression
        :param duration: Duration of each chord in seconds
        """
        # Get the major scale
        scale_steps = [0, 2, 4, 5, 7, 9, 11]
        root_index = MusicTheory.CHROMATIC_SCALE.index(root_note)
        
        # Derive chords from the scale
        chords = [
            # I chord (Tonic) - Stable, home base
            MusicTheory.triad(MusicTheory.CHROMATIC_SCALE[(root_index + scale_steps[0]) % 12]),
            
            # ii chord (Supertonic) - Creates mild tension
            MusicTheory.triad(MusicTheory.CHROMATIC_SCALE[(root_index + scale_steps[1]) % 12], 'minor'),
            
            # V chord (Dominant) - Maximum tension
            MusicTheory.triad(MusicTheory.CHROMATIC_SCALE[(root_index + scale_steps[4]) % 12]),
            
            # I chord (Tonic) - Resolution, release of tension
            MusicTheory.triad(MusicTheory.CHROMATIC_SCALE[(root_index + scale_steps[0]) % 12])
        ]
        
        # Chord names for display
        chord_names = [
            f"I ({root_note} Major)", 
            f"ii ({MusicTheory.CHROMATIC_SCALE[(root_index + scale_steps[1]) % 12]} Minor)", 
            f"V ({MusicTheory.CHROMATIC_SCALE[(root_index + scale_steps[4]) % 12]} Major)", 
            f"I ({root_note} Major)"
        ]
        
        # Play progression
        for chord, name in zip(chords, chord_names):
            print(f"Playing {name} chord")
            
            # Generate chord audio
            chord_audio = []
            for freq in chord:
                note = MusicTheory.generate_sine_wave(freq, duration)
                chord_audio.append(note)
            
            # Mix the notes together
            mixed_chord = np.sum(chord_audio, axis=0) / len(chord_audio)
            
            # Play the chord
            sd.play(mixed_chord, 44100)
            sd.wait()
            
            # Small pause between chords
            time.sleep(0.2)

# Demonstration
if __name__ == "__main__":
    # Play harmonic progression in C Major
    print("Demonstrating Harmonic Progression (I-ii-V-I) in C Major")
    MusicTheory.play_harmonic_progression("C")
    
    # Optional: Try the same progression in other keys
    print("\nHarmonic Progression in G Major")
    MusicTheory.play_harmonic_progression("G")