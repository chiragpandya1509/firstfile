import flet as ft
import math
import pandas as pd
df = pd.read_csv('C:/Users/asd/Desktop/flet.csv')  # Corrected file path


def home_page(page: ft.Page):
    page.add(ft.Container(gradient=ft.LinearGradient( begin=ft.alignment.top_left, end=ft.alignment.bottom_right, colors=["#ff7e5f", "#feb47b"], ), expand=True, # This ensures the gradient fills the entire page 
                           ))
    # Create buttons to navigate to other pages
    button1 = ft.ElevatedButton("Exam List", on_click=lambda e: go_to_page(page, "page1"))
    button2 = ft.ElevatedButton("page2", on_click=lambda e: go_to_page(page, "page2"))
    button3 = ft.ElevatedButton("Page3", on_click=lambda e: go_to_page(page, "page3"))
    order = ft.ElevatedButton("Orders", on_click=lambda e: go_to_page(page, "order"))
    page6 = ft.ElevatedButton("NewPage", on_click=lambda e: go_to_page(page,"page6"))
   
    # Arrange buttons in a column with center alignment and some space between them
    page.add(
        ft.Row(  # Use Column to arrange buttons vertically
            controls=[button1, button2, button3,page6],
            alignment=ft.MainAxisAlignment.END,  # Center the buttons vertically
            spacing=20  # Add space between buttons
        )
    )
    # Arrange buttons in a column with center alignment and some space between them
    page.add(
        ft.Row(  # Use Column to arrange buttons vertically
            controls=[order],
            alignment=ft.MainAxisAlignment.END,  # Center the buttons vertically
            spacing=20  # Add space between buttons
        )
    )
    # Use Stack for positioning My Website text at specific (x, y) coordinates
    page.add(ft.Stack(controls=[ft.Container(  # Use Container inside the Stack
                    content=ft.Text(
                        value="My website",  # Text value
                        size=40,
                        weight=ft.FontWeight.W_100,
                        text_align=ft.TextAlign.END  # Text alignment
                    ),
                    left=50,  # Position of My website text (X)
                    top=0,   # Position of My website text (Y)
)]))

