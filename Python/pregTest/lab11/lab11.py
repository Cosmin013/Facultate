import re

def ex1():
    example = "Cuvi432nte 23123 cuvinte ceva altceva"

    words = re.findall(r"[a-zA-Z0-9]+", example)

    print(words)



if __name__ == "__main__":
    result = re.search(".*(\d+)", "File size if 12345 bytes")
    if result:
        print(result.group(1))

    result = re.search(".*?(\d+)", "File size if 12345 bytes")
    if result:
        print(result.group(1))

   # ex1()



