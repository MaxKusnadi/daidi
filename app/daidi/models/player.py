import logging

from app import db
from sqlalchemy import Column, String, Integer


class Player(db.Model):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    no_of_wins = Column(Integer)

    def __init__(self, username):
        self.username = username
        self.no_of_wins = 0

    def __repr__(self):  # pragma: no cover
        return "{id}. Username: {username} - No of wins: {wins}".format(
            id=self.id, username=self.username, wins=self.wins)


class PlayerDatabaseController:

    def add_player(self, username):
        logging.info("Checking if the username exists")
        player = self.get_player(username)

        if player:
            logging.error("Username exists")
            return player

        logging.info("Adding a player to database...")
        player = Player(username)
        db.session.add(player)
        db.session.commit()
        return player

    def get_player(self, username):
        logging.info("Getting a username {username}".format(username=username))
        player = Player.query.filter(Player.username == username).first()
        return player
