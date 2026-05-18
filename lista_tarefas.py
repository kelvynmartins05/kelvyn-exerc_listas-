# lista_tarefas.py

tarefas = []

print("--- Cadastro de Tarefas ---")
while True:
    tarefa = input("Digite uma tarefa (ou digite 'fim' para encerrar): ")
    
    if tarefa.lower() == 'fim':
        break
        
    tarefas.append(tarefa)

# Exibindo todas as tarefas
print("\n--- Suas Tarefas ---")
if len(tarefas) > 0:
    for t in tarefas:
        print(f"- {t}")
else:
    print("Nenhuma tarefa foi cadastrada.")
