# controle_temperatura.py

celsius = []
fahrenheit = []

print("--- Controle de Temperaturas ---")
while True:
    entrada = input("Digite a temperatura em ºC (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        break
        
    try:
        temp_c = float(entrada)
        celsius.append(temp_c)
        
        # Convertendo para Fahrenheit e adicionando na segunda lista
        temp_f = (temp_c * 1.8) + 32
        fahrenheit.append(temp_f)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Calculando e exibindo as médias
if len(celsius) > 0:
    media_c = sum(celsius) / len(celsius)
    media_f = sum(fahrenheit) / len(fahrenheit)
    
    print("\n--- Resultados ---")
    print(f"Média das temperaturas em Celsius: {media_c:.2f} ºC")
    print(f"Média das temperaturas em Fahrenheit: {media_f:.2f} ºF")
else:
    print("\nNenhuma temperatura foi registrada.")
