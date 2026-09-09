# ☕ Actividad: Analítica de Datos en una Cafetería

## 📌 Descripción

En esta actividad se presenta un caso sencillo de aplicación de la **analítica de datos** en una cafetería.

La cafetería recopila diferentes tipos de información relacionada con sus ventas, clientes, productos y opiniones. Estos datos pueden ser utilizados para comprender el comportamiento del negocio, identificar tendencias y apoyar la toma de decisiones.

El objetivo de esta actividad es identificar diferentes tipos de datos, clasificarlos, formular preguntas de analítica descriptiva y predictiva, representar el flujo de los datos y explicar la diferencia entre ambos tipos de analítica.

---

## 🎯 Objetivos

- Identificar diferentes tipos de datos utilizados por una empresa.
- Clasificar los datos como **estructurados, semiestructurados o no estructurados**.
- Formular una pregunta de **analítica descriptiva**.
- Formular una pregunta de **analítica predictiva**.
- Representar el proceso de transformación de los datos mediante un diagrama.
- Comprender la diferencia entre analítica descriptiva y predictiva.
- Reconocer la importancia de los datos para la toma de decisiones empresariales.

---

# ☕ 1. Caso seleccionado: Cafetería

Para esta actividad se selecciona como caso de estudio una **cafetería** que ofrece productos como:

- ☕ Café americano
- 🥛 Capuchino
- 🍵 Té
- 🧁 Postres
- 🥐 Productos de panadería
- 🥪 Desayunos
- 🧋 Bebidas frías

La cafetería registra información diariamente sobre sus ventas, productos, clientes, inventario y opiniones.

Esta información puede ser analizada para conocer el desempeño del negocio y realizar predicciones sobre su comportamiento futuro.

---

# 📊 2. Tipos de datos

En una cafetería se pueden encontrar diferentes tipos de datos. Para este caso se seleccionaron cuatro ejemplos.

| # | Tipo de dato | Ejemplo | Clasificación | Descripción |
|---|---|---|---|---|
| 1 | Datos de ventas | Producto, cantidad, precio, fecha y total | **Estructurados** | Se organizan fácilmente en filas y columnas. |
| 2 | Información de clientes en JSON | Nombre, producto favorito y frecuencia de compra | **Semiestructurados** | Tiene campos y etiquetas que organizan la información. |
| 3 | Comentarios de clientes | "El café estaba muy bueno, pero el servicio fue lento." | **No estructurados** | Es texto libre y no tiene una estructura fija. |
| 4 | Fotografías de productos | Fotos de cafés, postres y desayunos | **No estructurados** | Contienen información visual que no está organizada en tablas. |

## 🟢 2.1 Datos estructurados

Los **datos estructurados** son aquellos que tienen una organización definida y siguen un formato establecido.

Generalmente se almacenan en:

- Bases de datos.
- Hojas de cálculo.
- Tablas.
- Sistemas de ventas.

### Ejemplo

| Fecha | Producto | Cantidad | Precio | Total |
|---|---|---:|---:|---:|
| 01/09/2026 | Café americano | 10 | $5.000 | $50.000 |
| 01/09/2026 | Capuchino | 15 | $7.000 | $105.000 |
| 01/09/2026 | Cheesecake | 8 | $9.000 | $72.000 |
| 02/09/2026 | Café americano | 12 | $5.000 | $60.000 |

Estos datos permiten realizar cálculos y análisis fácilmente.

Por ejemplo, se puede determinar:

- Cuántos productos se vendieron.
- Cuánto dinero ingresó.
- Cuál fue el producto más vendido.
- Qué día tuvo mayores ventas.
- Cuál fue el promedio de ventas.

## 🟡 2.2 Datos semiestructurados

Los **datos semiestructurados** tienen cierta organización, pero no siguen necesariamente el formato tradicional de una tabla.

Un ejemplo es la información de los clientes almacenada en formato **JSON**:

