# write your code here
# write your code here
formatted_text = ""

def plain():
    return input("Text: \n")

def bold():
    return f"**{input('Text: ')}**"

def italic():
    return f"*{input('Text: ')}*"

def inline_code():
    return f"`{input('Text: ')}`"

def new_line():
    return "\n"

def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"

def unordered_list():
    while True:
        rows = int(input('Number of rows:'))
        if rows <= 0:
            print('The number of rows should be greater than zero')
        else:
            result = ""
            for i in range(rows):
                text = input(f"Row #{i + 1}: ")
                result += f"* {text}\n"
            return result

def ordered_list():
    while True:
        rows = int(input('Number of rows:'))
        if rows <= 0:
            print('The number of rows should be greater than zero')
        else:
            result = ""
            for i in range(rows):
                text = input(f"Row #{i + 1}: ")
                result += f"\n{i + 1}. {text}"
            return result

def header():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                text = input("Text: ")
                # только перенос строки после заголовка
                return f"{'#' * level} {text}\n"
            else:
                print("The level should be within the range of 1 to 6")
        except ValueError:
            print("The level should be within the range of 1 to 6")

formatters = {
    "plain": plain,
    "bold": bold,
    "italic": italic,
    "inline-code": inline_code,
    "link": link,
    "header": header,
    "new-line": new_line,
    "unordered-list": unordered_list,
    "ordered-list": ordered_list
}

while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!help":
        print("Available formatters: plain bold italic header link inline-code new-line")
        print("Special commands: !help !done")

    elif user_input == "!done":
        file = open('output.md', 'w')
        file.write(formatted_text)
        file.close()
        break

    elif user_input in formatters:
        formatted_text += formatters[user_input]()
        print(formatted_text)

    else:
        print("Unknown formatting type or command")