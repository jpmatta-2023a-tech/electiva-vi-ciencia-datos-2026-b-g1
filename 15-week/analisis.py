from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base = Path(__file__).resolve().parent
df = pd.read_csv(base / 'datos_originales.csv')
df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True, errors='coerce')
resumen = df.groupby('ruta').agg(servicios=('id_servicio', 'size'), servicios_con_retraso=('retraso_min', lambda x: (x > 0).sum()))
resumen['porcentaje_retraso'] = (100 * resumen['servicios_con_retraso'] / resumen['servicios']).round(1)
resumen = resumen.sort_values('porcentaje_retraso', ascending=False)
print('Servicios:', len(df))
print('Servicios con retraso:', (df.retraso_min > 0).sum())
print('Porcentaje total:', round(100 * (df.retraso_min > 0).mean(), 1))
print('Tipos de servicio faltantes:', df.tipo_servicio.isna().sum())
print('IDs duplicados:', df.id_servicio.duplicated().sum())
print(resumen)
resumen.to_csv(base / 'resumen_rutas.csv', encoding='utf-8-sig')
fig, ax = plt.subplots(figsize=(10, 5.5))
bars = ax.barh(resumen.index[::-1], resumen['porcentaje_retraso'][::-1], color='#087f83')
ax.set_xlabel('Servicios con retraso (%)')
ax.set_title('Neiva–Cartagena registra la mayor proporción de retrasos (39,2 %)')
ax.set_xlim(0, 47)
for bar in bars:
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.1f} %', va='center')
fig.tight_layout()
fig.savefig(base / 'graficos' / 'retrasos_por_ruta.png', dpi=180)
