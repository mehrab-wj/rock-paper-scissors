import random # Import random library for generating random numbers

# Create choices dictionary for defining our choices names and etc...
choices = {
    '0':{
        'name': 'Rock',
        'emoji': '👊',
        'action': 'Smashes'
    },
    '1':{
        'name': 'Paper',
        'emoji': '🖐',
        'action': 'covers'
    },
    '2':{
        'name': 'Scissors',
        'emoji': '✌️',
        'action': 'cut'
    }
}
score_board = {
    'wins': 0,
    'draws': 0,
    'loses': 0
}
print('Welcome to Multiplayer Rock Paper Scissors game!')
print('This game created by www.mehrab.xyz for teaching how to create multiplayer games with socket.io')
print('you can read full tutorial post in reddit: https://www.reddit.com/r/learnpython/comments/idf6ns/create_multiplayer_rock_paper_scissors_in_python/\n')

def find_choice_advantage(choice,choices = choices):
    # Check if our choise - 1 exist in our choices dictionary, it means current choice has advantage on the previews choice
    if str(choice - 1) in choices: return str(int(choice) - 1)
    else: return (len(choices) - 1)
    # when there is no choice above are selected choice, it means we should take the last choice
def print_score_board(score_board = score_board):
    for item in score_board:
        print(item,':',score_board[item])
def print_choices():
    print('your choices in terminal mode is:')
    for choice_index in choices:
        print(choice_index,'-',choices[choice_index]['name'])
print_choices()

while True:
    user_choice = input('Rock Paper Scissors? ')
    if user_choice == 'q': break
    # We dont write else because if when the input is q, the app break and writing else here, will only add one extra and useless line here
    if user_choice not in choices:
        print_choices()
        continue
    computer_choice = str(random.randint(0,2)) # generate random number as computer choice
    # Get user choice advantage
    user_choice_advantage = find_choice_advantage(int(user_choice))
    
    if user_choice == computer_choice: # Check if the user and computer choiced the same option
        score_board['draws'] += 1
        print('[DRWA] Wow you and computer both choiced',choices[user_choice]['name'])
    elif str(user_choice_advantage) == computer_choice: # When user_choice_advantage is equal to computer choice, it means user is winner!
        score_board['wins'] += 1
        print('[WIN] Your',choices[user_choice]['name'],choices[user_choice]['action'],'computer',choices[computer_choice]['name'])
    else:
        score_board['loses'] += 1
        print('[LOSE] Computer',choices[computer_choice]['name'],choices[computer_choice]['action'],'your',choices[user_choice]['name'])

print_score_board()
print('Have a nice day ;)')