# Projeto com Site e Exercícios de Python

Este repositório reúne um pequeno projeto contendo páginas HTML e exercícios de programação em Python com explicações associadas. O foco principal está nas práticas de lógica, refatoração, validação de entrada e debugging.

## Estrutura do projeto

- `index.html` / `index2.html`
  - Páginas HTML principais do projeto.
- `test-assistent-progaming/`
  - Pasta com exercícios Python e explicações relacionadas.
- `image-model/`
  - Estrutura alternativa que replica a pasta `test-assistent-progaming` e inclui também as mesmas páginas HTML.

## Conteúdo principal

### `test-assistent-progaming/` e `image-model/test-assistent-progaming/`

Essas pastas contêm três práticas educativas:

1. `pratica01/`
   - `num_primo.py` - Verifica se um número inteiro é primo.
   - `explicacao_numprimo.md` - Explicação técnica do funcionamento da função de verificação de primo.

2. `pratica02/`
   - `refratoriacao.py` - Calcula estatísticas de uma lista de números (`total`, `average`, `maximum`, `minimum`).
   - `explicacao_refatoracao.md` - Documenta as melhorias de refatoração aplicadas ao código.

3. `pratica03/`
   - `debug.py` - Programa de cálculo de total com desconto, incluindo validação de entrada e tratamento de erros.
   - `explicacao-debug.md` - Explicação dos erros corrigidos e das boas práticas implementadas.

4. `explicacao-linha-a-linha.md`
   - Análise detalhada passo a passo de um código Python de estatísticas.

## Como executar os exercícios

O projeto usa Python 3.10 ou superior, devido ao uso de anotações de tipo como `float | int | None`.

Execute um exercício por vez na raiz do projeto:

```bash
python test-assistent-progaming/num_primo.py
python test-assistent-progaming/refratoriacao.py
python image-model/test-assistent-progaming/pratica03/debug.py
```

Se preferir usar a cópia dentro de `image-model`, altere o caminho para a pasta correspondente.

## Descrição dos scripts

### `num_primo.py`
- Função `is_prime(number: int) -> bool`:
  - Verifica números menores ou iguais a 1 como não primos.
  - Trata 2 e 3 como primos.
  - Descarta pares maiores que 2.
  - Testa apenas divisores ímpares até a raiz quadrada do número.
- `main()` lê a entrada do usuário, valida o inteiro e exibe o resultado.

### `refratoriacao.py`
- Função `calculate_statistics(numbers)`:
  - Verifica se a lista está vazia e lança `ValueError` quando necessário.
  - Calcula o total com `sum()`.
  - Calcula a média dividindo o total pelo número de elementos.
  - Determina máximo e mínimo com `max()` e `min()`.
- `main()` demonstra o uso da função com uma lista fixa de valores.

### `debug.py`
- `obter_entrada_numerica(mensagem, tipo)`:
  - Solicita entrada do usuário e converte para `int` ou `float`.
  - Retorna `None` em caso de conversão inválida.
- `calcular_total_com_desconto(preco, quantidade, percentual_desconto)`:
  - Calcula `subtotal` e aplica desconto percentual.
- `main()`:
  - Coleta nome, preço, quantidade e percentual de desconto.
  - Valida entradas e intervalo do desconto.
  - Exibe o total final ou mensagem de erro.

## Observações

- Há duas versões da mesma estrutura de exercícios: uma em `test-assistent-progaming/` e outra em `image-model/test-assistent-progaming/`.
- As explicações estão em arquivos Markdown para facilitar o estudo e a revisão do código.

## Sugestões de melhorias

- Unificar as duplicações de pasta entre `test-assistent-progaming/` e `image-model/test-assistent-progaming/`.
- Adicionar um `requirements.txt` caso o projeto passe a usar bibliotecas externas.
- Criar testes automatizados para validar cada função Python.
