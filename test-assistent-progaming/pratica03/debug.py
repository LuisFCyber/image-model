"""
Programa de cálculo de total com desconto.
Calcula o valor total de uma compra aplicando desconto por cupom.
"""


def obter_entrada_numerica(mensagem: str, tipo: type) -> float | int | None:
    """
    Solicita entrada do usuário e converte para o tipo especificado.

    Args:
        mensagem: Mensagem a exibir para o usuário.
        tipo: Tipo para conversão (int ou float).

    Returns:
        Valor convertido ou None se houver erro na conversão.
    """
    try:
        entrada = input(mensagem)
        return tipo(entrada)
    except ValueError:
        print(f"Erro: Por favor, informe um valor numérico válido.")
        return None


def calcular_total_com_desconto(preco: float, quantidade: int,
                                percentual_desconto: float) -> float:
    """
    Calcula o total com desconto aplicado.

    Args:
        preco: Preço unitário do item.
        quantidade: Quantidade de itens.
        percentual_desconto: Percentual de desconto (0-100).

    Returns:
        Valor total após desconto.
    """
    subtotal = preco * quantidade
    desconto = subtotal * (percentual_desconto / 100)
    return subtotal - desconto


def main() -> None:
    """Função principal que executa o programa."""
    cliente = input("Qual é seu nome? ")

    # Obter preço do item 1
    preco_item = obter_entrada_numerica("Preço do item 1: R$ ", float)
    if preco_item is None:
        return

    # Obter quantidade do item 1
    quantidade_item = obter_entrada_numerica("Quantidade do item 1: ", int)
    if quantidade_item is None:
        return

    # Obter percentual de desconto
    percentual_desconto = obter_entrada_numerica(
        "Digite o percentual de desconto (0-100): ", float
    )
    if percentual_desconto is None:
        return

    # Validar percentual de desconto
    if not 0 <= percentual_desconto <= 100:
        print("Erro: O desconto deve estar entre 0 e 100%.")
        return

    # Calcular total
    total = calcular_total_com_desconto(
        preco_item, quantidade_item, percentual_desconto
    )

    # Exibir resultado
    if total > 0:
        print(f"O total para {cliente} é: R$ {total:.2f}")
    else:
        print("Erro: O total não pode ser negativo.")


if __name__ == "__main__":
    main()