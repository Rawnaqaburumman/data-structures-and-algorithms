
def multi_bracket_validation(input):

    input=str(input)


    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []

    for c in input:
        if c.isalpha() or c not in ["{","}","(",")","[","]"]:

            continue
        elif c in "{[(":
            stack.append(c)


        elif stack and c == pairs[stack[len(stack)-1]]:

            stack.pop()

        else:
            return False
     

    return len(stack) == 0






print(multi_bracket_validation("{jnbn}"))

a=[5,4,3]
print(len(a)-1)
