def match_words(words):
    ctr = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("Matching words:", lst)
    return ctr 


words = ["level", "hello", "radar", "world", "wow", "python"]

count = match_words(words)
print("No. of matching words:", count)
    