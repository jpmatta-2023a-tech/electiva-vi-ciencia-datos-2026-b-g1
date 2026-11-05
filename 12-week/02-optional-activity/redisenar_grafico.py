import matplotlib.pyplot as plt
from pathlib import Path

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ventas = [12, 13.5, 14.2, 13.8, 15.5, 16.2, 15.8, 17.5, 18.2, 17.8, 19.5, 21]
salida = Path(__file__).resolve().parent

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.bar(meses, ventas, color=plt.cm.rainbow([i/11 for i in range(12)]), edgecolor='black', linewidth=1.5)
ax.set_ylim(11, 22)  # Escala truncada intencionalmente: diseño incorrecto
ax.set_ylabel('Valores')
ax.grid(axis='y', alpha=0.8, linestyle=':')
fig.tight_layout()
fig.savefig(salida / 'antes_grafico_incorrecto.png', dpi=170)
plt.close(fig)

fig, ax = plt.subplots(figsize=(11, 5.5))
colores = ['#187f89'] * 11 + ['#e4a23a']
barras = ax.bar(meses, ventas, color=colores, width=0.7)
ax.set_ylim(0, 24)
ax.set_ylabel('Ventas (millones de COP)')
ax.set_xlabel('Mes de 2025')
ax.set_title('Las ventas crecieron de $12 a $21 millones durante 2025', fontsize=14, weight='bold', pad=18)
ax.grid(axis='y', alpha=0.2)
ax.set_axisbelow(True)
for b, v in zip(barras, ventas):
    ax.text(b.get_x() + b.get_width()/2, v + 0.35, f'{v:g}', ha='center', fontsize=9)
for lado in ['top', 'right']:
    ax.spines[lado].set_visible(False)
fig.tight_layout()
fig.savefig(salida / 'despues_grafico_mejorado.png', dpi=170)
plt.close(fig)
