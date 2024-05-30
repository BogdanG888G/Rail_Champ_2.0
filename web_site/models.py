from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=1000000)  # Номер комнаты
    name = models.CharField(max_length=1000000)  # Опционально, название комнаты

    def __str__(self):
        return self.number

class Railways(models.Model):
    name = models.CharField(max_length=100, default='Unnamed Railway')  # Название железной дороги
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)  # Связь с комнатой
    is_occupied = models.BooleanField(default=False)  # Флаг занятости



    current_move = models.PositiveIntegerField(default=1)
    move_1 = models.IntegerField(default=-1)
    move_2 = models.IntegerField(default=-1)
    move_3 = models.IntegerField(default=-1)
    move_4 = models.IntegerField(default=-1)
    move_5 = models.IntegerField(default=-1)
    move_6 = models.IntegerField(default=-1)
    move_7 = models.IntegerField(default=-1)
    move_8 = models.IntegerField(default=-1)
    move_9 = models.IntegerField(default=-1)
    move_10 = models.IntegerField(default=-1)
    move_11 = models.IntegerField(default=-1)
    move_12 = models.IntegerField(default=-1)
    move_13 = models.IntegerField(default=-1)
    move_14 = models.IntegerField(default=-1)
    move_15 = models.IntegerField(default=-1)
    move_16 = models.IntegerField(default=-1)
    move_17 = models.IntegerField(default=-1)
    move_18 = models.IntegerField(default=-1)
    move_19 = models.IntegerField(default=-1)
    move_20 = models.IntegerField(default=-1)
    move_21 = models.IntegerField(default=-1)
    move_22 = models.IntegerField(default=-1)
    move_23 = models.IntegerField(default=-1)
    move_24 = models.IntegerField(default=-1)
    move_25 = models.IntegerField(default=-1)
    move_26 = models.IntegerField(default=-1)
    move_27 = models.IntegerField(default=-1)
    move_28 = models.IntegerField(default=-1)
    move_29 = models.IntegerField(default=-1)
    move_30 = models.IntegerField(default=-1)
    move_31 = models.IntegerField(default=-1)
    move_32 = models.IntegerField(default=-1)
    move_33 = models.IntegerField(default=-1)
    move_34 = models.IntegerField(default=-1)
    move_35 = models.IntegerField(default=-1)
    move_36 = models.IntegerField(default=-1)
    move_37 = models.IntegerField(default=-1)
    move_38 = models.IntegerField(default=-1)
    move_39 = models.IntegerField(default=-1)
    move_40 = models.IntegerField(default=-1)
    move_41 = models.IntegerField(default=-1)
    move_42 = models.IntegerField(default=-1)
    move_43 = models.IntegerField(default=-1)
    move_44 = models.IntegerField(default=-1)
    move_45 = models.IntegerField(default=-1)
    move_46 = models.IntegerField(default=-1)
    move_47 = models.IntegerField(default=-1)
    move_48 = models.IntegerField(default=-1)
    move_49 = models.IntegerField(default=-1)
    move_50 = models.IntegerField(default=-1)
    move_51 = models.IntegerField(default=-1)
    move_52 = models.IntegerField(default=-1)
    move_53 = models.IntegerField(default=-1)
    move_54 = models.IntegerField(default=-1)
    move_55 = models.IntegerField(default=-1)
    move_56 = models.IntegerField(default=-1)
    move_57 = models.IntegerField(default=-1)
    move_58 = models.IntegerField(default=-1)
    move_59 = models.IntegerField(default=-1)
    move_60 = models.IntegerField(default=-1)
    key = models.CharField(max_length=30)
    budget = models.IntegerField(default=0)
    sostoyanie_puti = models.IntegerField(default=90)
    len_of_put = models.IntegerField(default=1000)
    stat = models.IntegerField(default=100)
    gryzovye_vagoni = models.IntegerField(default=41)
    pass_vogoni = models.IntegerField(default=10)
    lokomotivi = models.IntegerField(default=10)
    pass_poesda = models.IntegerField(default=10)
    gryz_poesda = models.IntegerField(default=10)
    other_money = models.IntegerField(default=10)
    passeger_per_kilom = models.FloatField(default=0.2)
    amount_sotrudniki = models.IntegerField(default=1)
    zarplata_sotrudnikov = models.IntegerField(default=10)
    average_zarplata_region = models.IntegerField(default=1)
    tonn_per_kilometer = models.IntegerField(default=1)
    perevezeno_pass = models.IntegerField(default=1)

    virychka_ot_gryzov = models.FloatField(default=12_000)
    sebestoimost = models.FloatField(default=80_000)
    financi_po_prochim = models.FloatField(default=1)
    debitorka = models.FloatField(default=0)
    kreditorka = models.FloatField(default=0)
    pogryzka = models.FloatField(default=17002)
    raspisanie_pass_poesdov = models.FloatField(default=60.5)
    raspisanie_prigoroda = models.FloatField(default=60.5)
    dolya_gryzovix_otpravok = models.FloatField(default=60.5)
    average_speed_pass = models.FloatField(default=2533)
    average_speed_gryz = models.FloatField(default=12.5)
    average_proivoditelnost_loko = models.FloatField(default=1)
    time_zadershka = models.FloatField(default=-35)
    besopasnost = models.FloatField(default=-35)
    maks_kolvo_reisov = models.FloatField(default=1)
    maks_kolvo_reisov_gryz = models.FloatField(default=1)
    maks_kolvo_reisov_loko = models.FloatField(default=1)

    sostoyanie_pass = models.IntegerField(default=90)
    sostoyanie_gryz = models.IntegerField(default=90)
    sostoyanie_loko = models.IntegerField(default=90)

    total_score = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name}'

class CalculationResult(models.Model):
    railway = models.ForeignKey(Railways, on_delete=models.CASCADE)
    virychka_ot_gryzov = models.FloatField()
    sebestoimost = models.FloatField()
    financi_po_prochim = models.FloatField()
    debitorka = models.FloatField()
    kreditorka = models.FloatField()
    pogruzka_gryzov = models.FloatField()
    raspisanie_pass_poesdov = models.FloatField()
    raspisanie_prigoroda = models.FloatField(default=1)
    dolya_gryzovix_otpravok = models.FloatField()
    average_speed = models.FloatField()
    average_proivoditelnost_loko = models.FloatField()
    time_zadershka = models.FloatField()
    besopasnost = models.FloatField()

    def __str__(self):
        return f"Результаты для железной дороги {self.railway.name}"

