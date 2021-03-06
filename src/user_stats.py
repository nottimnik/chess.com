from chessdotcom import get_player_stats, get_player_profile, is_player_online
import pprint

printer = pprint.PrettyPrinter()

ratings = [] #where all the current ratings of the player are stored

def get_current_player_rating(username): #the function returns the current ratings of the player
	data = get_player_stats(username).json
	categories = ['chess_blitz', 'chess_rapid', 'chess_bullet', 'chess_daily']
	for category in categories:
		ratings.append(f'{data[category]["last"]["rating"]}')

	ratings.append(f'{data["tactics"]["highest"]["rating"]}')
	ratings.append(f'{data["puzzle_rush"]["best"]["score"]}')

	return ratings

	#Indexes of the ratings: 0 - blitz ; 1 - rapid ; 2 - bullet ; 3 - daily ; 5 - puzzle ; 6 - puzzle rush


def get_status(username): #returns true if the players is online and false if is offline
	data = is_player_online(username).json

	if data['online'] == True:
		return True
	else:
		return False