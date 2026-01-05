arr = ["Annaya", "Sayan", "Madhumita", "Arkaduti", "Sandipan"]

# By For loop
for i in range(len(arr)):
    print(f"{i} => {arr[i]}\n")

#By Enumerate
for index, value in enumerate(arr):
    print(f"{index} => {value}\n")

"""
Output:
0 => Annaya
1 => Sayan
2 => Madhumita
3 => Arkaduti
4 => Sandipan
"""

for index, value in enumerate(arr, start=1):
    print(f"{index} => {value}\n")

"""
Output:
1 => Annaya
2 => Sayan
3 => Madhumita
4 => Arkaduti
5 => Sandipan
"""