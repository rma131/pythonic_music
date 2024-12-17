import math

class MusicTheory:
    # Chromatic scale with standard tuning (A440)
    CHROMATIC_SCALE = [
        "C", "C#/Db", "D", "D#/Eb", "E", "F", 
        "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"
    ]
    
    @staticmethod
    def get_pitch_frequency(note_index, base_freq=440):
        """
        Calculate frequency for a given note using equal temperament.
        A440 (A4) is the standard reference pitch.
        """
        return base_freq * (2 ** (note_index / 12))
    
    @staticmethod
    def major_scale(root_note):
        """
        Generate a major scale starting from a given root note.
        Uses the standard whole-whole-half-whole-whole-whole-half step pattern.
        """
        root_index = MusicTheory.CHROMATIC_SCALE.index(root_note)
        scale_steps = [0, 2, 4, 5, 7, 9, 11]
        return [MusicTheory.CHROMATIC_SCALE[(root_index + step) % 12] for step in scale_steps]
    
    @staticmethod
    def triad(root_note, chord_type='major'):
        """
        Generate a triad (three-note chord) based on the root note and chord type.
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
        
        return [MusicTheory.CHROMATIC_SCALE[(root_index + interval) % 12] for interval in intervals]
    
    @staticmethod
    def chord_progression(scale):
        """
        Generate common chord progressions based on a major scale.
        Uses Roman numeral notation for chord degrees.
        """
        return {
            'I': scale[0],      # Tonic
            'IV': scale[3],     # Subdominant
            'V': scale[4],      # Dominant
            'vi': scale[5].lower()  # Relative minor
        }

# Demonstration
if __name__ == "__main__":
    # Explore C Major
    c_scale = MusicTheory.major_scale("C")
    print("C Major Scale:", c_scale)
    
    # C Major triad
    c_major_triad = MusicTheory.triad("C")
    print("C Major Triad:", c_major_triad)
    
    # Chord progression in C Major
    c_progression = MusicTheory.chord_progression(c_scale)
    print("C Major Chord Progression:", c_progression)
    
    # Frequency of A4 (concert pitch)
    a4_freq = MusicTheory.get_pitch_frequency(9)
    print(f"Frequency of A4: {a4_freq:.2f} Hz")