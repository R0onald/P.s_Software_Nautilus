def maior_divisor_primo(numero):
    def eh_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for divisor in range(numero // 2, 1, -1):
        if numero % divisor == 0 and eh_primo(divisor):
            return divisor
    return None

# Exemplo de uso:
numero = 84
print(maior_divisor_primo(numero))  # Saída: 7
