
def format_name(f_name, l_name):
    """Take a first name and last name and format it
    to return the title case version of the name."""
    return f"{f_name.title()} {l_name.title()}"

def format_name2(f_name, l_name):
    return f_name.title(), l_name.title()


print(format_name("mArCIN", "JC"))
