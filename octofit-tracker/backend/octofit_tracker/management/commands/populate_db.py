from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Limpa os dados existentes de forma compatível com ObjectIdField
        for model in [Activity, Leaderboard, Workout, User, Team]:
            for obj in model.objects.all():
                obj.delete()

        # Cria times
        marvel = Team.objects.create(name='Marvel', description='Time dos heróis Marvel')
        dc = Team.objects.create(name='DC', description='Time dos heróis DC')

        # Cria usuários
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)
        diana = User.objects.create(name='Diana Prince', email='diana@dc.com', team=dc.name)

        # Cria atividades
        Activity.objects.create(user=tony, type='Corrida', duration=30, date='2024-01-01')
        Activity.objects.create(user=steve, type='Natação', duration=45, date='2024-01-02')
        Activity.objects.create(user=clark, type='Ciclismo', duration=60, date='2024-01-03')
        Activity.objects.create(user=diana, type='Yoga', duration=50, date='2024-01-04')

        # Cria treinos
        Workout.objects.create(name='Treino Marvel', description='Treino intenso para heróis Marvel', suggested_for='Marvel')
        Workout.objects.create(name='Treino DC', description='Treino de força para heróis DC', suggested_for='DC')

        # Cria leaderboard
        Leaderboard.objects.create(user=tony, points=100, rank=1)
        Leaderboard.objects.create(user=steve, points=90, rank=2)
        Leaderboard.objects.create(user=clark, points=95, rank=1)
        Leaderboard.objects.create(user=diana, points=85, rank=2)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Cria usuários
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='123', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@marvel.com', password='123', team=marvel)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='123', team=dc)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='123', team=dc)

        # Cria atividades
        Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='bike', duration=45, calories=400)
        Activity.objects.create(user=clark, type='swim', duration=60, calories=500)
        Activity.objects.create(user=bruce, type='walk', duration=20, calories=150)

        # Cria workouts
        Workout.objects.create(name='Full Body', description='Treino completo', duration=60)
        Workout.objects.create(name='Cardio', description='Treino de cardio', duration=30)

        # Cria leaderboard
        Leaderboard.objects.create(user=tony, points=1000)
        Leaderboard.objects.create(user=steve, points=900)
        Leaderboard.objects.create(user=clark, points=1100)
        Leaderboard.objects.create(user=bruce, points=950)

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de super heróis!'))
