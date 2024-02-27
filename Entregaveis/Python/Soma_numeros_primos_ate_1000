def soma_primos_ate_limite(limite):
    def eh_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    soma = 0
    for num in range(2, limite):
        if eh_primo(num):
            soma += num
    return soma

# Exemplo de uso:
limite = 1000
print(soma_primos_ate_limite(limite))  # Saída: 76127
