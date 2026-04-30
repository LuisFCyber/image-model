# Explicação da Refatoração

O código original fazia o cálculo do total, da média, do maior e do menor valor de uma lista usando dois loops `for` e variáveis pouco descritivas.

## Melhorias aplicadas

1. Renomeação de função e variáveis
   - A função original `c` foi renomeada para `calculate_statistics`, tornando claro que ela calcula estatísticas de uma lista numérica.
   - As variáveis como `t`, `m`, `mx`, `mn` e `c2` foram substituídas por nomes descritivos como `total`, `average`, `maximum` e `minimum`.

2. Uso de funções built-in
   - O cálculo do total passou a usar `sum(numbers)` em vez de somar manualmente em um laço.
   - O maior e o menor valor passaram a ser obtidos com `max(numbers)` e `min(numbers)`, tornando o código mais curto e mais legível.

3. Validação de entrada
   - Adicionou-se uma verificação para impedir o processamento de listas vazias: `if not numbers: raise ValueError(...)`.
   - Isso evita divisão por zero e deixa o comportamento da função mais seguro.

4. Organização do fluxo principal
   - O bloco principal foi movido para uma função `main()` e protegido com `if __name__ == "__main__":`, o que facilita o reuso do código como módulo.
   - A lista de valores foi mantida, mas o cálculo e a impressão foram separados em etapas claras.

## Resultado

O arquivo `refratoriacao.py` agora contém:

- `calculate_statistics(numbers)` para computar total, média, máximo e mínimo;
- verificação de entrada vazia;
- `main()` para execução principal;
- melhoria na legibilidade e manutenção do código.

Essas mudanças tornam o programa mais robusto, mais fácil de entender e menos propenso a erros.
