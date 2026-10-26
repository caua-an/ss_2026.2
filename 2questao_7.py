import numpy as np
import matplotlib.pyplot as plt 
from pathlib import Path

PASTA = Path(__file__).resolve().parent
PASTA_GRAFICO = PASTA / 'graficos'
# vetor do tempo, indo de 0 a 1 com um pace de 1ms
t = np.linspace(0,1,1001)

x1 = np.cos(2*np.pi*5*t)
x2 = np.sin(2*np.pi*10*t)

H = np.array([
    [1.0, 0.4],
    [0.3, 0.8],
])

entradas = np.vstack((x1, x2))
# multiplica a matriz h pelas entradas
y1, y2 = H @ entradas

# plotagem do grafico dos sinais transmitidos
plt.figure(figsize=(10, 4))
plt.plot(t, x1, label='x1(t) = cos(10πt)')
plt.plot(t, x2, label='x2(t) = sen(20πt)')
plt.title('Sinais transmitidos')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(PASTA_GRAFICO/ 'q7_entradas.png', dpi=200)

# plotagem do grafico dos sinais recebidos
plt.figure(figsize=(10, 4))
plt.plot(t, y1, label='y1(t) = x1(t) + 0,4x2(t)')
plt.plot(t, y2, label='y2(t) = 0,3x1(t) + 0,8x2(t)')
plt.title('Sinais recebidos')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(PASTA_GRAFICO / 'q7_saidas.png', dpi=200)


#plotagem dos transmitidos x recebidos

plt.figure(figsize=(10, 5))
plt.plot(t, x1, label='x1(t)', linestyle='--', alpha=0.75)
plt.plot(t, x2, label='x2(t)', linestyle='--', alpha=0.75)
plt.plot(t, y1, label='y1(t)', linewidth=2)
plt.plot(t, y2, label='y2(t)', linewidth=2)
plt.title('Transmitidos x recebidos')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(PASTA_GRAFICO / 'q7_comparacao.png', dpi=200)

plt.show()