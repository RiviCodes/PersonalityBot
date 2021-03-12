# Personality Bot v. 0.1

print('Beep boop! I\'m a bot that measures the patience and kindness of a person!')
print('I need 2 values, from 1 to 10 (1 = LOW, 10 = HIGH) in order to work.')
patience = int(input('Please, input the value for PATIENCE: '))
kindness = int(input('Now, input the value for KINDNESS: '))
print('')
print('BEEP. Working on it...')
print('')

if patience == 1 and kindness == 1:
    print('This person is neither patient OR kind')
elif patience == 10 and kindness == 10:
    print('BEEP! This person is both patient AND kind :)')
elif patience > 1 or patience < 10 and kindness > 1 or patience < 10:
    print('Meh, I\'m bored...')
else:
    print('BRRRRH - Invalid command!')

if patience == kindness:
    print(f'Boop beep. This person SHARES the same values for patience ({patience}) and kindness ({kindness})')
else:
    print('~')

if patience < kindness:
    print(f'Also, patience\'s value ({patience}) is LOWER than kindness\'es value ({kindness})')
elif patience > kindness:
    print(f'Also, patience\'s value ({patience}) is HIGHER than kindness\'es value ({kindness})')
else:
    print('~')