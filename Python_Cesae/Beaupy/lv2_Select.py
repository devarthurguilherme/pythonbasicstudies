from beaupy import select

options = ["Python", "JavaScrip", "Power BI", "Excel", "R language"]
selected_option= select(options, cursor="-->", cursor_style="blue")
print(f"You like {selected_option}")