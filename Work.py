import pandas as pd
import Settings as st
from Clock import time
import numpy as np

root_dir = st.get_root()

def work(player):
    '''Three options: Do the job, ask for a promotion, yell at your boss and quit''' # If I can figure it out, it would be cool to have multiple different jobs possible.
    '''Working increases rapport with the boss and increases your skill. You can'''
    '''get a new job with higher skills, higher promotions with rapport'''
    user_input = None
    getting_input = True
    jobs = pd.read_csv(root_dir + '/Jobs_with_bosses.csv')
    
    cuss = ''
    if st.mature:
        cuss = 'cuss out'
    else:
        cuss = 'yell at'
    
    while getting_input:
        user_input = input(f"1. (Work)\t2. Ask for a (promotion)\n3. (Quit) and {cuss} the boss 4. (Apply) for new job.\n").lower()
        getting_input = False
        match(user_input):
            case 'work':
                if not isinstance(player.get_player_info('job'), pd.DataFrame):
                    print(f"You don't have a job, you {st.get_insult()}!")
                else: 
                    work_time = time.convert_to_hours(player.get_player_info('duration'))
                    pay = player.get_player_info('pay') * work_time
                    player.add(pay)
                    player.clock.update(player.get_player_info('duration'))
                    print(f"You worked {work_time} hours and made ${pay}")
                    print(f"Your total wallet balance is now ${player.get_player_info('wallet')}")
                    st.wait()
                    
            case 'promotion':
                if not isinstance(player.get_player_info('job'), pd.DataFrame):
                    print(f"You don't have a job, you {st.get_insult()}!")
                else:
                    print(player.get_player_info('rapport'))
                    print(player.get_player_info('rapport_required'))
                    if player.get_player_info('rapport') >= player.get_player_info('rapport_required'):
                        '''Increase their pay by a random integer'''
                        if st.mature:
                            print("Fuck it, here you go.")
                            increase = np.random.randint(1,5)
                            player.increase_pay(increase)
                            print(f'You make ${increase} more')
                            pay = player.get_player_info('pay')
                            print(f'Your current pay is {pay}')
                        else:
                            print("Screw it, here you go.")
                            increase = np.random.randint(1,5)
                            player.increase_pay(increase)
                            print(f'You make ${increase} more')
                            pay = player.get_player_info('pay')
                            print(f'Your current pay is {pay}')
                    else:
                        if st.mature:
                            print(f"Get the fuck out, you {st.get_insult()}")
                        else:
                            print(f"Get out of here, you {st.get_insult()}")
                    st.wait()
            
            case 'quit': 
                if not isinstance(player.get_player_info('job'), pd.DataFrame): 
                    print(f"You {st.get_insult()}, you don't have a job")
                else:
                    name = player.get_player_info('boss_name').split(' ')
                    print(f'Hey {name[0]}! You suck, you "{st.get_insult()}"!')
                    player.quit_job()
                    st.wait()
                    
            case 'apply':
                not_selected = True
                possible_jobs = jobs[jobs['skill_required'] <= player.get_player_info('skill')]
                while not_selected:
                    actual_jobs = None
                    if len(possible_jobs) <= 0:
                        print("I don't know how you did it, but you did it.\nThere are no possible jobs for you.")
                    elif len(possible_jobs) < 10:
                        actual_jobs = possible_jobs
                    else:
                        actual_jobs = possible_jobs.sample(10)
                    print(actual_jobs)
                    
                    user_input = input("Enter the full name of the Boss you want to work for: ")
                    name_matches = actual_jobs['name'].str.contains(user_input, case=False)
                    potential_jobs = actual_jobs[name_matches]
                    print(potential_jobs)
                    
                    user_input = input("Enter the full name of the job you want to work for: ")
                    name_matches = potential_jobs['job'].str.contains(user_input, case=False)
                    selected_job = potential_jobs[name_matches]
                    
                    if selected_job.shape[0] > 1:
                        print('Sorry, you have selected more than one job.')
                        print(selected_job)
                        not_selected = True
                        st.wait()
                    elif selected_job.shape[0] < 1:
                        print('Sorry, you have selected less than one job.')
                        print(selected_job)
                        not_selected = True
                        st.wait()
                    else:
                        not_selected = False
                player.set_job(selected_job)
                st.wait()
                    
            case _: 
                print("Sorry, I didn't catch that.")
                getting_input = True