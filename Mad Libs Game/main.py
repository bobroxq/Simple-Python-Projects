from stories import*
from random_stories import*

dct = {'1':fifty_shades, '2':awkward_encounter, '3':asking_out, '4':restroom_recon, '5':job_interview, '6':giraffe_facts}
lnth = {fifty_shades:29, awkward_encounter:18, asking_out:13, restroom_recon:15, job_interview:18, giraffe_facts:17}
random_dct = {'1':random_fifty_shades, '2':random_awkward_encounter, '3':random_asking_out, '4':random_restroom_recon, '5':random_job_interview, '6':random_giraffe_facts}

print("""Choose a story to get started!
1. 50 Shades of Madlibs
2. An Awkward Encounter
3. Asking Someone Out
4. Restroom Recon
5. Job Interview from Hell
6. Giraffe Facts""")

choice = input("Enter a number: " )

print(f'This story has {lnth[dct[choice]]} blanks.') 
answer = input("Would you like to use the randomized autofill feature? Type yes or no: ")
if answer == "yes":
    random_dct[choice]()
else:
    dct[choice]()

