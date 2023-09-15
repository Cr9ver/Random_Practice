import project

print("Welcome to TIC TAC TOE: ")


while True:

    # PLAY THE GAME

    # SET EVERYTHING UP (BOARD, WHO PLAYS FIRST, CHOOSE MARKERS X, O )
    the_board = [' ']*10
    player1_marker, player2_marker = project.player_input()

    turn = project.choose_first()
    print(f'{turn} will go first')

    play_game = input('Ready to play?  y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False


     # GAME PLAY
    while game_on == True :
        if turn == 'Player 1':

            #Show the board
            project.display_board(the_board)
            # Choose a postiion
            position = project.player_choice(the_board)

            # place the marker on the position
            project.place_marker(the_board,player1_marker,position)

            # Check if they won
            if project.win_check(the_board,player1_marker):
                project.display_board(the_board)
                print('PLAYER 1 HAS WON!! ')
                game_on = False
            else: 
                if project.full_board_check(the_board):
                    project.display_board(the_board)
                    print("TIE GAME !!")
                    game_on = False
                else:
                    turn = 'Player 2'


            # check if there is a tie

            # No tie and no win ? then next player's turn 
        
        # PLAYER ONE TURN

        else:

            #Show the board
            project.display_board(the_board)
            # Choose a postiion
            position = project.player_choice(the_board)

            # place the marker on the position
            project.place_marker(the_board,player2_marker,position)

            # Check if they won
            if project.win_check(the_board,player2_marker):
                project.display_board(the_board)
                print('PLAYER 2 HAS WON!! ')
                game_on = False
            else: 
                if project.full_board_check(the_board):
                    project.display_board(the_board)
                    print("TIE GAME !!")
                    game_on = False
                else:
                    turn = 'Player 1'

     

        # PLAYER TWO TURN 



    if not project.replay():
        break