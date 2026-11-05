import pandas as pd
import matplotlib.pyplot as plt

# Datos simulados de ventas mensuales de una empresa de transporte (COP)
fechas = pd.date_range(start='2025-01-01', periods=12, freq='MS')
ventas = [12000000, 13500000, 14200000, 13800000, 15500000, 16200000,
          15800000, 17500000, 18200000, 17800000, 19500000, 21000000]

df = pd.DataFrame({'fecha': fechas, 'ventas': ventas})
df['fecha'] = pd.to_datetime(df['fecha'])
df = df.set_index('fecha')

# Agrupación mensual y cálculo de media móvil de tres meses
mensual = df['ventas'].resample('MS').sum()
media_movil = mensual.rolling(window=3).mean()

resultado = pd.DataFrame({'ventas_mensuales': mensual, 'media_movil_3_meses': media_movil})
print(resultado.to_string())

plt.figure(figsize=(11, 5))
plt.plot(mensual.index, mensual / 1_000_000, marker='o', label='Ventas mensuales')
plt.plot(media_movil.index, media_movil / 1_000_000, marker='s', linestyle='--', label='Media móvil (3 meses)')
plt.title('Serie de tiempo: ventas de empresa de transporte (2025)')
plt.xlabel('Mes')
plt.ylabel('Ventas (millones de COP)')
plt.grid(alpha=0.3)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafica_ventas_media_movil.png', dpi=160)
plt.show()

print('\nAnálisis: Las ventas muestran una tendencia general creciente durante 2025,')
print('aunque presentan pequeñas disminuciones en abril, julio y octubre.')
print('Con un solo año de datos no se puede confirmar un patrón estacional recurrente.')
