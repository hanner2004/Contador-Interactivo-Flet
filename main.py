import flet as ft


class ContadorApp:

    def __init__(self, page):
        self.page = page
        self.contador = 0

        self.texto = ft.Text(
            value="0",
            size=50,
            weight=ft.FontWeight.BOLD
        )

    def aumentar(self, e):
        self.contador += 1
        self.actualizar()

    def disminuir(self, e):
        self.contador -= 1
        self.actualizar()

    def reiniciar(self, e):
        self.contador = 0
        self.actualizar()

    def actualizar(self):
        self.texto.value = str(self.contador)
        self.page.update()

    def construir(self):
        self.page.title = "Contador Interactivo"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.page.add(
            ft.Column(
                controls=[
                    ft.Text(
                        "MI CONTADOR",
                        size=25,
                        weight=ft.FontWeight.BOLD
                    ),
                    self.texto,
                    ft.Row(
                        controls=[
                            ft.Button(
                                "Aumentar",
                                on_click=self.aumentar
                            ),
                            ft.Button(
                                "Disminuir",
                                on_click=self.disminuir
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Button(
                        "Reiniciar",
                        on_click=self.reiniciar
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            )
        )


def main(page: ft.Page):
    aplicacion = ContadorApp(page)
    aplicacion.construir()


ft.run(main)