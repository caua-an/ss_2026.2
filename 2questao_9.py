"""O erro numérico não é exatamente zero devido a limitações de precisão numérica do computador.
Mesmo que matematicamente yA e yB sejam iguais, na prática, operações de ponto flutuante podem introduzir pequenas diferenças.
Por isso, o erro máximo Emax é um valor muito pequeno, mas não exatamente zero. """

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

PASTA = Path(__file__).resolve().parent
PASTA_GRAFICO = PASTA / 'graficos'  

t = np.arange(-0.5, 3.5001, 0.001)  # vetor do tempo, indo de -0.5 a 3.5 com um pace de 1ms

a,b = 2.0, -0.5

# entradas x1, x2 e x3 como funções
def x1(instante):
    return np.sin(2*np.pi*instante)

def x2(instante):
    return np.where((instante >= 0) & (instante < 2), 1.0, 0.0)

def x3(instante):
    return a * x1(instante) + b * x2(instante)

# funcao para receber o sinal e o instante (vetor tempo)
def T(sinal, instante):
    return 2 * sinal(instante) +0.5 * sinal(instante - 1)


y1 = T(x1, t)
y2 = T(x2, t)

yA = T(x3, t)
yB = a * y1 + b * y2

erro = yA - yB
Emax = np.max(np.abs(erro))

print(f"Erro máximo entre yA e yB: {Emax:.18f}")
print(f"Linearidade: {np.allclose(yA, yB, atol=1e-12, rtol=0)}")


# Gráfico 1: saídas dos dois caminhos sobrepostas.
plt.figure(figsize=(10, 5))
plt.plot(t, yA, label='yA(t) = T{x3(t)}', linewidth=2)
plt.plot(t, yB, '--', label='yB(t) = ay1(t) + by2(t)', linewidth=1.5)
plt.title('Comparação dos dois caminhos')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(PASTA_GRAFICO / 'q9_comparacao.png', dpi=200)

# Gráfico 2: erro numérico ao longo do tempo.
plt.figure(figsize=(10, 4))
plt.plot(t, erro, label='e(t) = yA(t) - yB(t)')
plt.title(f'Erro de superposição | Emax = {Emax:.2e}')
plt.xlabel('Tempo (s)')
plt.ylabel('Erro numérico')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(PASTA_GRAFICO / 'q9_erro.png', dpi=200)

plt.show()

