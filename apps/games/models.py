from django.db import models
from apps.users.models import MainUser
import random
from decimal import Decimal


class Room(models.Model):
    room_name = models.CharField(max_length=50)
    players = models.ManyToManyField(MainUser, related_name='rooms', blank=True)
    max_players = models.IntegerField(default=4)  # Поле для хранения максимального количества игроков
    loser_rule = models.IntegerField(default=4)  # Поле для хранения правила (каждый N-ый игрок проигрывает)
    game_amount = models.IntegerField(default=10)

    def current_player_count(self):
        return self.players.count()

    def determine_losers(self):
        current_count = self.current_player_count()
        if current_count >= self.max_players and current_count >= self.loser_rule:
            players_list = list(self.players.all())
            losers = random.sample(players_list, self.loser_rule)  # Рандомный выбор проигравших
            return losers
        return None

    def clear_players(self):
        self.players.clear()
        self.save()

    def __str__(self):
        return self.room_name


class RoomBase(models.Model):
    room_id = models.IntegerField()
    room_players = models.ManyToManyField(MainUser, related_name='room_players', blank=True)
    room_max_players = models.IntegerField(default=4)
    room_loser_rule = models.IntegerField(default=4)
    room_game_amount = models.IntegerField(default=10)
    winners = models.ManyToManyField(MainUser, related_name='winners', blank=True)
    losers = models.ManyToManyField(MainUser, related_name='losers', blank=True)
    date_time = models.DateTimeField()
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

