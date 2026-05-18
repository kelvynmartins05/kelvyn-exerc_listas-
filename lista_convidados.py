# lista_convidados.py

convidados = []

# Cadastrando 5 convidados
print("--- Cadastro de Convidados ---")
for i in range(5):
    nome = input(f"Digite o nome do {i+1}º convidado: ")
    convidados.append(nome)

# Exibindo todos os convidados
print("\n--- Lista de Convidados ---")
for convidado in convidados:
    print(f"- {convidado}")

# Informando a quantidade total
print(f"\nTotal de convidados na lista: {len(convidados)}")
