def sistema_envio(distancia, unidades):
    if distancia > 1000:
        tipo_envio = "largo"
    else:
        tipo_envio = "rápido"
    
    if tipo_envio == "rápido":
        bodega = "Bodega_A"
    else:
        bodega = "Bodega_B"
    
    if bodega == "Bodega_A" and unidades > 500:
        print("Error: la bodega A no puede almacenar más de 500 unidades.")
    elif bodega == "Bodega_B" and unidades > 500:
        print("Error: la bodega B no puede almacenar más de 500 unidades.")
    else:
        print(f"Se enviarán {unidades} unidades por un envío {tipo_envio} a la bodega {bodega}.")
