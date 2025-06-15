# Programa tradicional para calcular el promedio semanal del clima

def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura para cada día de la semana:")
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        temp = float(input(f"Temperatura del {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
