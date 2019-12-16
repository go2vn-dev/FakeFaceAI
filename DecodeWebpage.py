from bs4 import  BeautifulSoup


def list_to_set(name):
    # convert list to set
    return set(name)

#delcare list
name = ["A", "B", "C", "D", "A", "C"]

print(name)
print(list_to_set(name))