# Reading input from a file in the data_dir directory in this project
# Create a directory in the same project with the name "data_dir" and place the "input.txt" file in that directory
data_dir_name = 'data_dir'
filename = "input.txt"
path = f'{data_dir_name}/{filename}'
infile = open(path, 'r')

ans = []

for i in infile:
    lst = i.split('^^')

    for j in lst:
        a = j.split('=', 1)

        if a[0] not in ["id", "name", "city"]:
            print("Key missing!")
            raise Exception("Key is Missing")
            # break

        a = a[-1]
        if '\n' in a:
            a = a.replace('\n', '')
        if '^' in a:
            a = a.replace('^', '')
        if '=' in a:
            a = a.replace('=', '')
        ans.append(a)

print('id|name|city')

for i in range(0, len(ans), 3):
    print(ans[i], '|', ans[i + 1], '|', ans[i + 2])

"""
id=10^^name=bel, james^^city=paris
id=11^^name=smith, ^peter^^city=Chicago
id=12^^name=mcdonalds, julie^^city=NY=C
"""
