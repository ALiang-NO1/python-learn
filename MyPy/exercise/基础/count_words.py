def count_words(filename):
    try:
        with open(filename) as file:
            content = file.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + "does not exit!"
        print(msg)
    else:
        # 计算文本中大约包含多少个单词
        words = content.split()
        num_words = len(words)
        print("The file "+filename+" has about "+str(num_words)+" words!")