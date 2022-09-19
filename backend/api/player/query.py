from api.player.models import Player
from django.contrib.auth.models import User

Player.objects.create(user=User.objects.create_user(username='tazim', password='login'), name='tazim', age='24', height='165', email='tazim@gmail.com', password ='login', confirm_password='login')
print(Player.objects.all())

{
    "name": "tazim",
    "age": 25,
    "height": "165",
    "email": "tazim@gmail.com",
    "password": "25795",
    "confirm_password"
}