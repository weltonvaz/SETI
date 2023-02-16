# SETI
Exemplo simples em Python de como usar a Transformada de Fourier para analisar um sinal de áudio:

Neste exemplo, estamos lendo um arquivo de áudio (no formato WAV) e aplicando a Transformada de Fourier para analisar seu espectro de frequência. O primeiro passo é ler o arquivo de áudio e converter para mono, se necessário. Em seguida, aplicamos a Transformada de Fourier usando a função np.fft.fft do NumPy. Calculamos o espectro de frequência a partir do resultado da transformada, usando a função np.abs para obter a magnitude do sinal. Finalmente, visualizamos o espectro de frequência usando a biblioteca Matplotlib.

Obviamente, este é um exemplo muito simples e há muitas outras coisas que podem ser feitas com a Transformada de Fourier em Python. Mas espero que este exemplo dê uma ideia de como a Transformada de Fourier pode ser usada na prática para analisar sinais de áudio (ou qualquer outro tipo de sinal).

