import bottle
import os
import random

@bottle.route('/')
def index():
    return 'This is a snake.'

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#33CA7F',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'battlesnake-python'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    #return {
    #    'move': random.choice(directions),
    #    'taunt': 'battlesnake-python!'
    #}

    return {
        'move': "left",
        'taunt': 'battlesnake-python!'
        #if last move equals left, go right
        if ('move' = "left"): #searching for name of last move?
            'move'= "right"
        else 'move' = "left"
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '192.168.0.16'), port=os.getenv('PORT', '8080'))
