def split_before_each_uppercases(formula):
    apperapper = []
    new_formula = []
    for i in range(len(formula)):
      if formula[i].isupper() == True:
        apperapper.append(i)
    print(apperapper)
    if apperapper:
      for i in range(len(apperapper) -1):
        print(i)
        new_word = formula[apperapper[i]:apperapper[i+1]]
        new_formula.append(new_word)
      last_word = formula[apperapper[len(apperapper) - 1]:]
      new_formula.append(last_word)
      print(new_formula)
    elif formula:
      new_formula.append(formula)
    return new_formula
    

def split_at_first_digit(formula):
    num = []
    for i in range(len(formula)):
      if formula[i].isdigit() == True:
        num = formula[i:]
        letter = formula [0:i]
        num = int(num)
        return (letter, num)

    return (formula ,1)
