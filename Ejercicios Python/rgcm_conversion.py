class conversor:
    def cuerpo(self):
        si = input("¿Que va a convertir? Celsius = C Farenheit = F ")
        print("")
        if si == "C":
            celsius = float(input("Ingresa Una Temperatura En Celsius: "))
            print("")
            fahrenheit = (celsius * 9/5) + 32
            print('%.2f Celsius es: %0.2f Fahrenheit' %(celsius, fahrenheit))
        else:
            fahrenheit = float(input("Ingresa Una Temperatura En fahrenheit: "))
            print("")
            celsius = (fahrenheit - 32) * 5/9
            print('%.2f Fahrenheit es: %0.2f Celsius' %(fahrenheit, celsius))
            print("")
        print("¡Hasta la próxima!")

calcular = conversor()
calcular.cuerpo()