```json
{
  "cliente": "Cliente 001",
  "producto_favorito": "Capuchino",
  "frecuencia_compra": "Semanal",
  "preferencia": "Bebidas calientes"
}
```

Aunque esta información no está organizada en filas y columnas, existen campos y etiquetas que permiten identificar cada elemento.

Otros ejemplos de datos semiestructurados pueden ser:

- JSON.
- XML.
- Correos electrónicos.
- Registros de sistemas.
- Datos provenientes de algunas aplicaciones.

## 🔴 2.3 Datos no estructurados

Los **datos no estructurados** no tienen una estructura fija que permita organizarlos directamente en filas y columnas.

En la cafetería pueden encontrarse ejemplos como:

- 💬 Comentarios de clientes.
- 📷 Fotografías de productos.
- 🎥 Videos de redes sociales.
- 🎙️ Grabaciones de voz.
- 📝 Opiniones escritas libremente.

Por ejemplo:

> "Me gustó mucho el café y el ambiente, pero tuve que esperar demasiado para recibir mi pedido."

Este comentario contiene información útil sobre la satisfacción del cliente, pero primero tendría que ser procesado para convertirlo en información que pueda analizarse.

---

# 📈 3. Analítica descriptiva

La **analítica descriptiva** se utiliza para analizar datos históricos y comprender **qué ocurrió en el pasado**.

En una cafetería puede utilizarse para analizar:

- Ventas diarias.
- Ventas mensuales.
- Productos más vendidos.
- Horarios con mayor cantidad de clientes.
- Ingresos.
- Cantidad de productos vendidos.
- Opiniones de los clientes.
- Comportamiento histórico de las ventas.

### ❓ Pregunta de analítica descriptiva

> **¿Cuál fue el producto más vendido durante el último mes y cuánto dinero generó?**

Para responder esta pregunta se pueden analizar los registros históricos de ventas y agrupar los productos según la cantidad vendida.

### Ejemplo

| Producto | Unidades vendidas | Ingresos |
|---|---:|---:|
| Capuchino | 350 | $2.450.000 |
| Café americano | 280 | $1.400.000 |
| Cheesecake | 210 | $1.890.000 |
| Té | 150 | $750.000 |

A partir de estos datos, la cafetería puede identificar que el **capuchino** fue el producto con mayor cantidad de unidades vendidas.

### ✅ ¿Qué permite conocer?

La analítica descriptiva responde principalmente preguntas como:

- ¿Qué ocurrió?
- ¿Cuánto se vendió?
- ¿Cuál fue el producto más vendido?
- ¿Qué día tuvo mayores ventas?
- ¿Cuál fue el ingreso del mes?
- ¿Cuál fue el comportamiento de las ventas?

---

# 🔮 4. Analítica predictiva

La **analítica predictiva** utiliza datos históricos, patrones y métodos estadísticos para realizar estimaciones sobre situaciones futuras.

En una cafetería puede utilizarse para:

- Predecir la demanda de productos.
- Estimar las ventas futuras.
- Identificar días con mayor demanda.
- Anticipar necesidades de inventario.
- Estimar el comportamiento de los clientes.
- Planificar compras de ingredientes.
- Preparar promociones.

### ❓ Pregunta de analítica predictiva

> **¿Qué producto tendrá mayor demanda durante la próxima semana?**

Para responder esta pregunta se pueden utilizar datos históricos de ventas, días de la semana, temporadas, promociones y comportamiento de los clientes.

Por ejemplo, si los datos históricos muestran que durante los viernes y sábados aumenta la venta de capuchinos y postres, la cafetería puede estimar que estos productos tendrán una demanda elevada durante el siguiente fin de semana.

### ✅ ¿Qué permite conocer?

La analítica predictiva responde preguntas como:

- ¿Qué podría ocurrir?
- ¿Qué producto tendrá mayor demanda?
- ¿Cuánto podríamos vender la próxima semana?
- ¿Qué cantidad de inventario deberíamos preparar?
- ¿Qué días podrían tener mayores ventas?

