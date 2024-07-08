import flet as ft
import webbrowser

def main(page: ft.Page):
    page.title = "Doctor Finder"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # List of doctor types
    doctor_types = ["General Physician", "Gynecologist", "Pediatrician", "Dermatologist"]

    # Dropdown for selecting doctor type
    doctor_dropdown = ft.Dropdown(
        label="Select Doctor Type",
        options=[ft.dropdown.Option(doctor) for doctor in doctor_types]
    )

    # Function to handle search button click
    def search_doctor(e):
        selected_doctor = doctor_dropdown.value
        if selected_doctor:
            search_query = f"{selected_doctor} near me"
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

    # Search button
    search_button = ft.ElevatedButton(
        text="Search",
        on_click=search_doctor
    )

    # Add components to the page
    page.add(
        ft.Column(
            controls=[
                ft.Text("Find a Doctor", size=36, weight=ft.FontWeight.BOLD),
                doctor_dropdown,
                search_button
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
