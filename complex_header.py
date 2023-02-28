import flet as ft

def main(page: ft.Page):
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
                ft.DataColumn(ft.Text("Name")),  
                ft.DataColumn(ft.Text("City")),                
                ft.DataColumn(ft.Text("Index"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                        ft.DataCell(ft.Text("USA")),
                        ft.DataCell(ft.Text("New York")),
                        ft.DataCell(ft.Text("123456")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                        ft.DataCell(ft.Text("Brazil")),
                        ft.DataCell(ft.Text("Brasilia")),
                        ft.DataCell(ft.Text("23456")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                        ft.DataCell(ft.Text("Mexico")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("123456")),
                    ],
                ),               
            ],
        ),
    )

ft.app(target=main)