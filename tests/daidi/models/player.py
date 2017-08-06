import unittest
import os
import tempfile

from app import app

from app.daidi.models.player import Player, PlayerDatabaseController


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.controller = GratitudeDatabaseController()
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = app.app.test_client()
        app.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])


    def test_create(self):
        assert True
