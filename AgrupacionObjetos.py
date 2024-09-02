
class Producto:
    def __init__(self, nombre, codigoBarras, fabricante, categoria, genero):
        
        self.nombre = nombre
        self.codigoBarras = codigoBarras
        self.fabricante = fabricante
        self.categoria = categoria
        self.genero = genero

Producto1 = Producto("Zapatos XYZ", 8569741233658, "Deportes XYZ", "Zapatos", "Masculino")
Producto2 = Producto("Zapatos ABC", 7452136985471, "Deportes XYZ", "Zapatos", "Femenino")
Producto3 = Producto("Camisa DEF", 5236412896324, "Deportes XYZ", "Camisas", "Masculino")
Producto4 = Producto("Bolso KLM", 5863219635478, "Carteras Hi-Fashion", "Bolsos", "Femenino")

Productos = [Producto1, Producto2, Producto3, Producto4]

def AgrupacionProductos(ListaProductos):
    jerarquiaProductos = {}
    x=0
    for producto in ListaProductos:
        x+=1
        if (producto.fabricante not in jerarquiaProductos) == True:
            jerarquiaProductos[producto.fabricante]={}
            if (producto.categoria not in jerarquiaProductos[producto.fabricante]) == True:
                jerarquiaProductos[producto.fabricante][producto.categoria]={}
                if(producto.genero not in jerarquiaProductos[producto.fabricante][producto.categoria]) == True:
                    jerarquiaProductos[producto.fabricante][producto.categoria][producto.genero] = [x]
        else:
            if (producto.categoria not in jerarquiaProductos[producto.fabricante]) == True:
                jerarquiaProductos[producto.fabricante][producto.categoria]={}
                if(producto.genero not in jerarquiaProductos[producto.fabricante][producto.categoria]) == True:
                    jerarquiaProductos[producto.fabricante][producto.categoria][producto.genero] = [x]
            else:
                jerarquiaProductos[producto.fabricante][producto.categoria][producto.genero] = [x]
                                
        
    return jerarquiaProductos

Diccionario = AgrupacionProductos(Productos)
print(Diccionario)