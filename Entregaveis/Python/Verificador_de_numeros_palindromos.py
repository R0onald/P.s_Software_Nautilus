def eh_palindromo(numero):
    return str(numero) == str(numero)[::-1]

# Exemplo de uso:
numero = 12321
print(eh_palindromo(numero))  # Saída: True
