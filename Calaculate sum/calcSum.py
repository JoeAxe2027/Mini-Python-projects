

f = open("test.txt")
lines = f.readlines()
f.close()


sum_column1 = 0
sum_column2 = 0


for lines in lines:
    numbers = lines.split()
    if len(numbers) == 2:
        sum_column1 += int(numbers[0])
        sum_column2 += int(numbers[1])


f2 = open("result.txt", "w")
f2.write("The total sum of column one =" + str(sum_column1) + "\n")
f2.write("The total sum of column two =" + str(sum_column2) + "\n")
f2.close()
