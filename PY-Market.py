import csv

# Función para cargar los productos desde un archivo CSV
def cargar_productos(ruta_archivo):
    productos = []
    try:
        with open(ruta_archivo, mode='r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            print(f"Encabezados del archivo: {lector_csv.fieldnames}")  # Ver los encabezados leídos
            for fila in lector_csv:
                # Convertimos el precio y porcentaje_descuento a float para cálculos posteriores
                producto = {
                    'nombre': fila['nombre_producto'],  # Cambié 'nombre' por 'nombre_producto'
                    'precio': float(fila['precio']),
                    'porcentaje_descuento': float(fila['porcentaje_descuento'])
                }
                productos.append(producto)
    except FileNotFoundError:
        print("Error: No se encontró el archivo especificado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return productos

# Función para calcular el precio promedio de los productos
def calcular_precio_promedio(productos):
    if not productos:
        return 0
    total = sum(producto['precio'] for producto in productos)
    promedio = total / len(productos)
    return promedio

# Función para aplicar un descuento usando lambda
def aplicar_descuento(productos):
    aplicar_descuento_lambda = lambda precio, descuento: precio * (1 - descuento)
    # Aplicamos el descuento a cada producto usando el porcentaje de descuento
    for producto in productos:
        descuento = producto['porcentaje_descuento'] / 100  # Convertimos el porcentaje a decimal
        producto['precio'] = aplicar_descuento_lambda(producto['precio'], descuento)
    return productos

# Función principal
def main():
    # Cargar los productos desde el archivo con la ruta especificada
    productos = cargar_productos('G:\\Ruta\\productos.csv')
    
    # Calcular y mostrar el precio promedio de los productos
    precio_promedio = calcular_precio_promedio(productos)
    print(f"Precio promedio de los productos: ${precio_promedio:.2f}")
    
    # Aplicar descuento a todos los productos y mostrar los resultados
    productos_con_descuento = aplicar_descuento(productos)
    print("Productos con descuento aplicado:")
    for producto in productos_con_descuento:
        print(f"{producto['nombre']}: ${producto['precio']:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
