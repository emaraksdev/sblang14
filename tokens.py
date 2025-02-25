class keywords:
    def __init__(self):
        self.tokens = {"print", "input", "random"}

    def __contains__(self, item):
        return item.lower() in self.tokens
    
class operators:
    def __init__(self):
        self.tokens = {"add", "sub", "mul", "div", "mod"}
        #               +      -           *           /         %

    def __contains__(self, item):
        return item.lower() in self.tokens