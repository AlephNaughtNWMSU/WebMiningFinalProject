import berserk
from the_token import access_token

session = berserk.TokenSession(access_token)
client = berserk.Client(session=session)

#print(client.users.get_public_data('AlephNaught202'))
games = client.games.export_by_player('AlephNaught202', max=10, as_pgn = True)
print(list(games)[0])