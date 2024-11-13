class EquipoDeportivo:
    def __init__(self, nombre, fecha_creacion, precio, descripcion, precio_costo, precio_venta, cantidad_stock):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.precio = precio
        self.descripcion = descripcion
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.cantidad_stock = cantidad_stock

    def vender(self, cantidad_vendida):
        if cantidad_vendida > self.cantidad_stock:
            print(f"No hay suficiente stock para vender {cantidad_vendida} {self.nombre}.")
        else:
            self.cantidad_stock -= cantidad_vendida
            print(f"Se vendieron {cantidad_vendida} {self.nombre}. Cantidad en stock actual: {self.cantidad_stock}")

    def __str__(self):
        return f"Nombre: {self.nombre}\nFecha de creación: {self.fecha_creacion}\nPrecio: ${self.precio}\nDescripción: {self.descripcion}\nPrecio costo: ${self.precio_costo}\nPrecio venta: ${self.precio_venta}\nCantidad en stock: {self.cantidad_stock}"


class ControlStock:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def imprimir_equipos(self):
        for equipo in self.equipos:
            print(equipo)
            print("------------------------")

    def vender_equipo(self, nombre_equipo, cantidad_vendida):
        for equipo in self.equipos:
            if equipo.nombre == nombre_equipo:
                equipo.vender(cantidad_vendida)
                break
        else:
            print(f"No se encontró el equipo {nombre_equipo}.")


# Crear un control de stock
control_stock = ControlStock()

# Agregar equipos
control_stock.agregar_equipo(EquipoDeportivo("Pelota de fútbol", "2022-01-01", 100, "Pelota de fútbol de alta calidad", 50, 100, 10))
control_stock.agregar_equipo(EquipoDeportivo("Bicicleta", "2022-02-01", 500, "Bicicleta de montaña", 300, 500, 5))

# Imprimir equipos
print("Equipos en stock:")
control_stock.imprimir_equipos()

# Vender equipos
control_stock.vender_equipo("Pelota de fútbol", 3)
control_stock.vender_equipo("Bicicleta", 2)

# Imprimir equipos actualizados
print("Equipos en stock después de ventas:")
control_stock.imprimir_equipos()