def work():
    '''Three options: Do the job, ask for a promotion, yell at your boss and quit''' # If I can figure it out, it would be cool to have multiple different jobs possible.
    '''Working increases rapport with the boss and increases your skill. You can'''
    '''get a new job with higher skills, higher promotions with rapport'''
    user_input = None
    getting_input = True
    while getting_input:
        user_input = input("1. (Work)\t2. Ask for a (promotion)\n3. (Quit) (and cuss out the boss) 4. (Apply) for new job.").lower()
        getting_input = False
        match(user_input):
            case 'work': 
              ''  
            case 'promotion': ''
            case 'quit': ''
            case 'apply': ''
            case _: 
                print("Sorry, I didn't catch that.")
                getting_input = True