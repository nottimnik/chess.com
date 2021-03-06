from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def get_leaderboard(category: "blitz"):
	category = leaderboards_key(category)
	data = get_leaderboards().json
	leaderboard = { #the dictionary where the information of the top 50 users of that category will be stored

	}

	for idx, entry in enumerate(data[category]):
		username = f'{entry["username"]}'
		score = f'{entry["score"]}'
		leaderboard[idx+1] = [username, score]
	return leaderboard

def leaderboards_key(category): #transforms the category entered by the user into the keys used by chess.com
	key = ""
	if(category == "daily"):
		key = "daily"
	elif(category == "daily960"):
		key = "daily960"
	elif(category == "rapid"):
		key = "live_rapid"
	elif(category == "blitz"):
		key = "live_blitz"
	elif(category == "bullet"):
		key = "live_bullet"
	elif(category == "bughouse"):
		key = "live_bughouse"
	elif(category == "doubles"):
		key = "live_bughouse"
	elif(category == "blitz960"):
		key = "live_blitz960"
	elif(category == "threecheck"):
		key = "live_threecheck"
	elif(category == "crazyhouse"):
		key = "live_crazyhouse"
	elif(category == "kingofthehill"):
		key = "live_kingofthehill"
	elif(category == "puzzles"):
		key = "puzzles"
	else:
		key = None #if the category is invalid

	return key
