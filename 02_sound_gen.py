import numpy as np
import sounddevice as sd
import time

class MusicTheory:
    # Chromatic scale with standard tuning (A440)
    CHROMATIC_SCALE = [
        "C", "C#/Db", "D", "D#/Eb", "E", "F", 
        "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"
    ]
    
    @staticmethod
    def generate_sine_wave(frequency, duration=0.5, sample_rate=44100, amplitude=0.5):
        """
        Generate a sine wave for a given frequency.
        
        :param frequency: Frequency of the note in Hz
        :param duration: Duration of the note in seconds
        :param sample_rate: Audio sample rate
        :param amplitude: Volume of the note (0-1)
        :return: NumPy array of audio samples
        """
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        note = amplitude * np.sin(2 * np.pi * frequency * t)
        return note
    
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
    def play_scale(root_note, duration=0.5):
        """
        Play the major scale for a given root note.
        
        :param root_note: Root note of the scale
        :param duration: Duration of each note in seconds
        """
        # Get the scale
        scale = MusicTheory.major_scale(root_note)
        
        # Generate frequencies for the scale
        scale_frequencies = []
        root_index = MusicTheory.CHROMATIC_SCALE.index(root_note)
        for step in [0, 2, 4, 5, 7, 9, 11]:
            freq = MusicTheory.get_pitch_frequency((root_index + step) % 12)
            scale_frequencies.append(freq)
        
        # Generate and play the scale
        audio_scale = []
        for freq in scale_frequencies:
            note = MusicTheory.generate_sine_wave(freq, duration)
            audio_scale.extend(note)
            # Add a small pause between notes
            audio_scale.extend(np.zeros(int(44100 * 0.1)))
        
        # Play the scale
        sd.play(np.array(audio_scale), 44100)
        sd.wait()
    
    @staticmethod
    def play_chord(root_note, chord_type='major', duration=1):
        """
        Play a chord (triad) for a given root note.
        
        :param root_note: Root note of the chord
        :param chord_type: Type of chord (major or minor)
        :param duration: Duration of the chord in seconds
        """
        # Get the frequencies for the chord
        root_index = MusicTheory.CHROMATIC_SCALE.index(root_note)
        
        if chord_type == 'major':
            # Major triad: root, major third, perfect fifth
            intervals = [0, 4, 7]
        elif chord_type == 'minor':
            # Minor triad: root, minor third, perfect fifth
            intervals = [0, 3, 7]
        else:
            raise ValueError("Supported chord types are 'major' and 'minor'")
        
        # Generate frequencies
        chord_frequencies = [
            MusicTheory.get_pitch_frequency((root_index + interval) % 12) 
            for interval in intervals
        ]
        
        # Generate chord audio
        chord_audio = []
        for freq in chord_frequencies:
            note = MusicTheory.generate_sine_wave(freq, duration)
            chord_audio.append(note)
        
        # Mix the notes together
        mixed_chord = np.sum(chord_audio, axis=0) / len(chord_audio)
        
        # Play the chord
        sd.play(mixed_chord, 44100)
        sd.wait()

# Demonstration
if __name__ == "__main__":
    # Play C Major Scale
    print("Playing C Major Scale")
    MusicTheory.play_scale("C")
    time.sleep(1)
    
    # Play C Major Chord
    print("Playing C Major Chord")
    MusicTheory.play_chord("C")
    time.sleep(1)
    
    # Play A Minor Chord
    print("Playing A Minor Chord")
    MusicTheory.play_chord("A", chord_type='minor')