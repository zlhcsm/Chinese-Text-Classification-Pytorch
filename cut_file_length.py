filepath = 'THUCNews/data/train.txt'
output_filepath = 'THUCNews/data5000/train.txt'
amount = 4000
res = []
with open(filepath, 'r', encoding='utf8') as file:
    line = file.readline()
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    while line:
        if int(line.split("\t")[1]) == 0:
            if count0 <= amount:
                count0 = count0 + 1
                res.append(line)
        elif int(line.split("\t")[1]) == 1:
            if count1 <= amount:
                count1 = count1 + 1
                res.append(line)
        elif int(line.split("\t")[1]) == 2:
            if count2 <= amount:
                count2 = count2 + 1
                res.append(line)
        elif int(line.split("\t")[1]) == 3:
            if count3 <= amount:
                count3 = count3 + 1
                res.append(line)
        elif int(line.split("\t")[1]) == 4:
            if count4 <= amount:
                count4 = count4 + 1
                res.append(line)
        elif int(line.split("\t")[1]) == 5:
            if count5 <= amount:
                count5 = count5 + 1
                res.append(line)
        line = file.readline()
with open(output_filepath, 'wt', encoding='utf8') as f:
    for i in res:
        print(i, file=f, end='')
