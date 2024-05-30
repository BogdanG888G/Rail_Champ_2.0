# web_site/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Room, Railways

@receiver(post_save, sender=Room)
def create_railways_for_room(sender, instance, created, **kwargs):
    if created:
        Railways.objects.create(
            room=instance,
            move_1=-1,
            move_2=-1,
            key=f'Room_{instance.number}_Railway',
            budget=0,
            sostoyanie_puti=90,
            len_of_put=1000,
            stat=100,
            gryzovye_vagoni=41,
            pass_vogoni=10,
            lokomotivi=10,
            pass_poesda=10,
            gryz_poesda=10,
            other_money=10,
            passeger_per_kilom=0.2,
            amount_sotrudniki=1,
            zarplata_sotrudnikov=10,
            average_zarplata_region=1,
            tonn_per_kilometer=1,
            pogryzka=1,
            perevezeno_pass=1
        )
