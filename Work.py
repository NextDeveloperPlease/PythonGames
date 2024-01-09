import pandas as pd
import Settings as st
import random

root_dir = st.get_root()

def work(player):
    '''Three options: Do the job, ask for a promotion, yell at your boss and quit''' # If I can figure it out, it would be cool to have multiple different jobs possible.
    '''Working increases rapport with the boss and increases your skill. You can'''
    '''get a new job with higher skills, higher promotions with rapport'''
    user_input = None
    getting_input = True
    player_job = player.get_job()
    jobs = pd.read_csv(root_dir + '/Jobs_with_bosses.csv')
    while getting_input:
        user_input = input("1. (Work)\t2. Ask for a (promotion)\n3. (Quit) and cuss out the boss 4. (Apply) for new job.\n").lower()
        getting_input = False
        match(user_input):
            case 'work':
                if player_job == None: 
                    print("You don't have a job, you bum!")
                    print(jobs['name'])
                else: 
                    player.add(player_job['pay'])
                    player.clock.update(player_job['duration'])
            case 'promotion': ''
            case 'quit': ''
            case 'apply':
                possible_jobs = jobs[jobs['skill_required'] <= player.get_skill_level()]
                actual_jobs = None
                if len(possible_jobs) <= 0:
                    print("I don't know how you did it, but you did it.\nThere are no possible jobs for you")
                elif len(possible_jobs) < 10:
                    actual_jobs = possible_jobs
                else:
                    actual_jobs = possible_jobs.sample(10)
                print(actual_jobs)
                
            case _: 
                print("Sorry, I didn't catch that.")
                getting_input = True