from random import shuffle

print('--- MUSIC FUNDAMENTALS ---\n')

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

shuffle(scales_list)
shuffle(exercises_list)
for scale in scales_list:
    print('--> ' + scale)
    for exercise in exercises_list:
        print('\t' + exercise)

    theInput = input('\nPress Enter to continue... (q + enter to quit)\n')
    if theInput.lower() == 'q':
        print('Exiting...')
        break