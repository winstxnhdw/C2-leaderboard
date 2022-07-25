from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from server import init_server
from config import Config

app = init_server()
app.config.from_object(Config)
db = SQLAlchemy(app)

class Player(db.Model):

    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    score = db.Column(db.Integer)

    def __init__(self, username: str, score: int):

        self.username = username
        self.score = score

class PlayerFormatted:

    def __init__(self, id: int, username: str, score: int):

        self.id = id
        self.username = username
        self.score = score

@app.route('/')
def index() -> str:

    template_player = PlayerFormatted('', '-', '-')
    max_views = 10
    player_list = Player.query.order_by(Player.score.desc()).order_by(Player.id).limit(max_views).all()
    player_list_formatted = [PlayerFormatted(f"#{str(player.id).zfill(4)}", player.username, player.score) for player in player_list]

    if len(player_list) < max_views:
        player_list_formatted = [*player_list_formatted, *([template_player]*(max_views - len(player_list)))]

    return render_template("index.html", player_list=player_list_formatted)

@app.route(f"/{app.config['SECRET_KEY']}/submit_from_unity", methods=["POST"])
def submit() -> str:
    
    username = request.form["username"]
    score = request.form["score"]
    
    player = Player(username, score)
    db.session.add(player)
    db.session.commit()

    return "Player data has been submitted successfully."

@app.route(f"/{app.config['SECRET_KEY']}/clear_leaderboard", methods=["GET"])
def clear_leaderboard() -> str:

    Player.query.delete()
    db.session.commit()
    return "Leaderboard has been cleared."

@app.route(f"/{app.config['SECRET_KEY']}/remove_last", methods=["GET"])
def remove_last() -> str:

    player = Player.query.order_by(Player.id.desc()).first()
    db.session.delete(player)
    db.session.commit()
    
    return "Last player has been removed."

def main():

    port = app.config["PORT"]
    app.run(host="0.0.0.0", port=port, debug=False)

if __name__ == "__main__":
    main()
