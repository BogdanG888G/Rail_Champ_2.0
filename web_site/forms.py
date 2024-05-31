from django import forms
from .models import Room, Railways, CalculationResult

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number']

class RailwayChoiceForm(forms.Form):
    selected_railway = forms.ChoiceField(choices=[], label="")

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['selected_railway'].choices = choices


class RailwayManageForm(forms.ModelForm):
    maks_kolvo_reisov_gryz = forms.IntegerField(
        label='Количество рейсов грузовых поездов',
        min_value=0, max_value=1000000000, required=True,
        widget=forms.NumberInput(attrs={
            'style': 'background-color: rgb(2, 67, 143); border-radius: 10px; width: 320px; padding: 10px; color: white; font-size: 15px; margin-top: 10px; margin-left: -200px'
        })
    )

    maks_kolvo_reisov_loko = forms.IntegerField(
        label='Количество рейсов локомотивов',
        min_value=0, max_value=100000000, required=True,
        widget=forms.NumberInput(attrs={
            'style': 'background-color: rgb(2, 67, 143); border-radius: 10px; width: 320px; padding: 10px; color: white; font-size: 15px; margin-top: 10px;margin-left: -240px'
        })
    )

    new_gryzovye_vagoni = forms.IntegerField(
        label='Новые грузовые вагоны (штук)',
        min_value=0, max_value=2000, required=True,
        widget=forms.NumberInput(attrs={
            'type': 'range', 'step': '1', 'value': '0', 'style': 'width: 320px; margin-left:-250px;'
        })
    )

    new_pass_vagoni = forms.IntegerField(
        label='Новые пассажирские вагоны (штук)',
        min_value=0, max_value=2000, required=True,
        widget=forms.NumberInput(attrs={
            'type': 'range', 'step': '1', 'value': '0', 'style': 'width: 320px; margin-left:-250px;'
        })
    )

    new_zarplata_sotrudnikov = forms.IntegerField(
        label='Зарплата сотрудников (тысячи рублей)',
        min_value=0, required=True,
        widget=forms.NumberInput(attrs={
            'style': 'background-color: rgb(2, 67, 143); border-radius: 10px; width: 320px; padding: 10px; color: white; font-size: 15px; margin-top: 10px; margin-left: -200px;'
        })
    )
    repair_puti = forms.BooleanField(
        label='Ремонт путей', required=False,
        widget=forms.CheckboxInput(attrs={
            'style': 'margin-top: 10px;margin-left: -730px;'
        })
    )
    repair_vagoni = forms.BooleanField(
        label='Ремонт вагонов', required=False,
        widget=forms.CheckboxInput(attrs={
            'style': 'margin-top: 10px; margin-left: -730px;'
        })
    )
    repair_loko = forms.BooleanField(
        label='Ремонт локомотивов', required=False,
        widget=forms.CheckboxInput(attrs={
            'style':'margin-left: -680px;'
        })
    )
    maks_kolvo_reisov = forms.IntegerField(
        label='Количество рейсов пассажирских поездов',
        min_value=0, max_value=100000000, required=True,
        widget=forms.NumberInput(attrs={
            'style': 'background-color: rgb(2, 67, 143); border-radius: 10px; width: 320px; padding: 10px; color: white; font-size: 15px; margin-top: 10px; margin-left: -180px'
        })
    )



    class Meta:
        model = Railways
        fields = [
            'name', 'budget', 'sostoyanie_puti', 'len_of_put', 'stat',
            'gryzovye_vagoni', 'pass_vogoni', 'lokomotivi', 'pass_poesda', 'gryz_poesda',
            'other_money', 'amount_sotrudniki', 'zarplata_sotrudnikov',
            'average_zarplata_region', 'tonn_per_kilometer', 'pogryzka', 'perevezeno_pass',
            'maks_kolvo_reisov'
        ]
        labels = {
            'budget': 'Бюджет',
            'sostoyanie_puti': 'Состояние путей',
            'len_of_put': 'Длина путей',
            'stat': 'Штат',
            'gryzovye_vagoni': 'Грузовые вагоны',
            'pass_vogoni': 'Пассажирские вагоны',
            'lokomotivi': 'Локомотивы',
            'pass_poesda': 'Пассажирские поезда',
            'gryz_poesda': 'Грузовые поезда',
            'other_money': 'Другие финансы',
            'passenger_per_kilom': 'Пассажиры на километр',
            'amount_sotrudniki': 'Количество сотрудников',
            'zarplata_sotrudnikov': 'Зарплата сотрудников',
            'average_zarplata_region': 'Средняя зарплата в регионе',
            'tonn_per_kilometer': 'Тонны на километр',
            'pogryzka': 'Погрузка',
            'perevezeno_pass': 'Перевезено пассажиров',
            'maks_kolvo_reisov': 'Максимальное количество рейсов'
        }
        widgets = {
            'maks_kolvo_reisov': forms.HiddenInput(),
            'name': forms.HiddenInput(),
            'budget': forms.HiddenInput(),
            'sostoyanie_puti': forms.HiddenInput(),
            'len_of_put': forms.HiddenInput(),
            'stat': forms.HiddenInput(),
            'gryzovye_vagoni': forms.HiddenInput(),
            'pass_vogoni': forms.HiddenInput(),
            'lokomotivi': forms.HiddenInput(),
            'other_money': forms.HiddenInput(),
            'pass_poesda': forms.HiddenInput(),
            'gryz_poesda': forms.HiddenInput(),
            'passenger_per_kilom': forms.HiddenInput(),
            'amount_sotrudniki': forms.HiddenInput(),
            'average_zarplata_region': forms.HiddenInput(),
            'perevezeno_pass': forms.HiddenInput(),
            'pogryzka': forms.HiddenInput(),
            'zarplata_sotrudnikov': forms.HiddenInput(),
            'tonn_per_kilometer': forms.HiddenInput(),
        }




