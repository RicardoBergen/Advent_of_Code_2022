with open('D:/Github/Advent_of_Code_2022/Day_1/example.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]
elf_sums = []
current_sum = 0
for entry in calories:
    if entry != '':
        current_sum += int(entry)
    elif entry == '':
        elf_sums.append(current_sum)
        current_sum = 0
elf_sums.append(current_sum)
    
print(max(elf_sums))
