textList = ["One", "Two", "Three", "Four", "Five"]


# writeFile = open("original.txt", "w")
# for line in textList:
#     writeFile.write(line)
#     writeFile.write("\n")
#     writeFile.close()
    
writeFile = open("original.txt", "w").writelines(textList)
    # writeFile.write("\n")
  