import berserk, pickle
from the_token import access_token

session = berserk.TokenSession(access_token)
client = berserk.Client(session=session)

#print(client.users.get_public_data('AlephNaught202'))
games = list(client.games.export_by_player('AlephNaught202', max=10, as_pgn = True))
#print(games[0])

GamesPlayer = list(client.games.export_by_player('AlephNaught202', max=100, as_pgn = True))
with open('Last-100-games-AlephNaught202.pkl', 'wb') as f:
    pickle.dump(GamesPlayer,f)
with open('Last-100-games-AlephNaught202.pkl', 'rb') as f:
    GamesPlayer = pickle.load(f)    

for x in GamesPlayer:
	print("GAME:")
	print(x)

	#retrieves last 100 games of a given player name.
	#with this I can retrieve any game data I need.