import user_choice



game_on = True 
game_list = [0,1,2]

while game_on :
    user_choice.display_game(game_list)
    position = user_choice.position_choice()
    game_list = user_choice.replacement_choice(game_list, position)
    user_choice.display_game(game_list)
    game_on = user_choice.gameon_choice()