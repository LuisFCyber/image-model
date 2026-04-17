# Explicação técnica do código de verificação de número primo

## Objetivo

O arquivo `num_primo.py` contém uma função `is_prime` que verifica se um número inteiro é primo e uma função `main` que solicita a entrada do usuário para fazer a validação.

## Estrutura geral

- `is_prime(number: int) -> bool`: função que retorna `True` quando `number` é primo.
- `main() -> None`: função que lê a entrada do usuário, valida o valor e imprime o resultado.
- `if __name__ == "__main__":`: garante que o programa execute `main()` apenas quando o arquivo for rodado diretamente.

## Detalhes da função `is_prime`

1. `if number <= 1:`
   - Números menores ou iguais a 1 não são primos.
   - A função retorna `False` imediatamente nesses casos.

2. `if number <= 3:`
   - Os números 2 e 3 são primos.
   - Essa verificação evita testes extras para valores pequenos.

3. `if number % 2 == 0:`
   - Verifica se o número é par.
   - Todos os números pares maiores que 2 não são primos.

4. `max_divisor = int(number ** 0.5)`
   - Calcula a raiz quadrada de `number` e usa esse valor como limite de busca.
   - Não é necessário testar divisores acima da raiz quadrada.

5. `for divisor in range(3, max_divisor + 1, 2):`
   - Testa apenas divisores ímpares, começando em 3.
   - Isso reduz o número de verificações porque já descartamos os pares.

6. `if number % divisor == 0:`
   - Se `number` for divisível por algum divisor, ele não é primo.
   - Retorna `False` imediatamente.

7. `return True`
   - Se nenhum divisor foi encontrado até a raiz quadrada, o número é primo.

## Detalhes da função `main`

1. `raw_input = input("Digite um número inteiro para verificar se é primo: ")`
   - Solicita que o usuário digite um valor pelo teclado.

2. `number = int(raw_input)` dentro do `try`:
   - Converte a entrada para inteiro.
   - Se a entrada não for um número inteiro válido, o programa trata o erro e informa o usuário.

3. `if is_prime(number):`
   - Chama a função `is_prime` com o número fornecido.
   - Exibe se o valor é primo ou não.

## Importações

- Não é necessário importar nenhum módulo externo.
- O código usa funções internas do Python: `input`, `int`, `print` e operadores aritméticos.

## Como testar

Execute o arquivo com Python:

```bash
python num_primo.py
```

Depois, digite um número inteiro quando o programa solicitar. Ele informará se o número é primo ou não.
