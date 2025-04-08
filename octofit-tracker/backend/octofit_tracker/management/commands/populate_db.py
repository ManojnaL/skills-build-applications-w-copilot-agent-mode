from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.filter(pk__isnull=False).delete()
        Team.objects.filter(pk__isnull=False).delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        user1 = User.objects.create(email='thundergod@mhigh.edu', name='Thunder God')
        user2 = User.objects.create(email='metalgeek@mhigh.edu', name='Metal Geek')
        user3 = User.objects.create(email='zerocool@mhigh.edu', name='Zero Cool')
        user4 = User.objects.create(email='crashoverride@mhigh.edu', name='Crash Override')
        user5 = User.objects.create(email='sleeptoken@mhigh.edu', name='Sleep Token')

        self.stdout.write(self.style.SUCCESS(f'Created user: {user1.email}'))
        self.stdout.write(self.style.SUCCESS(f'Created user: {user2.email}'))
        self.stdout.write(self.style.SUCCESS(f'Created user: {user3.email}'))
        self.stdout.write(self.style.SUCCESS(f'Created user: {user4.email}'))
        self.stdout.write(self.style.SUCCESS(f'Created user: {user5.email}'))

        self.stdout.write(self.style.SUCCESS(f'User ID: {user1.id}, Email: {user1.email}'))
        self.stdout.write(self.style.SUCCESS(f'User ID: {user2.id}, Email: {user2.email}'))
        self.stdout.write(self.style.SUCCESS(f'User ID: {user3.id}, Email: {user3.email}'))
        self.stdout.write(self.style.SUCCESS(f'User ID: {user4.id}, Email: {user4.email}'))
        self.stdout.write(self.style.SUCCESS(f'User ID: {user5.id}, Email: {user5.email}'))

        users = [user1, user2, user3, user4, user5]

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(user1, user2, user3)
        team2.members.add(user4, user5)

        # Create activities
        activities = [
            Activity(user=User.objects.get(email='thundergod@mhigh.edu'), activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(user=User.objects.get(email='metalgeek@mhigh.edu'), activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(user=User.objects.get(email='zerocool@mhigh.edu'), activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(user=User.objects.get(email='crashoverride@mhigh.edu'), activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(user=User.objects.get(email='sleeptoken@mhigh.edu'), activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=User.objects.get(email='thundergod@mhigh.edu'), score=100),
            Leaderboard(user=User.objects.get(email='metalgeek@mhigh.edu'), score=90),
            Leaderboard(user=User.objects.get(email='zerocool@mhigh.edu'), score=95),
            Leaderboard(user=User.objects.get(email='crashoverride@mhigh.edu'), score=85),
            Leaderboard(user=User.objects.get(email='sleeptoken@mhigh.edu'), score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))