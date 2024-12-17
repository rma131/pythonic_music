class MusicTheory:
    """
    Music Theory as Python Concepts
    
    Imagine music as a programming language where:
    - Notes are variables
    - Scales are lists
    - Chords are tuples
    - Progressions are functions
    """
    
    # Class variables: our musical constants
    CHROMATIC_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    @classmethod
    def create_scale(cls, root, scale_type='major'):
        """
        Scale Generation: List Comprehension of Music
        
        Scales are like carefully filtered lists:
        - Major scale: list comprehension with specific index slicing
        - Each note is an 'element' in our musical sequence
        """
        # Music's list comprehension: select specific indices
        if scale_type == 'major':
            # Major scale: think of it as a list slice with custom step
            intervals = [0, 2, 4, 5, 7, 9, 11]
            root_index = cls.CHROMATIC_SCALE.index(root)
            
            return [
                cls.CHROMATIC_SCALE[(root_index + interval) % 12] 
                for interval in intervals
            ]
        
        # Error handling: like raising an exception in code
        raise ValueError("Unsupported scale type. Try 'major'.")
    
    @classmethod
    def generate_chord(cls, root, chord_type='major'):
        """
        Chords: Tuples of Harmonic State
        
        Chords are like immutable data structures:
        - Fixed composition
        - Represent a complete 'state' of musical information
        """
        root_index = cls.CHROMATIC_SCALE.index(root)
        
        # Chord generation: like creating a named tuple
        if chord_type == 'major':
            # Major chord: root, third, fifth
            return tuple(
                cls.CHROMATIC_SCALE[(root_index + interval) % 12] 
                for interval in [0, 4, 7]
            )
        elif chord_type == 'minor':
            # Minor chord: root, minor third, fifth
            return tuple(
                cls.CHROMATIC_SCALE[(root_index + interval) % 12] 
                for interval in [0, 3, 7]
            )
    
    @staticmethod
    def harmonic_progression(scale):
        """
        Chord Progressions: Higher-Order Functions of Music
        
        Progressions are like functional programming:
        - Transform input (scale)
        - Produce predictable output (chord sequence)
        - Each chord is a 'transformation' of the original scale
        """
        # Common progression mapping: functional approach
        return {
            'tonic': scale[0],          # I chord: home base
            'subdominant': scale[3],    # IV chord: gentle movement
            'dominant': scale[4],       # V chord: tension builder
            'relative_minor': scale[5]  # vi chord: emotional twist
        }

def music_theory_demo():
    """
    Musical Concepts as Pythonic Patterns
    
    Demonstrates how musical ideas map to programming concepts
    """
    # 1. Scale Generation: List Comprehension Magic
    print("🎵 Scale as List Comprehension:")
    c_major_scale = MusicTheory.create_scale('C')
    print(f"C Major Scale: {c_major_scale}")
    
    # 2. Chord Creation: Immutable Tuples
    print("\n🎸 Chords as Immutable Tuples:")
    c_major_chord = MusicTheory.generate_chord('C')
    c_minor_chord = MusicTheory.generate_chord('C', 'minor')
    print(f"C Major Chord: {c_major_chord}")
    print(f"C Minor Chord: {c_minor_chord}")
    
    # 3. Harmonic Progression: Functional Transformation
    print("\n🌈 Harmonic Progression: Functional Mapping:")
    progression = MusicTheory.harmonic_progression(c_major_scale)
    for role, chord in progression.items():
        print(f"{role.replace('_', ' ').title()}: {chord}")

# Meta-programming joke: music is just another programming language
if __name__ == "__main__":
    music_theory_demo()