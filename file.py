with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(len(content))
    words = len(content.split())
    print(words)

    with open('referat.txt', 'r', encoding='utf-8') as f:
        for ln in f:
            ln = ln.replace('.', '!')
            print(ln)