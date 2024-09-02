def Descuento(PrecioVenta):

    if PrecioVenta > 500:
        DescuentoVenta = "10%"
    elif (PrecioVenta >= 100 and PrecioVenta <= 500):
        DescuentoVenta = "5%"
    else:
        DescuentoVenta = "0"
    return DescuentoVenta



PrecioVentas = [100,45,432,530]

for Precio in PrecioVentas:
    print(Descuento(Precio))