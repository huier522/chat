
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        for line in file:
            chat.append(line.strip())
        return chat

def main():
    filename = 'input.txt'
    dialogue = read_file(filename)
    print(dialogue)

main()
