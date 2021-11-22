
def multi_bracket_validation(input):



    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    count=0

    for c in input:
        if c.isalpha() or c not in ["{","}","(",")","[","]"]:
            count=count+1


            continue
        elif c in "{[(":
            stack.append(c)


        elif stack and c == pairs[stack[len(stack)-1]]:

            stack.pop()

        else:
            return False

    if count==len(input):
            return False
    return len(stack) == 0






print(multi_bracket_validation("[}"))


