import timeit
from random import shuffle

def secondsToFormattedTime(seconds):
    # https://codereview.stackexchange.com/questions/174796/convert-seconds-to-hours-minutes-seconds-and-pretty-print/174798
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    periods = [('hours', hours), ('minutes', minutes), ('seconds', seconds)]
    time_string = ', '.join('{} {}'.format(round(value, 2), name)
                        for name, value in periods
                        if value)
    return time_string

print('--- MUSIC FUNDAMENTALS ---\n')
# ask user if they would like to randomize the keys, and save response as boolean
user_key_randomize_preference = ''
randomize_keys = False
while user_key_randomize_preference.lower() != 'y' and user_key_randomize_preference.lower() != 'n':
    user_key_randomize_preference = input('Randomize keys? (Y/N) ')
    if user_key_randomize_preference.lower() == 'y':
        randomize_keys = True

# ask user if they would like to randomize the exercises within each key, and save response as boolean
user_exercise_randomize_preference = ''
randomize_exercises = False
while user_exercise_randomize_preference.lower() != 'y' and user_exercise_randomize_preference.lower() != 'n':
    user_exercise_randomize_preference = input('Randomize exercises? (Y/N) ')
    if user_exercise_randomize_preference.lower() == 'y':
        randomize_exercises = True

# open keys file and populate list
keys_file = open('data/keys.txt', 'r')
keys_list = list()
for line in keys_file.read().splitlines():
    keys_list.append(line)

keys_file.close()

# open exercises file and populate list
exercises_file = open('data/exercises.txt', 'r')
exercises_list = list()

for line in exercises_file.read().splitlines():
    exercises_list.append(line)

exercises_file.close()

if randomize_keys:
    shuffle(keys_list)

keys_list_with_times = list(keys_list)
start_time = timeit.default_timer()

for key in keys_list:
    current_index = keys_list.index(key)
    key_start_time = timeit.default_timer()
    if randomize_exercises:
        shuffle(exercises_list)
    # prints the key, and the number it is out of the total number of keys
    print('--> {0} ({1}/{2})'.format(key, current_index + 1, len(keys_list)))
    for exercise in exercises_list:
        print((' ' * 4) + exercise)

    theInput = input('\nPress Enter to continue... (q + enter to quit)\n')
    key_end_time = timeit.default_timer()
    key_total_time = key_end_time - key_start_time
    keys_list_with_times[current_index] = [key, round(key_total_time, 2)]
    if theInput.lower() == 'q':
        print('Exiting...')
        break

end_time = timeit.default_timer()
total_time = round(end_time - start_time, 2)

print('Results:')
for result in keys_list_with_times:
    key = result[0]
    time = result[1]
    print('{0: <6s}: {1}'.format(key, secondsToFormattedTime(time)))

print('Total time: {0}'.format(secondsToFormattedTime(total_time)))
print('Complete! Nice work :)')