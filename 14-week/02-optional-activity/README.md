# Ciencia de Datos — Semana 14
## Optimización de medidas DAX — TRANSPORTES MT

**Opción elegida:** B) DAX en Power BI.

**Objetivo:** crear dos medidas que permitan analizar el total de ventas y la participación de cada tipo de servicio. Se utiliza una empresa ficticia y un modelo de datos ilustrativo.

### Modelo de datos necesario
Importa una tabla llamada `Ventas` con estas columnas: `Fecha`, `Agencia`, `Tipo_Servicio`, `Valor_Venta`. La columna `Valor_Venta` debe ser numérica.

### Antes: cálculos manuales
- Total de ventas: sumar manualmente los valores de `Valor_Venta` en una hoja de cálculo.
- Participación: dividir manualmente las ventas de cada servicio entre las ventas totales y multiplicar por 100.

**Limitación:** los cálculos manuales deben actualizarse cuando cambian los registros o los filtros.

### Después: dos medidas DAX

**Medida 1 — Total Ventas**
```dax
Total Ventas = SUM(Ventas[Valor_Venta])
```
Suma las ventas respetando los filtros activos (por ejemplo, mes, agencia o servicio).

**Medida 2 — % Participacion**
```dax
% Participacion =
DIVIDE(
    [Total Ventas],
    CALCULATE(
        [Total Ventas],
        REMOVEFILTERS(Ventas[Tipo_Servicio])
    ),
    0
)
```
Calcula la participación de cada tipo de servicio sobre el total de los servicios, manteniendo los demás filtros del informe. Formatea esta medida como **Porcentaje** en Power BI. No multipliques por 100 en la fórmula.

### ¿Por qué mejora?
Las medidas DAX se recalculan automáticamente con los filtros y nuevos datos del modelo, evitando actualizar sumas y porcentajes manualmente. `SUM` agrega el valor de ventas y `DIVIDE` maneja de forma segura la división por cero. `REMOVEFILTERS` elimina solo el filtro de tipo de servicio del denominador, por lo que la comparación mantiene filtros como fecha y agencia.

**Nota:** esta propuesta mejora la mantenibilidad y el análisis interactivo; no se afirma que reduzca el tiempo de ejecución sin medirlo.

### Comprobación en Power BI
1. Importa la tabla `Ventas` con las columnas indicadas.
2. En **Modelado > Nueva medida**, crea cada medida con el código DAX.
3. Inserta una tarjeta con `Total Ventas` y una tabla con `Tipo_Servicio`, `Total Ventas` y `% Participacion`.
4. Agrega un segmentador por `Agencia` o `Fecha` y verifica que las medidas cambien.
5. Si se muestran todos los servicios y no hay otros filtros por servicio, la suma de los porcentajes debe ser 100 % (salvo diferencias por redondeo).

### Entrega en GitHub
Sube esta carpeta `14-week` a tu fork del repositorio de la clase. Mensaje del commit: `Entrega semana 14`.