> **Importante:** una predicción no garantiza que el evento vaya a ocurrir. Es una estimación basada en patrones y datos históricos.

---

# 🔄 5. Flujo de los datos

El proceso de análisis de datos de la cafetería puede representarse mediante las siguientes etapas:

```text
┌─────────────────────────────┐
│          📥 FUENTE           │
├─────────────────────────────┤
│ • Sistema de ventas         │
│ • Registro de inventario    │
│ • Encuestas                 │
│ • Comentarios de clientes   │
│ • Redes sociales            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      💾 ALMACENAMIENTO       │
├─────────────────────────────┤
│ • Base de datos             │
│ • Hojas de cálculo          │
│ • Almacenamiento en la nube │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│          🔎 ANÁLISIS         │
├─────────────────────────────┤
│ • Limpieza de datos         │
│ • Analítica descriptiva     │
│ • Analítica predictiva      │
│ • Identificación de patrones│
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       📊 VISUALIZACIÓN      │
├─────────────────────────────┤
│ • Gráficos                  │
│ • Tablas                    │
│ • Indicadores (KPI)         │
│ • Dashboards                │
└─────────────────────────────┘
```

### 🔗 Resumen del flujo

**Fuente → Almacenamiento → Análisis → Visualización**

---

# 🧩 6. Explicación del flujo

## 📥 Fuente

La **fuente** es el lugar donde se generan o recopilan los datos.

En la cafetería pueden ser:

- Sistema de ventas.
- Registro de inventario.
- Encuestas.
- Comentarios de clientes.
- Redes sociales.

Por ejemplo, cada vez que un cliente compra un capuchino, el sistema puede registrar la fecha, hora, cantidad y precio.

## 💾 Almacenamiento

Una vez recopilados, los datos deben almacenarse para poder consultarlos y analizarlos posteriormente.

La cafetería podría utilizar:

- Excel o Google Sheets.
- Una base de datos.
- Un sistema de punto de venta.
- Servicios de almacenamiento en la nube.

El objetivo es mantener los datos disponibles y organizados.

## 🔎 Análisis

En esta etapa los datos se procesan para obtener información útil.

Algunas actividades pueden ser:

1. Eliminar datos duplicados.
2. Corregir errores.
3. Organizar la información.
4. Calcular indicadores.
5. Identificar patrones.
6. Realizar análisis descriptivos.
7. Realizar análisis predictivos.

Por ejemplo, se pueden analizar las ventas de los últimos seis meses para determinar cuáles son los productos más populares.

## 📊 Visualización

Los resultados del análisis pueden presentarse mediante:

- Gráficos de barras.
- Gráficos de líneas.
- Tablas.
- Indicadores.
- Dashboards.

Por ejemplo, un dashboard podría mostrar:

| Indicador | Resultado |
|---|---:|
| Ventas del mes | $12.500.000 |
| Producto más vendido | Capuchino |
| Día con mayores ventas | Viernes |
| Promedio de ventas diarias | $416.667 |
| Producto con mayor crecimiento | Cheesecake |

La visualización facilita que el administrador pueda interpretar rápidamente la información.

---

# 💡 7. Ejemplo de aplicación práctica

Supongamos que la cafetería analiza sus datos correspondientes a los últimos seis meses.

Después de realizar el análisis, identifica los siguientes patrones:

- Los viernes presentan mayores ventas.
- El capuchino es uno de los productos más vendidos.
- Los postres tienen mayor demanda durante la tarde.
- Las promociones generan un aumento en las ventas.
- Los fines de semana aumenta el número de clientes.

### Aplicación de analítica descriptiva

La cafetería puede concluir:

> **"Durante los últimos seis meses, los viernes fueron los días con mayores ventas."**

Esta conclusión describe un comportamiento que ya ocurrió.

### Aplicación de analítica predictiva

A partir de los datos anteriores, la empresa podría estimar:

> **"Es probable que las ventas del próximo viernes sean superiores al promedio de los demás días."**

