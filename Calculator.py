import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#363636"
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 350
    page.title = "Calculadora"
    page.window_always_on_top = True
    result = ft.Text(value="", color="#FFFFFF", size=30)

    def keyboard(e):
        data = e.control.data
        print(data)

        if data in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "*", "/"]:
            result.value = str(result.value) + str(data)
            page.update()

        if data == "=":
            result.value = str(eval(result.value))
            page.update()

        if data == "<":
            st = list(result.value)
            st.pop()
            result.value = "".join(map(str,st))
            page.update()

        if data == "c":
            result.value = ""
            page.update()

        if data == "%":
            result.value = int(result.value) / 100
            page.update()

        if data == "+/-":
            result.value = -int(result.value)
            page.update()

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
                ft.ElevatedButton(text="C", bgcolor="#000000", data="c", on_click=keyboard),
                ft.ElevatedButton(text="<", bgcolor="#000000", data="<", on_click=keyboard),
                ft.ElevatedButton(text="+/-", bgcolor="#000000", data="+/-", on_click=keyboard),
                ft.ElevatedButton(text="/", bgcolor="#000000", data="/", on_click=keyboard)]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

            controls=[
                ft.ElevatedButton(text="7", bgcolor="#1C1C1C", data="7", on_click=keyboard),
                ft.ElevatedButton(text="8", bgcolor="#1C1C1C", data="8", on_click=keyboard),
                ft.ElevatedButton(text="9", bgcolor="#1C1C1C", data="9", on_click=keyboard),
                ft.ElevatedButton(text="x", bgcolor="#000000", data="*", on_click=keyboard)]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.ElevatedButton(text="4", bgcolor="#1C1C1C", data="4", on_click=keyboard),
                ft.ElevatedButton(text="5", bgcolor="#1C1C1C", data="5", on_click=keyboard),
                ft.ElevatedButton(text="6", bgcolor="#1C1C1C", data="6", on_click=keyboard),
                ft.ElevatedButton(text="-", bgcolor="#000000", data="-", on_click=keyboard)]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.ElevatedButton(text="1", bgcolor="#1C1C1C", data="1", on_click=keyboard),
                ft.ElevatedButton(text="2", bgcolor="#1C1C1C", data="2", on_click=keyboard),
                ft.ElevatedButton(text="3", bgcolor="#1C1C1C", data="3", on_click=keyboard),
                ft.ElevatedButton(text="+", bgcolor="#000000", data="+", on_click=keyboard)]
        ),
        ft.Row(
            width=300,
            expand=1,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.ElevatedButton(text="%", bgcolor="#000000", data="%", on_click=keyboard),
                ft.ElevatedButton(text="0", bgcolor="#1C1C1C", data="0", on_click=keyboard),
                ft.ElevatedButton(text=",", bgcolor="#000000", data=".", on_click=keyboard),
                ft.ElevatedButton(text="=", bgcolor="#000000", data="=", on_click=keyboard)]
        )

    )


ft.app(target=main)
