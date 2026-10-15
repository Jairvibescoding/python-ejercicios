print("calculdora de campaña")
presupuesto_diario= float(input("presupuesto diario ($): "))
dias =  int (input("cuantos dias?"))

total = presupuesto_diario * dias
print ("presupuesto total: $", round(total,2))

if total > 100:
    print ("campaña grande - revisa bien los anuncios")
else:
    print ("campaña de prueba - mide resultados pronto") 