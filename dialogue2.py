
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        for line in file:
            chat.append(line.strip())
        return chat


def convert(dialogue):
    person = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in dialogue:
        words = line.split(' ')
        time = words[0]
        name = words[1]
        say = words[2:]
        if name == 'Allen':
            if words[2] == '貼圖':
                allen_sticker_count += 1
            elif words[2] == '圖片':
                allen_image_count += 1
            else:
                for msg in say:
                    allen_word_count += len(msg)
        elif name == 'Viki':
            if words[2] == '貼圖':
                viki_sticker_count += 1
            elif words[2] == '圖片':
                viki_image_count += 1 
            else:
                for msg in say:
                    viki_word_count += len(msg)
    print(f'Allen 說了{allen_word_count}個字')
    print(f'Allen 傳了{allen_sticker_count}個貼圖和{allen_image_count}張圖片')
    print(f'Viki 說了{viki_word_count}個字')
    print(f'Viki 傳了{viki_sticker_count}個貼圖和{viki_image_count}張圖片')


def main():
    filename = 'LINE-Viki.txt'
    dialogue = read_file(filename)
    dialogue = convert(dialogue)


main()
