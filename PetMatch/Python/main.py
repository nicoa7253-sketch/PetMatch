# ====================================
# PETMATCH - Ecommerce de mascotas
# ====================================


productos = []


# ------------------------------------
# GUARDAR PRODUCTOS EN ARCHIVO
# ------------------------------------

def guardar_productos():

    archivo = open("productos.txt", "w")


    for producto in productos:

        linea = (
            str(producto["idProducto"]) + ";" +
            producto["nombreProducto"] + ";" +
            producto["categoria"] + ";" +
            producto["tipoMascota"] + ";" +
            producto["edad"] + ";" +
            producto["descripcion"] + ";" +
            str(producto["personalizable"]) + ";" +
            str(producto["precio"]) + ";" +
            str(producto["stock"]) + ";" +
            producto["proveedor"] + "\n"
        )


        archivo.write(linea)


    archivo.close()



# ------------------------------------
# CARGAR PRODUCTOS DEL ARCHIVO
# ------------------------------------

def cargar_productos():

    try:

        archivo = open("productos.txt", "r")


        for linea in archivo:


            datos = linea.strip().split(";")



            producto = {

                "idProducto": int(datos[0]),
                "nombreProducto": datos[1],
                "categoria": datos[2],
                "tipoMascota": datos[3],
                "edad": datos[4],
                "descripcion": datos[5],
                "personalizable": datos[6] == "True",
                "precio": float(datos[7]),
                "stock": int(datos[8]),
                "proveedor": datos[9]

            }


            productos.append(producto)



        archivo.close()



    except FileNotFoundError:

        pass




# ------------------------------------
# AGREGAR PRODUCTO
# ------------------------------------

def agregar_producto():

    idProducto = len(productos) + 1


    print("\n--- AGREGAR PRODUCTO ---")


    nombre = input("Nombre del producto: ")

    categoria = input("Categoria: ")

    tipoMascota = input("Tipo de mascota: ")

    edad = input("Edad recomendada (Cachorro/Adulto/Senior): ")

    descripcion = input("Descripcion: ")



    respuesta = input("¿Es personalizable? (si/no): ")



    if respuesta.lower() == "si":

        personalizable = True

    else:

        personalizable = False



    precio = float(input("Precio: "))


    stock = int(input("Stock disponible: "))


    proveedor = input("Proveedor: ")




    producto = {


        "idProducto": idProducto,

        "nombreProducto": nombre,

        "categoria": categoria,

        "tipoMascota": tipoMascota,

        "edad": edad,

        "descripcion": descripcion,

        "personalizable": personalizable,

        "precio": precio,

        "stock": stock,

        "proveedor": proveedor


    }



    productos.append(producto)


    guardar_productos()



    print("\nProducto agregado correctamente")

    print("ID asignado:", idProducto)





# ------------------------------------
# MOSTRAR PRODUCTOS
# ------------------------------------

def mostrar_productos():


    print("\n--- PRODUCTOS DISPONIBLES ---")



    if len(productos) == 0:


        print("No hay productos cargados")



    else:



        for producto in productos:



            print("----------------------------")


            print("ID:", producto["idProducto"])

            print("Nombre:", producto["nombreProducto"])

            print("Categoria:", producto["categoria"])

            print("Mascota:", producto["tipoMascota"])

            print("Edad:", producto["edad"])

            print("Descripcion:", producto["descripcion"])

            print("Personalizable:", producto["personalizable"])

            print("Precio: $", producto["precio"])

            print("Stock:", producto["stock"])

            print("Proveedor:", producto["proveedor"])





# ------------------------------------
# BUSCAR PRODUCTO
# ------------------------------------

def buscar_producto():


    print("\n--- BUSCAR PRODUCTO ---")



    idBuscar = int(input("Ingrese ID del producto: "))



    encontrado = False




    for producto in productos:



        if producto["idProducto"] == idBuscar:



            print("\nProducto encontrado")

            print("----------------")


            print("Nombre:", producto["nombreProducto"])

            print("Categoria:", producto["categoria"])

            print("Mascota:", producto["tipoMascota"])

            print("Edad:", producto["edad"])

            print("Precio:", producto["precio"])

            print("Stock:", producto["stock"])



            encontrado = True





    if encontrado == False:


        print("Producto no encontrado")







# ------------------------------------
# ELIMINAR PRODUCTO
# ------------------------------------

def eliminar_producto():


    print("\n--- ELIMINAR PRODUCTO ---")



    idEliminar = int(input("Ingrese ID del producto: "))



    for producto in productos:



        if producto["idProducto"] == idEliminar:



            productos.remove(producto)


            guardar_productos()


            print("Producto eliminado correctamente")


            return





    print("Producto no encontrado")






# ------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------


cargar_productos()



while True:



    print("""
    
🐾 PETMATCH

1 - Agregar producto
2 - Mostrar productos
3 - Buscar producto
4 - Eliminar producto
5 - Salir

""")


    opcion = input("Seleccione una opcion: ")




    if opcion == "1":


        agregar_producto()



    elif opcion == "2":


        mostrar_productos()



    elif opcion == "3":


        buscar_producto()



    elif opcion == "4":


        eliminar_producto()



    elif opcion == "5":


        print("Gracias por usar PetMatch")

        break



    else:


        print("Opcion incorrecta")
