with open("binary",'bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

