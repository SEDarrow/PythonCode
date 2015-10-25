
#imput a polynomial in standard form and return the 1st derivative 
def polynomial():
    polynomial = input("Enter a polynomial of x: ")
    terms = []
    last = 0
    for each in range(0, len(polynomial)):
        if(polynomial[each] == '+' or polynomial[each] == '-'):
            terms.append(polynomial[last:each].strip(' '))
            terms.append(polynomial[each])
            last = each+1
    terms.append(polynomial[last:])
    output = ''
    for each in terms:
        if(each[0] == ' '):
            each = each[1:]
        if each == '+' or each == '-':
            output+= each
            continue
        if not 'x' in each:
            output = output[:-1]
            continue
        if not '^' in each:
            if(each.strip('x') ==""):
                output+= '1'
                continue
            output+=each.strip('x')
            continue
        if each[0] == 'x':
            output+= each[each.index('^')+1:]
        else:
            output+= str(int(each[0:each.index('^')-1])*int(each[each.index('^')+1:]))
        
        if(int(each[each.index('^')+1:])-1 == 1):
            output += 'x'
            continue
        output+= 'x^'+str(int(each[each.index('^')+1:])-1)
    print(output)

