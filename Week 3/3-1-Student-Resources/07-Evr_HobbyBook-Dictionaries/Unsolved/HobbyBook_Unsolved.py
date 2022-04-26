# @TODO: Your code here

my_info{'name': 'Lupita',
         'age': 5,
         'hobbies': ['sleeping', 'running', 'eating'],
         'wake-up': {'Mon': 8,
                     'Tue': 8,
                     'Wed': 8}}
            
print(f"My pet's name is {my_info['name']},")

hobbies = my_info['hobbies']
for each_hobby in hobbies:
    print(f'She likes {each_hobby},')

wake_up=my_info['wake-up']
for each_key in wake_up:
    print(f'I wake up on {each_key} at {wake_up[each_key]}.')