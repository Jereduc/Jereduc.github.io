import datetime

def reposicion_ingredientes(faltantes):
    """Subproceso: reposición de ingredientes"""
    print("\n--- SUBPROCESO: REPOSICIÓN DE INGREDIENTES ---")
    while faltantes:
        print(f"Faltan los siguientes ingredientes: {', '.join(faltantes)}")
        print("Consultando inventario... Realizando pedido de reposición...")
        for ing in faltantes[:]:
            respuesta = input(f"¿Ha llegado el ingrediente '{ing}'? (si/no): ").lower()
            if respuesta == "si":
                faltantes.remove(ing)
        if faltantes:
            print("Aún faltan ingredientes. Esperando llegada...")
    print("Todos los ingredientes están disponibles. Continuando con el proceso...\n")

def gestionar_pedido():
    print("=== SISTEMA DE GESTIÓN DE PEDIDOS - PASTELERÍA UNIVERSITARIA DELICIATEC ===")
    
    nombre = input("Ingrese el nombre del cliente: ")
    tipo_pastel = input("Tipo de pastel (pequeño / mediano / grande): ").lower()
    horas_entrega = int(input("¿En cuántas horas desea el pastel?: "))

    if horas_entrega < 4:
        print("\nEl pedido debe realizarse con al menos 4 horas de anticipación.")
        decision = input("¿Desea servicio exprés con recargo del 20%? (si/no): ").lower()
        if decision != "si":
            print("Pedido rechazado por no cumplir con el tiempo mínimo.\n")
            return
        else:
            print("Servicio exprés confirmado con recargo del 20%.\n")

    print("Verificando disponibilidad en el horno...")
    capacidad_actual = int(input("Ingrese número actual de pasteles en el horno (0-4): "))
    if capacidad_actual >= 4:
        print("La tanda actual está llena. Verificando siguiente tanda...")
        siguiente_tanda = int(input("Número de pasteles en la siguiente tanda (0-4): "))
        if siguiente_tanda >= 4:
            print("No hay espacio disponible en el horno. Pedido pendiente por capacidad.\n")
            return
        else:
            print("Pedido agendado para la siguiente tanda disponible.\n")
    else:
        print("Espacio disponible en el horno.\n")

    ingredientes = ["harina", "azúcar", "huevos", "frutas", "mantequilla"]
    faltantes = []
    print("Verificando disponibilidad de ingredientes...\n")
    for ing in ingredientes:
        disponible = input(f"¿Hay {ing}? (si/no): ").lower()
        if disponible != "si":
            faltantes.append(ing)

    if faltantes:
        reposicion_ingredientes(faltantes)

    print("\nIniciando preparación del pastel...")
    print("→ Mezclando ingredientes")
    print("→ Horneando pastel...")
    fallo = input("¿Ocurrió un fallo en el horno? (si/no): ").lower()
    if fallo == "si":
        print("\n--- SUBPROCESO: REPROGRAMAR PEDIDO ---")
        print("Fallo detectado. Pedido reprogramado para la siguiente tanda disponible.\n")
        return
    print("→ Enfriando pastel")
    print("→ Decorando pastel")
    print("Pastel listo para entrega.\n")

    confirmacion = input("¿El cliente confirmó su retiro en las próximas 2 horas? (si/no): ").lower()
    if confirmacion == "si":
        print(f"Pedido de {nombre} completado y entregado con éxito.\n")
    else:
        print("Pedido no retirado. Movido al inventario de sobrantes.\n")

    print("=== FIN DEL PROCESO ===")

gestionar_pedido()