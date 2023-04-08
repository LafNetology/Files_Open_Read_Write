# from pprint import pprint

final_list = []
files = ['1.txt', '2.txt', '3.txt']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        strings = f.readlines()
        final_list.append([len(strings), file, strings])

final_list_sorted = sorted(final_list)
# pprint(final_list_sorted, width=100)

for elem in final_list_sorted:
    with open('4.txt', 'a', encoding='utf-8') as f:
        f.write(elem[1] + '\n')
        f.write(str(elem[0]) + '\n')
        for line in elem[2]:
            f.write(line)
        f.write('\n')
        f.write('\n')
