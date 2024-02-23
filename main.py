# open files to read
with open(input('Input configuration file name : '), 'r') as conf_file:
    conf_list = conf_file.readlines()
with open(input('Input text file name   : '), 'r') as text_file:
    text_list = text_file.readlines()

# remove charecter \n from text file strings
for i in range(len(text_list)):
    text_list[i] = text_list[i].replace('\n', '')

new_list = text_list.copy() # crate new list for change

# replace  value1 by value2
for i in range(len(new_list)):
    for s in conf_list:
        new_list[i] = new_list[i].replace(s[0], s[2])

# count the number of changes in a line
for i in range(len(new_list)):
    ch_count = 0
    for c in range(len(new_list[i])):
        if new_list[i][c] != text_list[i][c]:
            ch_count += 1
    new_list[i] = [ch_count, new_list[i]]

# sort lines
new_list.sort(reverse=True)

# Output result
print('Modified and sorted text :')
for i in new_list:
    print(i[1])
