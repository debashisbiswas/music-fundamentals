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
if randomize_exercises:
    shuffle(exercises_list)

for scale in scales_list:
    print('--> ' + scale)
    for exercise in exercises_list:
        print((' ' * 4) + exercise)

    theInput = input('\nPress Enter to continue... (q + enter to quit)\n')
    if theInput.lower() == 'q':
        print('Exiting...')
        break

print('Complete!')