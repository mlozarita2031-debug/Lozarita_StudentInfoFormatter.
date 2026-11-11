
# Student Information Formatter

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

full_name = first_name + " " + last_name

formatted_name = full_name.title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()

character_count = len(full_name)

print("\nFormatted Output:")
print("Name:", formatted_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Favorite Subject:", formatted_subject)
print("Character Count:", character_count)
