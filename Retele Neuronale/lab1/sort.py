f=  open("Lorem.txt","r")


content = f.read().split()
content = [word.strip('.').strip(',') for word in content ]
content = set(content)
content = sorted(content)


print(content)

