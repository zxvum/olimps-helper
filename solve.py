# Пример сторонней функции
def check_prime(n) -> []:
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def main(data):
    return check_prime(data) # тут верните строку
