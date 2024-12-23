import flet as ft
import math

def home_page(page: ft.Page):
    page.add(ft.Container(gradient=ft.LinearGradient( begin=ft.alignment.top_left, end=ft.alignment.bottom_right, colors=["#ff7e5f", "#feb47b"], ), expand=True, # This ensures the gradient fills the entire page 
                           ))
    # Create buttons to navigate to other pages
    button1 = ft.ElevatedButton("Exam List", on_click=lambda e: go_to_page(page, "page1"))
    button2 = ft.ElevatedButton("page2", on_click=lambda e: go_to_page(page, "page2"))
    button3 = ft.ElevatedButton("Page3", on_click=lambda e: go_to_page(page, "page3"))
    order = ft.ElevatedButton("Orders", on_click=lambda e: go_to_page(page, "order"))
   
    # Arrange buttons in a column with center alignment and some space between them
    page.add(
        ft.Row(  # Use Column to arrange buttons vertically
            controls=[button1, button2, button3],
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
import pandas as pd

def page3(page: ft.Page):
    import datetime
    page.scroll=ft.ScrollMode.ALWAYS
    # scroll=ft.ScrollMode.ALWAYS
    
    # Create a page with centered content
    back_button = ft.ElevatedButton("Back to Home", on_click=lambda e: go_to_page(page, "home"))

    # Arrange content in a column, center the text and button, with some spacing
    page.add(ft.Row(controls=[back_button], alignment=ft.MainAxisAlignment.END))

    page.add(
        ft.Row(
            controls=[
                ft.Text("Welcome to Page 3", size=24, weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20  # Space between text and back button
        )
    )
    #here i am adding date
    def handle_change(e):
    # Get the selected date
        selected_date = e.control.value
    # Print or display the selected date
        page.add(ft.Text(f"Date changed: {selected_date.strftime('%Y-%m-%d')}"))


    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))

    page.add(
        ft.ElevatedButton(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(day=1,month=10,year=2023),
                    last_date=datetime.datetime(day=1,month=12,year=2023),
                    on_change=handle_change,
                    on_dismiss=handle_dismissal,
                )
            ),
        )
    )
    
    # Load the CSV file
    try:
        df = pd.read_csv('C:/Users/asd/Desktop/flet.csv')  # Corrected file path
        if df.empty:
            raise ValueError("CSV file is empty.")
    except Exception as e:
        page.add(ft.Text(f"Error loading CSV: {e}", color="red"))
        return

    # Create the DataTable
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("First name")),
            ft.DataColumn(ft.Text("Last name")),
            ft.DataColumn(ft.Text("order"), numeric=True),
            ft.DataColumn(ft.Text("rate"), numeric=True),
            ft.DataColumn(ft.Text("total"), numeric=True),
            ft.DataColumn(ft.Text("mycheck"), numeric=True),

            
        ],
        rows=[],  # Start with no rows
    )

    # Loop through the DataFrame rows and add them to the DataTable
    for _, row in df.iterrows():
        total = row["rate"]*row["order"]
        mycheck = row["rate"]-2


        data_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row['First_name'])),
                    ft.DataCell(ft.Text(row['Last_name'])),
                    ft.DataCell(ft.Text(str(row['order']))),
                    ft.DataCell(ft.Text(str(row['rate']))),
                    ft.DataCell(ft.Text(str(total))),
                    ft.DataCell(ft.Text(str(mycheck))),
                    

                ]
            )
        )
    scrollable_table = ft.Column(
        controls=[data_table],
        scroll=ft.ScrollMode.ALWAYS  # Enable scrolling
    )
    # Add the DataTable to the page
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
    page.update()  # Refresh the page content

def main(page: ft.Page):
    go_to_page(page, "home")  # Start by showing the home page


ft.app(target=main)#,view = ft.WEB_BROWSER)
