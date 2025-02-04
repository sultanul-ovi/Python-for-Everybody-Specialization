name = "mbox-short.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst = list()
mail_names = list()
counts = dict()
qew= ""

for line in handle:
    lst = line.rstrip().split()
    if 'From' in lst:
        mail_names.append(lst[1])


for name in mail_names:
    counts[name] = counts.get(name, 0) + 1

max_name_as_list = [key for key, value in counts.items() if value == max(counts.values())]
max_name = qew.join(max_name_as_list)

print(max_name ,max(counts.values()))
