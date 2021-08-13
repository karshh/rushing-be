from app import app
from controllers.players_controller import players

app.register_blueprint(players, url_prefix='/players')
if __name__ == '__main__':
    app.run()
