rv_class = ["Class A", "Class B/Van", "Class C", "Travel Trailer", "5th Wheel"]

rv_type = input(
    """
    Please select your RV Type:
    A) Class A
    B) Class B/Van
    C) Class C
    D) Travel Trailer
    E) 5th Wheel
    [A/B/C/D/E]?:
    """
).upper()


def show_rv_type(choice):
    print("Equipment Type: " + choice)


if rv_type in ("A"):
    newStr = rv_class[0]
    show_rv_type(newStr)
elif rv_type in ("B"):
    newStr = rv_class[1]
    show_rv_type(newStr)
elif rv_type in ("C"):
    newStr = rv_class[2]
    show_rv_type(newStr)
elif rv_type in ("D"):
    newStr = rv_class[3]
    show_rv_type(newStr)
elif rv_type in ("E"):
    newStr = rv_class[4]
    show_rv_type(newStr)
else:
    print("Invalid Input!")
