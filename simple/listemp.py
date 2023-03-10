file_name = 'emp.csv'
def content(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()

    lines_string = ''.join(lines)
    lines_string = lines_string.replace("email.com", "email.com<br>")
    lines_string = lines_string.replace(",Manager", ",Manager<br>")

    return lines_string
#print(content(file_name))
