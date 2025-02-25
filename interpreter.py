import tokens

variables = {}
keywords = tokens.keywords()
operators = tokens.operators()

def tokenize(code):
    for word in code.split():
        if word.isdigit():
            yield("NUMBER")
            yield(word)
        
        elif word in keywords:
            yield("KEYWORD")
            yield(word)

        elif word in operators:
            yield("OPERATOR")
            yield(word)

        elif word[0] == "#":
            yield("VAR")
            yield(word)

        else:
            yield("ELSE")
            yield(word)


def parse(tokens):
    if tokens[0] == "KEYWORD" and tokens[1] == "print":
        print(tokens[3])

    if tokens[0] == "NUMBER" and tokens[2] == "OPERATOR" and tokens[4] == "NUMBER":
        if tokens[3] == "add":
            print(int(tokens[1])+int(tokens[5]))

        elif tokens[3] == "sub":
            pass

        elif tokens[3] == "mul":
            pass

        elif tokens[3] == "div":
            pass

        elif tokens[3] == "mod":
            pass

        elif tokens[0] == "VAR" and tokens[2] == "ELSE":
            if tokens[1] in variables:
                variables.update({tokens[1]: tokens[3]})

        elif tokens[1] == "print" and tokens[2] == "VAR":
            if tokens[3] in variables:
                detected_variable = tokens[3]
                print(variables[detected_variable])

def raise_error(word_number,message):
    raise ValueError(f"{message} on word number {word_number}")