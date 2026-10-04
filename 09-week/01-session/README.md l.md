# Semana 9 — Análisis y limpieza de datos de ventas

## Descripción del proyecto

Este proyecto analiza un conjunto de datos de ventas de una tienda utilizando Python y Pandas. Incluye un modelo entidad-relación (DER), limpieza de datos, comparación antes/después y dos preguntas de análisis.

## Conjunto de datos

El archivo original es `data/ventas_sucias.csv`. El conjunto fue preparado con problemas comunes de calidad para demostrar el proceso de limpieza: valores faltantes, una fila duplicada, formatos de fecha diferentes, texto con mayúsculas/minúsculas inconsistentes y valores numéricos almacenados como texto.

## Modelo entidad-relación

El modelo contiene cuatro entidades:

- **Cliente:** información de los clientes.
- **Pedido:** información de cada compra.
- **Detalle_Pedido:** productos, cantidades y precios asociados a cada pedido.
- **Producto:** información de los productos y sus categorías.

Relaciones:

- Cliente **1:N** Pedido
- Pedido **1:N** Detalle_Pedido
- Producto **1:N** Detalle_Pedido

El diagrama se encuentra en `erd/modelo_der.png`.

## Data & Cleaning

The dataset contains e-commerce sales records with customers, orders, products, categories, quantities, prices, cities, and payment statuses. Before cleaning, the data included missing values, an exact duplicate row, inconsistent date formats, inconsistent text capitalization, and numeric values stored as strings. I converted the order dates to a consistent datetime format and standardized text fields by trimming spaces and applying consistent capitalization. I converted quantity and unit price into numeric data types so they could be used safely in calculations. I removed the duplicated row and filled missing values using documented rules, including medians for numeric fields and explicit labels for missing text. After cleaning, I created a total_sales column by multiplying quantity by unit price. Finally, I used pandas aggregations to answer two business questions about sales by category and average order value by city.

## Resumen de la limpieza

| Métrica | Antes | Después |
|---|---:|---:|
| Filas | 36 | 35 |
| Columnas | 11 | 12 |
| Celdas vacías | 4 | 0 |
| Filas duplicadas | 1 | 0 |

## Preguntas y hallazgos

### 1. ¿Qué categorías generan más ventas?

Se agrupan los datos por categoría y se suma `total_sales`. El notebook muestra automáticamente la categoría con mayores ventas y el valor total.

### 2. ¿Qué ciudad tiene el mayor valor promedio por pedido?

Se agrupan los datos por ciudad y se calcula el promedio de `total_sales`. El notebook muestra automáticamente la ciudad con el mayor valor promedio.

## Cómo ejecutar el proyecto

1. Instala Python 3.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Abre el notebook:

```bash
jupyter notebook notebooks/analisis_limpieza.ipynb
```

4. Ejecuta las celdas de arriba hacia abajo.

## Estructura del proyecto

```text
semana-9-proyecto-ventas-es/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── ventas_sucias.csv
│   └── DICCIONARIO_DATOS.md
├── erd/
│   └── modelo_der.png
└── notebooks/
    └── analisis_limpieza.ipynb
```

## Entrega en GitHub

Desde la carpeta del proyecto:

```bash
git add .
git commit -m "Agregar proyecto de análisis de datos semana 9"
git push
```

**Importante:** agrega el bloque `CONFIG` que exige tu curso con tu nombre completo y usuario de GitHub antes de entregar.
