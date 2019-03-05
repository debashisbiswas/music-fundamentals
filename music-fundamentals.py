import timeit
from random import shuffle

print('--- MUSIC FUNDAMENTALS ---\n')
user_scale_preference = ''
randomize_scales = False
while user_scale_preference.lower() != 'y' and user_scale_preference.lower() != 'n':
    user_scale_preference = input('Randomize scales? (Y/N) ')
    if user_scale_preference.lower() == 'y':
        randomize_scales = True

user_exercise_preference = ''
randomize_exercises = False
while user_exercise_preference.lower() != 'y' and user_exercise_preference.lower() != 'n':
    user_exercise_preference = input('Randomize exercises? (Y/N) ')
    if user_exercise_preference.lower() == 'y':
        randomize_exercises = True

# open scales file and populate list
scales_file = open('data/scales.txt', 'r')
scales_list = list()
for line in scales_file.read().splitlines():
    scales_list.append(line)

scales_file.close()

# open exercises file and populate list
exercises_file = open('data/exercises.txt', 'r')
exercises_list = list()

for line in exercises_file.read().splitlines():
    exercises_list.append(line)

exercises_file.close()

if randomize_scales:
    shuffle(scales_list)

scales_list_with_times = list(scales_list)
start_time = timeit.default_timer()

for scale in scales_list:
    current_index = scales_list.index(scale)
    scale_start_time = timeit.default_timer()
    if randomize_exercises:
        shuffle(exercises_list)
    # prints the scale, and the number it is out of the total number of scales
    print('--> {0} ({1}/{2})'.format(scale, current_index + 1, len(scales_list)))
    for exercise in exercises_list:
        print((' ' * 4) + exercise)

    theInput = input('\nPress Enter to continue... (q + enter to quit)\n')
    scale_end_time = timeit.default_timer()
    scale_total_time = scale_end_time - scale_start_time
    scales_list_with_times[current_index] = [scale, round(scale_total_time, 2)]
    if theInput.lower() == 'q':
        print('Exiting...')
        break

end_time = timeit.default_timer()
total_time = round(end_time - start_time, 2)

print('Results:')
for result in scales_list_with_times:
    scale = result[0]
    time = result[1]
    print('{0: <6s}: {1} seconds'.format(scale, time))

print('Total time: {0} seconds'.format(total_time))
print('Complete! Nice work :)')