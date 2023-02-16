import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Leitura do arquivo de áudio
fs, audio = wavfile.read('exemplo_audio.wav')

# Conversão para mono, se necessário
if audio.ndim > 1:
    audio = np.mean(audio, axis=1)

# Aplicação da Transformada de Fourier
fft = np.fft.fft(audio)

# Cálculo do espectro de frequência
freqs = np.fft.fftfreq(len(audio), 1.0/fs)
spectrum = np.abs(fft)

# Visualização do espectro de frequência
plt.plot(freqs[:len(freqs)//2], spectrum[:len(spectrum)//2])
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')
plt.show()
