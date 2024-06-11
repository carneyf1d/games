import pyaudio
import numpy as np
import scipy.io.wavfile as wavfile

class voice_mutator:

    def __init__():
        pass

    def record_audio(self, filename, duration=5):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        frames = []
        for _ in range(int(RATE / CHUNK * duration)):
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        with open(filename, 'wb') as wf:
            wf.write(b''.join(frames))

    def pitch_shift(self, filename, semitones=2):
        rate, data = wavfile.read(filename)
        shifted_data = np.roll(data, int(rate * semitones / 12))
        wavfile.write('shifted_' + filename, rate, shifted_data)

    if __name__ == "__main__":
        record_audio('original.wav')
        pitch_shift('original.wav', semitones=2)