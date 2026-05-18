# controle_precos.py

precos = []

# Solicitando 5 preços
print("--- Controle de Preços ---")
for i in range(5):
    preco = float(input(f"Digite o {i+1}º preço: R$ "))
    precos.append(preco)

# Exibindo o maior e o menor preço
print(f"\nMaior preço registrado: R$ {max(precos):.2f}")
print(f"Menor preço registrado: R$ {min(precos):.2f}")
