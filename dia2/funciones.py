def saludar (nombre):
    print("hola,", nombre)

def presupuesto(diario,dias):
    return diario * dias

saludar("Richard")
saludar("outlier")

total = presupuesto (15, 10)
print ("Presupuesto:", total)