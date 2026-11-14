# TRANSPORTES MT | Semana 15: Storytelling del proyecto final

**Asignatura:** Ciencia de Datos · **Modalidad:** Individual · **Periodo:** 2026-B

## Storytelling: ¿En qué rutas debemos priorizar la puntualidad?

### Contexto
TRANSPORTES MT es una empresa ficticia utilizada para estudiar el comportamiento de los servicios de transporte mediante datos simulados. El archivo de trabajo contiene **1.505 registros** con información sobre fecha, ruta, tipo de servicio, agencia, distancia recorrida, minutos de retraso e ingreso en pesos colombianos. Analizar estos datos permite identificar patrones operativos y orientar decisiones de seguimiento y programación.

### Pregunta de análisis
**¿Qué ruta presenta la mayor proporción de servicios con retraso y dónde conviene concentrar las acciones de mejora?**

Para responder, se clasificó cada registro como *con retraso* cuando `retraso_min > 0`. Luego se calculó, para cada ruta, el porcentaje de servicios con retraso respecto del total de servicios registrados en esa ruta. Este indicador compara rutas con distintos volúmenes de operación.

### Hallazgo principal
De los **1.505 servicios**, **361** registraron algún retraso (**24,0 %**). La ruta **Neiva–Cartagena** presentó la mayor proporción: **73 de 186 servicios (39,2 %)**. Le siguieron **Neiva–Medellín (30,5 %)**, **Neiva–Cali (23,4 %)**, **Pitalito–Neiva (20,8 %)** y **Neiva–Bogotá (15,3 %)**.

![Neiva–Cartagena registra la mayor proporción de retrasos (39,2 %)](graficos/retrasos_por_ruta.png)

**Conclusión del gráfico:** Neiva–Cartagena es la ruta con mayor incidencia relativa de retrasos en los datos analizados; por tanto, constituye una prioridad razonable para investigar las causas de las demoras. El gráfico describe asociaciones observadas, no demuestra sus causas.

### Recomendación accionable
Se recomienda implementar un **plan piloto de seguimiento de puntualidad en la ruta Neiva–Cartagena**, con registro de hora programada y real, duración del retraso, punto de ocurrencia y causa reportada. El equipo operativo debe revisar semanalmente el porcentaje de servicios con retraso y los motivos más frecuentes, para ajustar la programación y establecer medidas preventivas. Tras cuatro semanas, se comparará el indicador con el valor de referencia del **39,2 %**; la meta inicial propuesta es reducirlo a **menos del 35 %**, sujeto a la viabilidad operativa y a la calidad de los nuevos registros.

### Consideraciones de calidad de datos
El archivo contiene **15 valores faltantes** en `tipo_servicio` y **5 identificadores de servicio repetidos**. Se conservaron los 1.505 registros para describir el conjunto suministrado; antes de tomar decisiones reales deben verificarse esos casos. Los datos son simulados y las conclusiones no representan indicadores verificados de una empresa real.

## Indicadores del tablero

| Vista | Título con conclusión | Resultado |
|---|---|---|
| KPI general | Uno de cada cuatro servicios registra retraso | 361 de 1.505 (24,0 %) |
| Comparación de rutas | Neiva–Cartagena concentra la mayor proporción de retrasos | 39,2 % |
| Calidad de datos | Hay registros que requieren validación | 15 tipos faltantes y 5 IDs repetidos |

## Archivos y reproducción

- `datos_originales.csv`: registros simulados suministrados para el proyecto.
- `analisis.py`: código reproducible para calcular los indicadores y crear el gráfico.
- `resumen_rutas.csv`: resultados agregados por ruta.
- `graficos/retrasos_por_ruta.png`: gráfico clave solicitado en la guía.

Para reproducir el análisis en Python o Google Colab, instala `pandas` y `matplotlib` y ejecuta `python analisis.py` desde la carpeta del proyecto.

**Entrega:** repositorio GitHub del proyecto individual TRANSPORTES MT, Semana 15.
