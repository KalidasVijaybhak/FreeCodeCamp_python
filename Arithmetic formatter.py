def arithmetic_arranger(problems,answer = False):
    first_operand = []
    second_operand = []
    operator = []
#     Splliting the entire problems into operands and operators ex: if "34 + 23" : it is split into 34 , + , 23 as first_operand ,operator, second_operand
    for problem in problems:
        elements = problem.split()
        first_operand.append(elements[0])
        operator.append(elements[1])
        second_operand.append(elements[2])

     # Check for * or /
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Check the digits
    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check the length
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
    # check if no. of problems is greater than 5
    if len(problems) > 5:
        return "Error: Too many problems."
    
#       32         1      9999      523     First line
#     +  8    - 3801    + 9999    -  49     Second line
#     ----    ------    ------    -----     Third line
#       40     -3800     19998      474     Fourth line
    
    
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for i in range(len(first_operand)):
        if(len(first_operand[i])>len(second_operand[i])):
            first_line.append(" "*2 + first_operand[i])
        else:
            first_line.append(" "*(len(second_operand[i])-len(first_operand[i])+2)+first_operand[i])

    for i in range(len(second_operand)):
        if(len(first_operand[i])< len(second_operand[i])):
            second_line.append(operator[i]+" "+second_operand[i])
        else:
            second_line.append(operator[i]+" "*(len(first_operand[i])-len(second_operand[i])+1)+second_operand[i])

    for i in range(len(first_operand)):
        third_line.append("-"*(max(len(first_operand[i]),len(second_operand[i]))+2))

    if answer:
        for i in range(len(first_operand)):
            if operator[i] == "+":
                result = str(int(first_operand[i])+int(second_operand[i]))
            elif operator[i] == "-":
                result = str(int(first_operand[i])-int(second_operand[i]))
            if (max(len(first_operand[i]),len(second_operand[i]))<len(result)):
                fourth_line.append(" "+result)
            else:
                fourth_line.append(" "*(max(len(first_operand[i]),len(second_operand[i]))-len(result)+2)+result)    
        arranged_problems = "    ".join(first_line)+"\n"+"    ".join(second_line)+"\n"+"    ".join(third_line)+"\n"+"    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line)+"\n"+"    ".join(second_line)+"\n"+"    ".join(third_line)
    return(arranged_problems)
