import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#363636"
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 400
    page.title = "Calculadora"
    page.vertical_alignment.SPACE_EVENLY
    page.window_always_on_top = True

    result = ft.Text(value="0", color="#FFFFFF", size=20)

    page.add(

        ft.Row(
            width=300,
            alignment="end",
            controls=[result]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.ElevatedButton(text="%", bgcolor="#000000"),
                ft.ElevatedButton(text="AC", bgcolor="#000000"),
                ft.ElevatedButton(text="C", bgcolor="#000000"),
                ft.ElevatedButton(text="/", bgcolor="#000000")]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

            controls=[
                ft.ElevatedButton(text="7", bgcolor="#1C1C1C",style=ft.ButtonStyle(
                shape=ft.CircleBorder(3)
            )),
                ft.ElevatedButton(text="8", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text="9", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text="x", bgcolor="#000000")]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.ElevatedButton(text="4", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text="5", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text="6", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text="-", bgcolor="#000000")]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.ElevatedButton(text="1", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text="2", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text="3", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text="+", bgcolor="#000000")]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.ElevatedButton(text="+/-", bgcolor="#000000"),
                ft.ElevatedButton(text="0", bgcolor="#1C1C1C"),
                ft.ElevatedButton(text=",", bgcolor="#000000"),
                ft.ElevatedButton(text="=", bgcolor="#000000")]
        )

    )

ft.app(target=main)