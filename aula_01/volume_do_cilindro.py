#formula para calcular o volume do cilindro PI * RAIO**2 * ALTURA
import math

raio = int(input("Informe o raio do cilindro: " + "\n"))
altura = int(input("Informe a altura do cilindro: " + "\n"))

volume = (3.14 * raio**2) * altura

print("Volume: " + str(volume))

