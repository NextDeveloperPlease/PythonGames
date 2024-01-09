import pandas as pd
import Settings as st

root_dir = st.get_root()

def work(player):
    '''Three options: Do the job, ask for a promotion, yell at your boss and quit''' # If I can figure it out, it would be cool to have multiple different jobs possible.
    '''Working increases rapport with the boss and increases your skill. You can'''
    '''get a new job with higher skills, higher promotions with rapport'''
    user_input = None
    getting_input = True
    player_job = player.get_player_info('job')
    jobs = pd.read_csv(root_dir + '/Jobs_with_bosses.csv')
    while getting_input:
        user_input = input("1. (Work)\t2. Ask for a (promotion)\n3. (Quit) and cuss out the boss 4. (Apply) for new job.\n").lower()
        getting_input = False
        match(user_input):
            case 'work':
                if not isinstance(player.get_job(), pd.DataFrame):
                    print("You don't have a job, you bum!")
                else: 
                    player.add(player_job['pay'])
                    player.clock.update(player_job['duration'])
                    
            case 'promotion': ''
            case 'quit': 
                if not isinstance(player.get_player_info('job'), pd.DataFrame): 
                    print("You dumbass, you don't have a job")
                else:
                    name = player.get_player_info('boss_name').split(' ')
                    print(f"Hey {name[0]}! You suck ass!")
                    player.quit_job()
                    st.wait()
                    
            case 'apply':
                possible_jobs = jobs[jobs['skill_required'] <= player.get_player_info('skill')]
                actual_jobs = None
                if len(possible_jobs) <= 0:
                    print("I don't know how you did it, but you did it.\nThere are no possible jobs for you")
                elif len(possible_jobs) < 10:
                    actual_jobs = possible_jobs
                else:
                    actual_jobs = possible_jobs.sample(10)
                    #duplicate_names = actual_jobs[actual_jobs.duplicated('name')]['name']
                    #actual_jobs = actual_jobs[~actual_jobs.duplicated('name', keep='first')]
                print(actual_jobs)
                
                user_input = input("Enter the full name of the Boss you want to work for: ")
                name_matches = actual_jobs['name'].str.contains(user_input, case=False)
                potential_jobs = actual_jobs[name_matches]
                print(potential_jobs)
                
                user_input = input("Enter the full name of the job you want to work for: ")
                name_matches = potential_jobs['job'].str.contains(user_input, case=False)
                selected_job = potential_jobs[name_matches]
                player.set_job(selected_job)
                st.wait()
                    
            case _: 
                print("Sorry, I didn't catch that.")
                getting_input = True