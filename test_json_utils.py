import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library
    for game_data in json_data["Games"]:
        game = test_data.Game()
        game.title = game_data["Title"]
        game.year = game_data["Year"]
        for platform_data in game_data["Platform"]:
            game.platform = test_data.Platform()
            game.platform.name = platform_data["Name"]
            game.platform.launch_year = platform_data["Launch Year"]
        game_library.add_game(game)
    return game_library
