# Solicitado como entrada dois números e depois será realizado uma operação matemática entre eles como
# se fosse uma calculadora.

# Apresentação
print("Bem-vindo(a) à calculadora Python!")

# Recebendo os números e a operação
numero1 = float(input("Digite o primeiro número: "))
operacao = input("Escolha a operação matématica (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))

# Realizando a operação
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 == 0:
        print("Erro: Não é possível dividir por zero.")
    else:
        resultado = numero1 / numero2
else:
    print("Operação inválida!")

# Exibindo o resultado
if operacao in ["+", "-", "*", "/"]:
    print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")
