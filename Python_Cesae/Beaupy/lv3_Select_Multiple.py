from beaupy import select_multiple

options = ["Apple", "Philips", "Lg", "HP"]
selected_options = select_multiple(options, tick_character="xD", ticked_indices=[0], cursor_style="blue")
print("You Selected: ")
for option in selected_options:
    print(option)