import os

target = "./chat_modes.yml"

src = "./modes.csv"

writer = open(target, "w", encoding="utf-8")


with open(src, "r", encoding="utf-8") as reader:
    _ = reader.readline();
    while True:
        line = reader.readline()
        if len(line) == 0:
            break
        line = line.strip()
        print(line)
        name, *prompt = line.split(",")
        name = name.strip("\"")
        name = name.strip("`")
        prompt = ",".join(prompt)
        prompt = prompt.strip("\"")
        prompt = prompt.strip("`")
        writer.write(f'{name}:\n')
        writer.write(f'  name: {name}\n')
        writer.write(f'  welcome_message: Hi, I am {name}\n')
        writer.write(f'  prompt_start: |\n')
        writer.write(f'    {prompt}\n')
        writer.write(f'  parse_mode: html\n\n')

writer.close()
