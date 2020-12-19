n = int(input())
files_dict = {}
for _ in range(n):
    fname, ext = input().split('.')
    if ext not in files_dict:
        files_dict[ext] = 1
    else:
        files_dict[ext] += 1
files_dict = {k:v for k, v in sorted(files_dict.items(), key=lambda item: item[0])}
for k, v in files_dict.items():
    print(k, v)
