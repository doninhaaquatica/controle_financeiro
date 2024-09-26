"""my app"""

import flet as ft
from time import sleep


def main(page: ft.Page):
    def remover_digito(valor_atual: str):
        # Remove a vírgula, os pontos de milhar e o último dígito
        start = False
        novo_valor = valor_atual.replace(",", "").replace(".", "")[:-1]

        # Garante que o valor tenha pelo menos dois dígitos
        if len(novo_valor) < 3:
            start = True
        if len(novo_valor) < 2:
            novo_valor = "0" + novo_valor
        if len(novo_valor) < 1:
            novo_valor = "00"

        # Formata o valor para ter duas casas decimais
        valor_formatado = (
            ((f"{int(novo_valor[:-2]):,}".replace(",", ".")) if not start else "0")
            + ","
            + f"{novo_valor[-2:]}"
        )

        return valor_formatado

    def adicionar_digito(valor_inicial, digito):
        # Remove a vírgula e o ponto para tratar o valor como um número inteiro
        novo_valor = valor_inicial.replace(".", "").replace(",", "") + str(digito)

        # Formata o valor para ter duas casas decimais
        parte_inteira = novo_valor[:-2]
        parte_decimal = novo_valor[-2:]
        valor_formatado = (
            f"{int(parte_inteira):,}".replace(",", ".") + "," + parte_decimal
        )

        return valor_formatado

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    valor = ft.TextField(
        prefix_text="R$ ", value="0,00", label="Entre com o valor", read_only=True
    )
    text = ft.Text()

    def on_keyboard(e: ft.KeyboardEvent):

        try:
            text.value = int(e.key)
            valor.value = adicionar_digito(valor.value, str(int(e.key)))

        except ValueError:
            text.value = e.key
            if text.value.startswith("Numpad "):
                num_pad = e.key.removeprefix("Numpad ")
                text.value = num_pad
                valor.value = adicionar_digito(valor.value, num_pad)
            pass
        if e.key == "Backspace":
            print(valor.value)
            valor.value = remover_digito(valor.value)
            print(valor.value)

        # {e.shift}{e.control}{e.alt}"
        page.update()

    page.on_keyboard_event = on_keyboard
    page.add(valor, text)


if __name__ == "__main__":
    ft.app(main)
