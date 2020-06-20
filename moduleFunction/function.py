def python_food():
    width = 80
    text = "spam and eggs"
    left_maargin = (width - len(text)) //2
    print(" " * left_maargin, text)


def center_text(text):
    text = str(text)
    left_maargin = (80 - len(text)) // 2
    print(" " * left_maargin, text)


center_text("spam and egg")
center_text("spam, spam egg")
center_text("spam spam spam")