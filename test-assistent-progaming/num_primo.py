def is_prime(number: int) -> bool:
    """Retorna True se number for primo, caso contrário False."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False

    max_divisor = int(number ** 0.5)
    for divisor in range(3, max_divisor + 1, 2):
        if number % divisor == 0:
            return False
    return True


def main() -> None:
    raw_input = input("Digite um número inteiro para verificar se é primo: ")
    try:
        number = int(raw_input)
    except ValueError:
        print("Entrada inválida. Por favor, informe um número inteiro.")
        return

    if is_prime(number):
        print(f"O número {number} é primo.")
    else:
        print(f"O número {number} não é primo.")


if __name__ == "__main__":
    main()