def page1(page: ft.Page):
    # Create a page with centered content
    back_button = ft.ElevatedButton("Back to Home", on_click=lambda e: go_to_page(page, "home"))
    
    # Arrange content in a column, center the text and button, with some spacing
    page.add(ft.Row(controls=[back_button], alignment=ft.MainAxisAlignment.END))
    page.add(ft.Row(controls=[ft.Text("Exam", size=24, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER))
    card1 = ft.Card(content=ft.Container(content=ft.Column(controls=[ft.Image(src="C:/Users/asd/Downloads/istockphoto-1973365581-612x612.jpg", expand=True,), ft.Text("Exam 1", size=18, weight=ft.FontWeight.BOLD), ft.ListTile(title=ft.Text("Physics")), ft.Row(controls=[ft.TextButton("Buy Exam",tooltip="Click on buy button"), ft.TextButton("View Details")], alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER), width=300, padding=5))
    card2 = ft.Card(content=ft.Container(content=ft.Column(controls=[ft.Image(src="C:/Users/asd/Downloads/istockphoto-1973365581-612x612.jpg", expand=True,), ft.Text("Exam 1", size=18, weight=ft.FontWeight.BOLD), ft.ListTile(title=ft.Text("Physics")), ft.Row(controls=[ft.TextButton("Buy Exam",tooltip="Click on buy button"), ft.TextButton("View Details")], alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER), width=300, padding=5))
    card3 = ft.Card(content=ft.Container(content=ft.Column(controls=[ft.Image(src="C:/Users/asd/Downloads/istockphoto-1973365581-612x612.jpg", width=400, height=300), ft.Text("Exam 2", size=18, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER), width=400, padding=10)) 
    page.add(ft.Row(controls=[card1, card2,card3], alignment=ft.MainAxisAlignment.CENTER, spacing=20))



def order(page: ft.Page):
    # Create a page with centered content
    back_button = ft.ElevatedButton("Back to Home", on_click=lambda e: go_to_page(page, "home"))
    
    # Background with gradient
    background = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.Alignment(0.8, 1),
            colors=[
                "0xff1f005c",
                "0xff5b0060",
                "0xff870160",
                "0xffac255e",
                "0xffca485c",
                "0xffe16b5c",
                "0xfff39060",
                "0xffffb56b",
            ],
            tile_mode=ft.GradientTileMode.MIRROR,
            rotation=math.pi / 3,
        ),
        expand=True,
        content=ft.Column(
            [
                ft.Row(
                    controls=[back_button],
                    alignment=ft.MainAxisAlignment.END
                ),
                ft.Text("Here you can see orders", size=24, weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20  # Space between text and back button
        ),
    )

    # Add background to the page
    page.add(background)

def page2(page: ft.Page):
    back_button = ft.ElevatedButton("Back to Home", on_click=lambda e: go_to_page(page, "home"))

    gradient_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=[ft.Text("Welcome to Page 2", size=24, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Row(controls=[back_button], alignment=ft.MainAxisAlignment.END),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        ),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#FF5733", "#C70039"]
        ),padding=20
    )

    page.add(gradient_container)
import flet as ft
import csv
import flet as ft
import csv

def page6(page: ft.Page):
    # Header row
    page.add(
        ft.Row(
            controls=[ft.Text("All Data will be shown Here", size=24, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20  # Space between text and button
        )
    )

    # Function to handle button click
    def button_clicked(e):
        # Collect the values from the text boxes
        data = [
            tb1.value,
            tb2.value,
            tb3.value,
            tb4.value,
            tb5.value
        ]
        
        # Print values to text field for display
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        
        # Write data to CSV
        with open('C:/Users/asd/Desktop/chiragpandyaflet.csv', mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)  # Write a row with the collected values

        page.update()  # Update the page

    # Create TextBox controls
    t = ft.Text()
    tb1 = ft.TextField(label="Standard")
    tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
    tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
    tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
    tb5 = ft.TextField(label="With an icon", icon=ft.Icons.EMOJI_EMOTIONS)

    # Create the button
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    # Add TextBoxes and button to the page
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)

    page.update()  # Final update to the page layout

import flet as ft
import pandas as pd

def page3(page: ft.Page):
    
    page.scroll = ft.ScrollMode.ALWAYS
    
    # Create a page with centered content
    back_button = ft.ElevatedButton("Back to Home", on_click=lambda e: go_to_page(page, "home"))
    
    # Function to handle filtering and updating table based on dropdown selections
    def button_clicked(e):
        # Get selected values from dropdowns
        selected_first_name = dd_first_name.value
        selected_last_name = dd_last_name.value
        selected_date = dd_date.value  # Ensure we get the selected value

        # Filter DataFrame based on the selected values from dropdowns
        filtered_df = df
        if selected_date:
            filtered_df = filtered_df[filtered_df["Date"] == selected_date]
        if selected_first_name:
            filtered_df = filtered_df[filtered_df["First_name"] == selected_first_name]
        if selected_last_name:
            filtered_df = filtered_df[filtered_df["Last_name"] == selected_last_name]

        # Clear the current rows in the data table
        data_table.rows.clear()

        # Add filtered rows to the data table
        for _, row in filtered_df.iterrows():
            total = row["rate"] * row["order"]
            mycheck = row["rate"] - 2

            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row['Date'])),
                        ft.DataCell(ft.Text(row['First_name'])),
                        ft.DataCell(ft.Text(row['Last_name'])),
                        ft.DataCell(ft.Text(str(row['order']))),
                        ft.DataCell(ft.Text(str(row['rate']))),
                        ft.DataCell(ft.Text(str(total))),
                        ft.DataCell(ft.Text(str(mycheck))),
                    ]
                )
            )
        # Calculate the totals
        total_order = filtered_df['order'].sum()
        total_rate = filtered_df['rate'].sum()
        total_amount = filtered_df['rate'].sum() * filtered_df['order'].sum()

        # Add a total row
        data_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Total")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text(str(total_order))),
                    ft.DataCell(ft.Text(str(total_rate))),
                    ft.DataCell(ft.Text(str(total_amount))),
                    ft.DataCell(ft.Text("")),
                ]
            )
        )

        # Update the page to reflect the changes
        page.update()

    # Function to reset filters and show all data
    def reset_button_clicked(e):
        # Clear filters (reset dropdowns to None or default)
        dd_first_name.value = None
        dd_last_name.value = None
        dd_date.value = None
        page.update()
        # Show all data in the table
        show_all_data()

    # Function to display all data in the table
    def show_all_data():
        # Clear the table first
        data_table.rows.clear()
        
        # Add all rows to the table
        for _, row in df.iterrows():
            total = row["rate"] * row["order"]
            mycheck = row["rate"] - 2

            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row['Date'])),
                        ft.DataCell(ft.Text(row['First_name'])),
                        ft.DataCell(ft.Text(row['Last_name'])),
                        ft.DataCell(ft.Text(str(row['order']))),
                        ft.DataCell(ft.Text(str(row['rate']))),
                        ft.DataCell(ft.Text(str(total))),
                        ft.DataCell(ft.Text(str(mycheck))),
                    ]
                )
            )
        
        # Calculate the totals
        total_order = df['order'].sum()
        total_rate = df['rate'].sum()
        total_amount = df['rate'].sum() * df['order'].sum()

        # Add a total row at the bottom
        data_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Total")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text(str(total_order))),
                    ft.DataCell(ft.Text(str(total_rate))),
                    ft.DataCell(ft.Text(str(total_amount))),
                    ft.DataCell(ft.Text("")),
                ]
            )
        )

        # Update the page
        page.update()

    # Text label for displaying selected value
    t = ft.Text()

    # Submit button
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    # Reset button
    reset_button = ft.ElevatedButton(text="Reset Filters", on_click=reset_button_clicked)

    # Dropdowns for filtering by First name and Last name
    dd_first_name = ft.Dropdown(
        width=200,
        options=[ft.dropdown.Option(name) for name in df["First_name"].unique()],
        label="Select First Name"
    )
    dd_last_name = ft.Dropdown(
        width=200,
        options=[ft.dropdown.Option(name) for name in df["Last_name"].unique()],
        label="Select Last Name"
    )
    dd_date = ft.Dropdown(
        width=200,
        options=[ft.dropdown.Option(name) for name in df["Date"].unique()],
        label="Select Date"
    )

    # Add dropdowns, buttons, and text to the page
    page.add(ft.Row(
        controls=[dd_first_name, dd_last_name, dd_date, b, reset_button,back_button], 
        alignment=ft.MainAxisAlignment.CENTER, 
        spacing=20  # Add space between controls
    ))

    # Arrange content in a row for the buttons and dropdowns
    # page.add(ft.Row(
    #     controls=[back_button], alignment=ft.MainAxisAlignment.END))

    page.add(
        ft.Row(
            controls=[ft.Text("All Data will be shown Here", size=24, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20  # Space between text and back button
        )
    )

    # Load the CSV file (assuming df is already available here)
    try:
        # df = pd.read_csv('C:/Users/asd/Desktop/flet.csv')  # Corrected file path
        if df.empty:
            raise ValueError("CSV file is empty.")
    except Exception as e:
        page.add(ft.Text(f"Error loading CSV: {e}", color="red"))
        return

    # Create the DataTable with initial data (can be empty or all data)
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Date")),
            ft.DataColumn(ft.Text("First name")),
            ft.DataColumn(ft.Text("Last name")),
            ft.DataColumn(ft.Text("order"), numeric=True),
            ft.DataColumn(ft.Text("rate"), numeric=True),
            ft.DataColumn(ft.Text("total"), numeric=True),
            ft.DataColumn(ft.Text("mycheck"), numeric=True),
        ],
        rows=[],  # Start with no rows
    )

    # Initially, populate the data table with all data
    show_all_data()

    # Scrollable table
    scrollable_table = ft.Column(
        controls=[data_table],
        scroll=ft.ScrollMode.ALWAYS  # Enable scrolling
    )
    
    # Add the scrollable table to the page
    page.add(scrollable_table)

    # Print the table rows in the console for debugging
    print(f"Rows in the table: {len(data_table.rows)}")

    
    # import pandas as pd
    # df = pd.read_csv('C:\Users\asd\Desktop\flet.csv')
    # for i in df['First_name']:
    #     for j in df['Last_name']:
    #         for k in df['Age']:
    #                 # page.add(
    #                 ft.DataTable(
    #         #         columns=[
    #         #             ft.DataColumn(ft.Text("First name")),
    #         #             ft.DataColumn(ft.Text("Last name")),
    #         #             ft.DataColumn(ft.Text("Age"), numeric=True),
    #         #         ],
    #         #         rows=[
    #         #             ft.DataRow(
    #         #                 cells=[
    #         #                     ft.DataCell(ft.Text("John")),
    #         #                     ft.DataCell(ft.Text("Smith")),
    #         #                     ft.DataCell(ft.Text("43")),
    #         #                 ],
    #         #             ),
    #         #         ],
    #         #     ),
    #         # )

                

    
 
    # page.add(
    #     ft.DataTable(
    #         columns=[
    #             ft.DataColumn(ft.Text("First name")),
    #             ft.DataColumn(ft.Text("Last name")),
    #             ft.DataColumn(ft.Text("Age"), numeric=True),
    #         ],
    #         rows=[
    #             ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(ft.Text("John")),
    #                     ft.DataCell(ft.Text("Smith")),
    #                     ft.DataCell(ft.Text("43")),
    #                 ],
    #             ),
    #         ],
    #     ),
    # )

    

# Function to handle page navigation
def go_to_page(page: ft.Page, page_name: str):
    page.clean()  # Clear the current page content
    if page_name == "home":
        home_page(page)
    elif page_name == "page1":
        page1(page)
    elif page_name == "page2":
        page2(page)
    elif page_name == "page3":
        page3(page)
    elif page_name == "order":
        order(page)
    elif page_name == "page6":
        page6(page)
    page.update()  # Refresh the page content

def main(page: ft.Page):
    go_to_page(page, "home")  # Start by showing the home page


ft.app(target=main)#,view = ft.WEB_BROWSER)