Esta información puede ayudar al administrador a prepararse con anticipación.

Por ejemplo, podría:

- Comprar más café.
- Preparar más postres.
- Aumentar el inventario.
- Programar más empleados.
- Crear una promoción para ese día.

---

# 📋 8. Comparación entre analítica descriptiva y predictiva

| Característica | Analítica descriptiva | Analítica predictiva |
|---|---|---|
| Objetivo | Comprender lo que ocurrió | Estimar lo que podría ocurrir |
| Datos | Principalmente históricos | Históricos y patrones |
| Pregunta principal | ¿Qué pasó? | ¿Qué podría pasar? |
| Ejemplo | ¿Cuál fue el producto más vendido? | ¿Cuál será el producto más demandado? |
| Uso | Comprender el desempeño | Apoyar la planificación |
| Resultado | Información sobre el pasado | Predicciones sobre el futuro |

---

# 🇺🇸 9. Difference between descriptive analytics and predictive analytics

Descriptive analytics focuses on historical data to explain what happened in the past. It helps businesses understand sales, trends, and customer behavior.

Predictive analytics uses historical data, patterns, and statistical methods to estimate what may happen in the future. It helps businesses forecast demand, sales, and customer behavior.

---

# 🌟 10. Importancia de la analítica de datos

La analítica de datos puede ayudar a una cafetería a mejorar diferentes áreas del negocio.

### 📌 Toma de decisiones

Los administradores pueden tomar decisiones basadas en información real en lugar de depender únicamente de suposiciones.

### 📌 Control del inventario

Conocer cuáles productos tienen mayor demanda permite comprar y preparar los ingredientes necesarios.

### 📌 Reducción de desperdicios

Si la empresa puede estimar la demanda, puede evitar preparar cantidades excesivas de productos que después no se venden.

### 📌 Conocimiento de los clientes

Los datos de compras y comentarios permiten conocer mejor las preferencias de los consumidores.

### 📌 Aumento de las ventas

El análisis de los productos más populares puede ayudar a diseñar promociones y estrategias comerciales.

### 📌 Planificación

Las predicciones permiten prepararse para períodos de mayor demanda.

---

# 📝 11. Conclusión

La analítica de datos permite convertir los datos generados por una empresa en información útil para la toma de decisiones.

En el caso de la cafetería, existen diferentes tipos de datos. Los registros de ventas son **datos estructurados**, la información almacenada en formatos como JSON puede considerarse **semiestructurada**, mientras que los comentarios y fotografías corresponden principalmente a **datos no estructurados**.

La **analítica descriptiva** permite conocer y explicar lo que ocurrió en el pasado, por ejemplo, identificar cuál fue el producto más vendido durante el último mes. Por otro lado, la **analítica predictiva** utiliza información histórica para estimar situaciones futuras, como determinar qué producto podría tener mayor demanda la próxima semana.

El proceso **Fuente → Almacenamiento → Análisis → Visualización** permite transformar los datos en información comprensible y útil. Gracias a este proceso, una cafetería puede mejorar la gestión de sus productos, inventario, ventas y clientes.

En conclusión, el uso adecuado de los datos puede ayudar a que una empresa tome mejores decisiones, reduzca costos, mejore sus servicios y se prepare de una mejor manera para las necesidades futuras de sus clientes.

---

---

# 📚 Resumen de la actividad

| Requisito | Cumplimiento |
|---|---|
| Identificar 4 tipos de datos | ✅ |
| Clasificar datos estructurados | ✅ |
| Clasificar datos semiestructurados | ✅ |
| Clasificar datos no estructurados | ✅ |
| Pregunta de analítica descriptiva | ✅ |
| Pregunta de analítica predictiva | ✅ |
| Diagrama Fuente → Almacenamiento → Análisis → Visualización | ✅ |
| 2 frases en inglés | ✅ |
| Explicación del caso | ✅ |
| Conclusión | ✅ |
