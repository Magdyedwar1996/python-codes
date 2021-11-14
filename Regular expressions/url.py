# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"
MY_WEB = "http://www.elzero.org"

search_my_web = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)
search_MY_WEB = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", MY_WEB)


def check_valid_URL(url):
    if url:
        print(f"{url} :is a valid url\n")
    else:
        print(f"{url}: is not a valid url\n")


check_valid_URL(my_web)
check_valid_URL(MY_WEB)


def Getting_groups_of_URL(url):
    print(f"Protocol: {url.group(1)}")
    print(f"Sub Domain: {url.group(2)}")
    print(f"Domain Name: {url.group(3)}")
    print(f"Top Level Domain: {url.group(4)}")
    print(f"Port: {url.group(5)}")
    print(f"Query String: {url.group(6)}")
    print("=" * 50)


Getting_groups_of_URL(search_my_web)
Getting_groups_of_URL(search_MY_WEB)
