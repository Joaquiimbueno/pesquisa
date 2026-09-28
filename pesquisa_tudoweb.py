# Pesquisa de Opinião - TudoWeb
# Coleta a satisfação de clientes com o atendimento prestado.

# Para a entrega final use 50. Para os testes (item 6), altere para 10.
TOTAL_ENTREVISTADOS = 50

excelente = 0
bom = 0
ruim = 0

print("=" * 45)
print("   PESQUISA DE OPINIÃO - TUDOWEB")
print("=" * 45)

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\nEntrevistado {i} de {TOTAL_ENTREVISTADOS}")

    # Nome (não pode ficar vazio)
    nome = input("Nome: ").strip()
    while nome == "":
        print("Nome inválido. Digite novamente.")
        nome = input("Nome: ").strip()

    # Idade (número inteiro positivo)
    idade = input("Idade: ").strip()
    while not idade.isdigit() or int(idade) <= 0:
        print("Idade inválida. Digite um número inteiro maior que zero.")
        idade = input("Idade: ").strip()
    idade = int(idade)

    # Opinião (1, 2 ou 3)
    print("Opinião sobre o atendimento:")
    print("  1 - EXCELENTE")
    print("  2 - BOM")
    print("  3 - RUIM")
    opiniao = input("Digite a opção: ").strip()
    while opiniao not in ("1", "2", "3"):
        print("Opção inválida. Digite 1, 2 ou 3.")
        opiniao = input("Digite a opção: ").strip()

    # Estrutura de decisão para verificar a opinião
    if opiniao == "1":
        excelente += 1
        print(f"Obrigado, {nome}! Resposta registrada: EXCELENTE.")
    elif opiniao == "2":
        bom += 1
        print(f"Obrigado, {nome}! Resposta registrada: BOM.")
    else:
        ruim += 1
        print(f"Obrigado, {nome}! Resposta registrada: RUIM.")

# Resultado final
print("\n" + "=" * 45)
print("   RESULTADO DA PESQUISA")
print("=" * 45)
print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print(f"a) Respostas EXCELENTE: {excelente}")
print(f"b) Respostas RUIM: {ruim}")
