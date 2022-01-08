words = (
    "Animal",
    "Badger",
    "Lion",
)

alpha = "America"

print(type(words), tuple(alpha))


def main():
    for word in words:
        print(word.upper())
    for word in words:
        print(word.lower())
    for word in words:
        print(word.endswith("er"))


# first_name = "Lica"
# last_name = "Andro"
# first_whitespace = "      leaks"
# last_whitespace = "lasd             "
# both_whitespace = "         asldkjasd             "

# full_name: str = first_name + " " + last_name

# print(
#     full_name.lower(),
#     last_name[:3],
#     #  first_name[1],
# )

# print(type(last_name))
# print(last_whitespace)
# print(first_whitespace.lstrip())
# print(both_whitespace.strip())

if __name__ == "__main__":
    main()
