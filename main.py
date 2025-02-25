from interpreter import parse, tokenize, raise_error

tokens = []

while True:
    code = input("Enter code to interpret: ")

    print("\n*tokens begin*\n")

    for token in tokenize(code):
        print(token)

        tokens.append(token)

    print("\n*tokens end*\n")

    parseconfirm = input("Would you like to parse? ")
    if parseconfirm == "yes":
        parse(tokens)