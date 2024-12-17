import math
import numpy as np
import sounddevice as sd
import time

class MusicExplorer:
    """
    🎵 Musical Journey Through Code 🐍
    
    A playful exploration of music theory using Python,
    designed for absolute beginners!
    """
    
    # The 12 musical notes - our musical alphabet
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 
             'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    @staticmethod
    def visualize_notes():
        """
        🎨 Visual Representation of Musical Notes
        
        Think of musical notes like colors in a rainbow:
        - Each note is unique
        - They repeat in a predictable pattern
        """
        print("🌈 Musical Rainbow of Notes 🎵")
        for i, note in enumerate(MusicExplorer.NOTES):
            # Create a visual representation with color intensity
            intensity = int((i + 1) * 20)
            print(f"{note}: {'#' * intensity}")
    
    @staticmethod
    def sound_of_math(note_index):
        """
        🔢 Convert Mathematical Frequency to Sound
        
        Music is just beautiful mathematics!
        Frequency doubles every octave
        """
        base_frequency = 440  # A4 note
        frequency = base_frequency * (2 ** (note_index / 12))
        
        # Generate a brief musical tone
        sample_rate = 44100
        duration = 1.0
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        tone = np.sin(2 * np.pi * frequency * t)
        
        print(f"🎼 Playing {MusicExplorer.NOTES[note_index]} at {frequency:.2f} Hz")
        sd.play(tone, sample_rate)
        sd.wait()
    
    @staticmethod
    def create_major_scale(root_note):
        """
        🎹 Building a Musical Scale
        
        Scales are like musical staircases:
        - Each step follows a specific pattern
        - Creates a unique musical flavor
        """
        # Major scale follows: whole, whole, half, whole, whole, whole, half steps
        scale_pattern = [0, 2, 4, 5, 7, 9, 11]
        root_index = MusicExplorer.NOTES.index(root_note)
        
        scale = [MusicExplorer.NOTES[(root_index + step) % 12] for step in scale_pattern]
        
        print(f"🌟 {root_note} Major Scale: {scale}")
        return scale
    
    @staticmethod
    def musical_chords(root_note):
        """
        🎸 Chord Magic: Harmony in Code
        
        Chords are like musical friendships:
        - Multiple notes played together
        - Create emotional landscapes
        """
        root_index = MusicExplorer.NOTES.index(root_note)
        
        # Major chord: root, major third, perfect fifth
        major_chord = [
            MusicExplorer.NOTES[root_index],
            MusicExplorer.NOTES[(root_index + 4) % 12],
            MusicExplorer.NOTES[(root_index + 7) % 12]
        ]
        
        # Minor chord: root, minor third, perfect fifth
        minor_chord = [
            MusicExplorer.NOTES[root_index],
            MusicExplorer.NOTES[(root_index + 3) % 12],
            MusicExplorer.NOTES[(root_index + 7) % 12]
        ]
        
        print(f"🎳 {root_note} Major Chord: {major_chord}")
        print(f"🎲 {root_note} Minor Chord: {minor_chord}")
        return major_chord, minor_chord

def music_theory_demo():
    """
    🚀 3-Minute Music Theory Explosion! 
    A beginner's journey through musical concepts
    """
    print("🎵 Welcome to Music Theory: Coded! 🐍\n")
    
    # 1. Visualize the Musical Alphabet
    print("1. Musical Notes: Our Sonic Alphabet")
    MusicExplorer.visualize_notes()
    time.sleep(1)
    
    # 2. Sound of Mathematics
    print("\n2. Music is Math in Disguise!")
    MusicExplorer.sound_of_math(9)  # Play A note
    time.sleep(1)
    
    # 3. Create a Musical Scale
    print("\n3. Building Musical Staircases")
    c_scale = MusicExplorer.create_major_scale('C')
    time.sleep(1)
    
    # 4. Explore Musical Chords
    print("\n4. Harmonies: Musical Friendships")
    MusicExplorer.musical_chords('C')
    
    print("\n🌈 Music Theory: Decoded with Python! 🎉")

# Run the musical journey
if __name__ == "__main__":
    music_theory_demo()