import logging

from app import db
from sqlalchemy import Column, Integer, Boolean


class Game(db.Model):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    overall_winner = Column(Integer)
    is_on = Column(Boolean)
    is_started = Column(Boolean)

    def __init__(self):
        self.overall_winner = None
        self.is_on = True
        self.is_started = False

    def __repr__(self):  # pragma: no cover
        return "{id}. Winner: {winner} - is_on: {is_on} - is_started: {is_started}".format(
            id=self.id, winner=self.overall_winner, is_on=self.is_on, is_started=self.is_started)


class GameDatabaseController:

    def add_game(self):
        logging.info("Adding a game to database...")
        game = Game()
        db.session.add(game)
        db.session.commit()
        return game

    def get_game(self, game_id):
        logging.info("Getting a game of id {game_id}".format(game_id=game_id))
        game = Game.query.filter(Game.id == game_id).first()
        return game

    def finish_game(self, game_id):
        logging.info("Finishing game {game_id}".format(game_id=game_id))
        game = self.get_game(game_id)
        if game:
            game.is_on = False
            db.session.commit()
        return game

    def start_game(self, game_id):
        logging.info("Starting game {game_id}".format(game_id=game_id))
        game = self.get_game(game_id)
        if game:
            game.is_started = True
            db.session.commit()
        return game
