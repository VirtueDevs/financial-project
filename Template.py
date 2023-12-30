def calcular_ingresos():

    ingresos_originales = int(input("Por favor escribe los ingresos totales:"))
    ingresos = ingresos_originales
  
    while True:
        pregunta = input("Tienes un egreso? (Sí / No)")


        if (pregunta.lower() == "si"): 
            egreso = int(input("Por favor indica el egreso:"))
            ingresos -=  egreso
            print(f"El total del egreso es: {ingresos}")
        else:
            print(f"El total es: {ingresos}")

        pregunta_nuevo_calculo = input("¿Quieres realizar otro cálculo? (Sí / No): ")

        if pregunta_nuevo_calculo.lower() == "no":
            print("Volviendo al menú")
            menu()

def menu():
    print("1. Consultar ingresos totales:")
    print("2. Realizar inserción de egresos")
    print("3. Salir del programa")
    respuesta = int(input("Indica la opción que necesitas: "))

    if respuesta == 1:
        calcular_ingresos()

if __name__ == '__main__':

    menu()