import pyinputplus as pyip


prices = {'wheat': 1, 'white': 1, 'sourdough': 2, 'chicken': 2, ' turkey': 2, 'ham': 1, 'tofu': 1,
          'cheddar': 1, 'swiss': 1, 'mozzarella': 1, 'mayo': 1, 'mustard': 1, 'lettuce': 1, 'tomato': 1}

while True:
    ingredients = []
    ingredients.append(pyip.inputMenu(['wheat', 'white', 'sourdough'],
                           prompt='Please select the type of bread for your sandwich: \n',
                           numbered=True))

    ingredients.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                           prompt='Please select the type of protein for your sandwich: \n',
                           numbered=True))

    if pyip.inputYesNo('Would you like cheese in your sandwich?(Y/N)\n')=='yes':
        ingredients.append(pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True))

    if pyip.inputYesNo('Would you like mayo?(Y/N)\n')=='yes':
        ingredients.append('mayo')
    if pyip.inputYesNo('Would you like mustard?(Y/N)\n')=='yes':
        ingredients.append('mustard')
    if pyip.inputYesNo('Would you like lettuce?(Y/N)\n')=='yes':
        ingredients.append('lettuce')
    if pyip.inputYesNo('Would you like tomato?(Y/N)\n')=='yes':
        ingredients.append('tomato')

    sandwichQt = pyip.inputInt('How many sandwiches would you like to order?\n',
                               blockRegexes=['[0|-|.]'])

    total_amount = 0

    print(f'Your ingredients selection together with the prices are as follows: \n')
    for item in ingredients:
        price = prices[item]
        print(f'{item}= {price}')
        total_amount += price

    print(f'sandwich cost x sandwich Qt ordered = {total_amount}x{sandwichQt}= '
          f'{total_amount*sandwichQt}')

    if pyip.inputYesNo('Please confirm your order: (Y/N)\n')=='yes':
        print('Please take your order number from the machine ')
        break
