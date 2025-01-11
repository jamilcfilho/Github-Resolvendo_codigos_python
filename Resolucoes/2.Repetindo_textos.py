# Solicitação de uma string e um número inteiro como entrada.
# Depois será retornado a string repetida vezes conforme o número informado pelo usuário.

# Solicitação de uma frase e do número de repetições
string = input("Forneça uma frase que precisa ser repetida: ")
vezes = int(input("Quantas vezes gostaria de repetir essa frase? "))

# Verificando se a entrada do número é um valor inteiro válido
if vezes < 1:
    print("Por favor, forneça um número inteiro positivo.")
else:
    exit

print((string + "\n") * vezes)
