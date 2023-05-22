def aplicarAumento(precio: int) -> int:

    aumento = precio * 0.05
    precio_actualizado = precio + aumento
    return precio_actualizado

resultado = aplicarAumento(3)

