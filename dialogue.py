
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        for line in file:
            chat.append(line.strip())
        return chat

def convert(dialogue):
    new_chat = []
    person = None #先給空值，避免一開始不是人名（空值）時程式出錯
    for line in dialogue:
        if line == 'Allen':
            person = 'Allen'
            continue #跳過廻圈，避免當只有人名卻沒有對話時裝入清單
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #若person是空值
            new_chat.append(person + ': ' + line)
    return new_chat

def write_file(filename, dialogue):
    with open(filename, 'w') as file:
        for line in dialogue:
            file.write(line + '\n')

def main():
    filename = 'input.txt'
    dialogue = read_file(filename)
    dialogue = convert(dialogue)
    write_file('output.txt', dialogue)

main()
