import logging

from app import db
from sqlalchemy import Column, Integer


class GamePlayer(db.Model):
    __tablename__ = 'gameplayer'

    player_id = Column(Integer, db.ForeignKey('player.id'), primary_key=True)
    game_id = Column(Integer, db.ForeignKey('game.id'), primary_key=True)
    turn = Column(Integer)
    game = db.relationship("Game", back_populates='player')
    player = db.relationship("Player", back_populates='game')

    def __init__(self, game, player, turn):
        self.game = game
        self.player = player
        self.turn = turn

    def __repr__(self):  # pragma: no cover
        return "Game id: {game_id} - User id: {user_id} - Turn: {turn}".format(
            game_id=self.game_id, user_id=self.user_id, turn=self.turn
        )


class GamePlayerController:

    def add_game_player(self, game, player, turn):
        logging.info("Adding a player to a game...")
        game_player = GamePlayer(game, player, turn)
        db.session.add(game_player)
        db.session.commit()
        return game_player

    def get_game_players(self, game_id):
        logging.info("Getting players for game {game_id}".format(game_id=game_id))
        game_player = GamePlayer.query.filter(GamePlayer.game_id == game_id).first()
        return game_player
