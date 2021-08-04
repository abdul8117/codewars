def quadratic_builder(expression):
    import string

    alphabet = list(string.ascii_lowercase)

    for i in expression:
        if i in alphabet:
            variable = i

    left = expression.split(")(")[0].replace("(", "")
    right = expression.split(")(")[1].replace(")", "")

    print("Input:", left, right)

    left_terms = get_terms(left, variable)
    right_terms = get_terms(right, variable)

    
    ax = left_terms[0] * right_terms[0]
    bx = left_terms[0] * right_terms[1] + left_terms[1] * right_terms[0]
    c = left_terms[1] * right_terms[1]

    quadratic = ""

    if ax == 1:
        quadratic += f"{variable}^2"
    elif ax == -1:
        quadratic += f"-{variable}^2"
    elif ax == 0:
        pass
    elif ax < -1:
        quadratic += f"{str(ax)}{variable}^2"
    else:
        quadratic += f"{ax}{variable}^2"
    
    
    if bx == 1:
        quadratic += f"+{variable}"
    elif bx == -1:
        quadratic += f"-{variable}"
    elif bx == 0:
        pass
    elif bx < -1:
        quadratic += f"{str(bx)}{variable}"
    else:
        quadratic += f"+{bx}{variable}"
    
    if c < 0:
        quadratic += str(c)
    elif c == 0:
        pass
    else:
        quadratic += f"+{c}"


    return quadratic

        
        
def get_terms(exp, var):
    terms = []

    if exp[0] == "-":

        exp = list(exp)
        del exp[0]
        exp = ''.join(exp)

        if "+" in exp:

            # constant is > 0

            exp = exp.split("+")

            if exp[0] == var:
                terms.append(-1)
                terms.append(int(exp[1]))

                return terms
            

            # coefficient is < -1
            
            # remove x
            exp[0] = exp[0].replace(var, "")

            terms.append(int(exp[0]))
            terms.append(int(exp[1]))

            return terms


        elif "-" in exp:
            
            # constant is < 0

            exp = exp.split("-")

            if exp[0] == var:
                terms.append(-1)
                terms.append(int(exp[1]) * -1)

                return terms

            # coefficient is < -1

            # remove x
            exp[0] = exp[0].replace(var, "")

            terms.append(int(exp[0]) * -1)
            terms.append(int(exp[1]) * -1)

            return terms

        
    
    else:
        # leading coefficient is a positive number

        if "+" in exp:
            exp = exp.split("+")

            if exp[0] == var:
                terms.append(1)
                terms.append(int(exp[1]))

                return terms

            # coefficient is > 1

            exp[0] = exp[0].replace(var, "")
            
            terms.append(int(exp[0]))
            terms.append(int(exp[1]))

            return terms



        elif "-" in exp:
            exp = exp.split("-")
                       

            if exp[0] == var:
                terms.append(1)
                terms.append(int(exp[1]) * -1)

                return terms

            # coefficient is > 1

            exp[0] = exp[0].replace(var, "")

            terms.append(int(exp[0]))
            terms.append(int(exp[1]) * -1)

            return terms
        




print("Output:", quadratic_builder("(x+4)(x-4)"))
