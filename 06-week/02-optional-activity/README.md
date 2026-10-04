# Entrega Semana 06 — ERD de Sistema de Ventas

## 1. Modelo entidad-relación

### Entidades
- Cliente
- Pedido
- Producto
- DetallePedido

### Relaciones
- Cliente — Pedido: 1:N. Un cliente puede realizar muchos pedidos.
- Pedido — Producto: N:M. Un pedido puede contener muchos productos y un producto puede estar en muchos pedidos.
- La relación N:M se resuelve mediante DetallePedido.
- DetallePedido — Producto: N:1.

### Claves

**Cliente**
- PK: `id_cliente`

**Pedido**
- PK: `id_pedido`
- FK: `id_cliente`

**Producto**
- PK: `id_producto`

**DetallePedido**
- PK compuesta: `id_pedido`, `id_producto`
- FK: `id_pedido`
- FK: `id_producto`

## 2. Decisión relacional / NoSQL

Se utilizaría un enfoque **relacional** porque los datos tienen una estructura definida y existen relaciones claras entre las entidades. Las claves primarias y foráneas permiten mantener la integridad de los datos y representar correctamente la relación N:M entre pedidos y productos.

## 3. Normalización

Se aplicó una normalización básica para evitar la repetición de información. Los datos de los clientes se almacenan una sola vez en `Cliente` y los datos de los productos una sola vez en `Producto`. `Pedido` utiliza `id_cliente` como clave foránea y `DetallePedido` utiliza las claves de pedido y producto para representar la relación entre ambas entidades.

Esto reduce la duplicidad y facilita el mantenimiento de la información.
