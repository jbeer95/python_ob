peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

indice_masa_corporal = peso / (estatura ** 2)
indice_masa_corporal = round(indice_masa_corporal, 2)

print("Tu índice de masa corporal es", indice_masa_corporal)
