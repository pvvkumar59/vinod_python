# # This is to read line in text file
with open("C:\Users\Admin\Documents\\readline.txt", 'r') as f:
    lines = f.readlines()
    fp = open("C:\Users\Admin\Documents\\writer.txt", 'w+')
    # fp.write()
    print(fp.read())
    print(lines[1])
    print(lines)
    print (len(lines))
    for l in lines:
        if l == lines[3]:
        # print (l.strip())
        # print("+++++++")
            print(l)
    line = (l for l in lines if l == lines[3])
    print(line)

fp = open("C:\Users\Admin\Documents\\writer.txt", 'w+')
fp.write("heyyyy this is vinod")
data = fp.read()
print(data)
fp.close()

