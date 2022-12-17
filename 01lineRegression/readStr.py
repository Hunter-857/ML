


if __name__ == '__main__' :
    new_lines = []
    with open("/Users/hunter/Desktop/JAVApro/electron-app/in.vtt",) as file:
        lines = file.readlines()
        index = 0
        new_lines = []
        for i in range(0, len(lines)):
            # index = int(i / 4)
            # if i == 4 * index + 2:
            #     new_lines.append(lines[i])
            if not lines[i].startswith("00"):
                new_lines.append(lines[i])
        print(new_lines)
    with open("/Users/hunter/Desktop/revise_out.txt", 'a') as file:
        file.writelines(new_lines)