'''
from django import forms
from .models import Room, Railways, CalculationResult

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number']

class RailwayChoiceForm(forms.Form):
    selected_railway = forms.ChoiceField(choices=[], label="Выберите железную дорогу")

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['selected_railway'].choices = choices


class RailwayManageForm(forms.ModelForm):
    new_gryzovye_vagoni = forms.IntegerField(label='Новые грузовые вагоны', min_value=0, required=True, widget=forms.NumberInput(attrs={'type': 'range', 'step': '1', 'value': '0'}), max_value=100)
    new_pass_vogoni = forms.IntegerField(label='Новые пассажирские вагоны', min_value=0, required=True, widget=forms.NumberInput(attrs={'type': 'range', 'step': '1', 'value': '0'}), max_value=100)
    new_lokomotivi = forms.IntegerField(label='Новые локомотивы', min_value=0, required=True, widget=forms.NumberInput(attrs={'type': 'range', 'step': '1', 'value': '0'}), max_value=100)
    new_zarplata_sotrudnikov = forms.IntegerField(label='Зарплата сотрудников', min_value=0, required=True)
    repair_puti = forms.BooleanField(label='Ремонт путей', required=False)
    repair_vagoni = forms.BooleanField(label='Ремонт вагонов', required=False)
    repair_loko = forms.BooleanField(label='Ремонт локомотивов', required=False)
    maks_kolvo_reisov = forms.IntegerField(label='Количество рейсов пассажирских поездов', min_value=0, required=True, widget=forms.NumberInput(attrs={'type': 'range', 'step': '1', 'value': '0'}), max_value=20000)
    maks_kolvo_reisov_gryz = forms.IntegerField(label='Количество рейсов грузовых поездов', min_value=0, required=True, widget=forms.NumberInput(attrs={'type': 'range', 'step': '1', 'value': '0'}), max_value=20000)
    maks_kolvo_reisov_loko = forms.IntegerField(label='Количество рейсов локомотивов', min_value=0, required=True, widget=forms.NumberInput(attrs={'type': 'range', 'step': '1', 'value': '0'}), max_value=20000)

    def __init__(self, *args, **kwargs):
        data = kwargs.get('initial', {})
        average_speed_pass = data.get('average_speed_pass', 0)
        average_speed_gryz = data.get('average_speed_gryz', 0)
        pass_poesda = data.get('pass_poesda', 0)
        gryz_poesda = data.get('gryz_poesda', 0)
        pass_vogoni = data.get('pass_vogoni', 0)
        gryzovye_vagoni = data.get('gryzovye_vagoni', 0)
        lokomotivi = data.get('lokomotivi', 0)
        super().__init__(*args, **kwargs)
        self.fields['maks_kolvo_reisov'].widget.attrs['readonly'] = True
        self.fields['maks_kolvo_reisov_gryz'].widget.attrs['readonly'] = True
        self.fields['maks_kolvo_reisov_loko'].widget.attrs['readonly'] = True
        self.fields['maks_kolvo_reisov'].initial = self.calculate_max_reisov_pass(average_speed_pass, pass_poesda)
        self.fields['maks_kolvo_reisov_gryz'].initial = self.calculate_max_reisov_gryz(average_speed_gryz, gryz_poesda)
        self.fields['maks_kolvo_reisov_loko'].initial = self.calculate_max_reisov_loko(pass_vogoni, gryzovye_vagoni, lokomotivi)

    def calculate_max_reisov_pass(self, average_speed_pass, pass_poesda):
        if average_speed_pass == 0 or pass_poesda == 0:
            return 1
        return int((1500 / average_speed_pass) * pass_poesda * (30 / (1500 / average_speed_pass)))

    def calculate_max_reisov_gryz(self, average_speed_gryz, gryz_poesda):
        if average_speed_gryz == 0 or gryz_poesda == 0:
            return 1
        return int((1500 / average_speed_gryz) * gryz_poesda * (30 / (1500 / average_speed_gryz)))

    def calculate_max_reisov_loko(self, pass_vogoni, gryzovye_vagoni, lokomotivi):
        if pass_vogoni == 0 or gryzovye_vagoni == 0 or lokomotivi == 0:
            return 1
        return int((1500 / ((pass_vogoni * 50 + gryzovye_vagoni * 35) / 2)) * lokomotivi * (30 / (1500 / ((pass_vogoni * 50 + gryzovye_vagoni * 35) / 2))))

    class Meta:
        model = Railways
        fields = [
            'name', 'budget', 'sostoyanie_puti', 'len_of_put', 'stat',
            'gryzovye_vagoni', 'pass_vogoni', 'lokomotivi', 'pass_poesda', 'gryz_poesda',
            'other_money', 'amount_sotrudniki', 'zarplata_sotrudnikov',
            'average_zarplata_region', 'tonn_per_kilometer', 'pogryzka', 'perevezeno_pass',
            'maks_kolvo_reisov'
        ]
        labels = {
            'budget': 'Бюджет',
            'sostoyanie_puti': 'Состояние путей',
            'len_of_put': 'Длина путей',
            'stat': 'Штат',
            'gryzovye_vagoni': 'Грузовые вагоны',
            'pass_vogoni': 'Пассажирские вагоны',
            'lokomotivi': 'Локомотивы',
            'pass_poesda': 'Пассажирские поезда',
            'gryz_poesda': 'Грузовые поезда',
            'other_money': 'Другие финансы',
            'amount_sotrudniki': 'Количество сотрудников',
            'zarplata_sotrudnikov': 'Зарплата сотрудников',
            'average_zarplata_region': 'Средняя зарплата в регионе',
            'tonn_per_kilometer': 'Тонны на километр',
            'pogryzka': 'Погрузка',
            'perevezeno_pass': 'Перевезено пассажиров',
            'maks_kolvo_reisov': 'Максимальное количество рейсов пассажирских поездов',
            'maks_kolvo_reisov_gryz': 'Максимальное количество рейсов грузовых поездов',
            'maks_kolvo_reisov_loko': 'Максимальное количество рейсов локомотивов'
        }
        widgets = {
            'maks_kolvo_reisov': forms.HiddenInput(),
            'name': forms.HiddenInput(),
            'budget': forms.HiddenInput(),
            'sostoyanie_puti': forms.HiddenInput(),
            'len_of_put': forms.HiddenInput(),
            'stat': forms.HiddenInput(),
            'gryzovye_vagoni': forms.HiddenInput(),
            'pass_vogoni': forms.HiddenInput(),
            'lokomotivi': forms.HiddenInput(),
            'other_money': forms.HiddenInput(),
            'pass_poesda': forms.HiddenInput(),
            'gryz_poesda': forms.HiddenInput(),
            'passenger_per_kilom': forms.HiddenInput(),
            'amount_sotrudniki': forms.HiddenInput(),
            'average_zarplata_region': forms.HiddenInput(),
            'perevezeno_pass': forms.HiddenInput(),
            'pogryzka': forms.HiddenInput(),
            'zarplata_sotrudnikov': forms.HiddenInput(),
            'tonn_per_kilometer': forms.HiddenInput(),
        }

from django import forms
from .models import Railways

class RailwayManageForm(forms.ModelForm):
    new_gryzovye_vagoni = forms.IntegerField(required=False, label='Новые грузовые вагоны')
    new_pass_vogoni = forms.IntegerField(required=False, label='Новые пассажирские вагоны')
    new_lokomotivi = forms.IntegerField(required=False, label='Новые локомотивы')
    new_zarplata_sotrudnikov = forms.FloatField(required=False, label='Новая зарплата сотрудников')
    repair_puti = forms.BooleanField(required=False, label='Ремонт путей')
    repair_vagoni = forms.BooleanField(required=False, label='Ремонт вагонов')
    repair_loko = forms.BooleanField(required=False, label='Ремонт локомотивов')

    class Meta:
        model = Railways
        fields = [
            'budget', 'sostoyanie_puti', 'len_of_put', 'stat',
            'gryzovye_vagoni', 'pass_vogoni', 'lokomotivi', 'pass_poesda',
            'gryz_poesda', 'other_money', 'amount_sotrudniki',
            'zarplata_sotrudnikov', 'average_zarplata_region', 'tonn_per_kilometer',
            'pogryzka', 'perevezeno_pass'
        ]
        widgets = {
            'budget': forms.HiddenInput(),
            'sostoyanie_puti': forms.HiddenInput(),
            'len_of_put': forms.HiddenInput(),
            'stat': forms.HiddenInput(),
            'gryzovye_vagoni': forms.HiddenInput(),
            'pass_vogoni': forms.HiddenInput(),
            'lokomotivi': forms.HiddenInput(),
            'pass_poesda': forms.HiddenInput(),
            'gryz_poesda': forms.HiddenInput(),
            'other_money': forms.HiddenInput(),
            'amount_sotrudniki': forms.HiddenInput(),
            'zarplata_sotrudnikov': forms.HiddenInput(),
            'average_zarplata_region': forms.HiddenInput(),
            'tonn_per_kilometer': forms.HiddenInput(),
            'pogryzka': forms.HiddenInput(),
            'perevezeno_pass': forms.HiddenInput(),
        }
'''