# Recebendo dois dados diferentes do usuário, no caso o nome e o sobrenome e concatenando-os em uma única string

# Saudações e solicitação para o usuário se identificar
print("Olá! Vamos iniciar o projeto.")

# Recebendo os dados do usuário
dado1 = input("Por favor, digite seu nome: ")
dado2 = input("Agora, digite seu sobrenome: ")

# Verificando se o usuário inseriu os dados corretamente
if dado1 and dado2:
    print(f"Bem-vindo(a), {dado1} {dado2}! Vamos dar início no projeto.")
else:
    print("Por favor, forneça o nome quanto o sobrenome.")
