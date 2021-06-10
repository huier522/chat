
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        chat = []
        for line in file:
            chat.append(line.strip())
        return chat


def convert(dialogue):
    for line in dialogue:
        words = line.split(' ')
        time = words[0][:5]
        name = words[0][5:]
        say = words[1:]
        print(name)

def main():
    filename = '3.txt'
    dialogue = read_file(filename)
    dialogue = convert(dialogue)


main()
