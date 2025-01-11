# Agora vamos calcular a média de três notas fornecidas na entrada do usuário.
# Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

# Recebendo as notas do usuário
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3) / 3

# Exibindo a média
print(f"A média das suas notas é: {media:.2f}")
