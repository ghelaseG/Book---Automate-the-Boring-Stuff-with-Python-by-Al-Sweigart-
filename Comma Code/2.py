def list_to_string(a_list):
    return '{0} and {1}'.format(', '.join(a_list[:-1]), a_list[-1])

some_list = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(some_list))
