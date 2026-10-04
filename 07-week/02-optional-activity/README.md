# Entrega Semana 07 — Consultas SQL y Pandas

## Dataset
Se utilizó un dataset propio de ventas (`ventas.csv`) basado en el caso de sistema de ventas trabajado en la semana anterior.

## 1. Consulta SQL con WHERE
Filtra las ventas de la categoría **Tecnologia** cuyo valor de línea es superior a $500.000.

**Qué responde:** permite encontrar ventas de tecnología de mayor valor.

## 2. Consulta SQL con JOIN
Relaciona `Pedido`, `Cliente`, `DetallePedido` y `Producto`.

**Qué responde:** muestra qué cliente realizó cada pedido y qué producto compró, junto con la cantidad y el precio.

## 3. Consulta SQL con GROUP BY
Agrupa las ventas por categoría y calcula:
- ventas totales
- unidades vendidas

**Qué responde:** permite comparar el rendimiento de cada categoría.

## Equivalente en Pandas
La consulta `GROUP BY` se reproduce con `groupby()` y `agg()` en `semana_07_pandas.py`.

## Nota sobre el JOIN
El CSV está preparado como dataset compacto para las consultas WHERE y GROUP BY. La consulta JOIN usa el modelo relacional de la semana 6 (`Cliente`, `Pedido`, `DetallePedido`, `Producto`), porque así se demuestra correctamente el uso de claves y relaciones.
