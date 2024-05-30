from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Railways, CalculationResult
from .forms import RoomForm, RailwayChoiceForm, RailwayManageForm, RailwayCalculationForm

from random import *

RAILWAYS_DATA = [
    {
        'name': 'Октябрьская железная дорога',
        'key': 'oktyabrskaya_key',
        'budget': 18837993258,
        'sostoyanie_puti': 90,
        'len_of_put': 13323,
        'stat': 100,
        'gryzovye_vagoni': 16882,
        'pass_vogoni': 3401,
        'lokomotivi': 2261,
        'pass_poesda': 213,
        'gryz_poesda': 531,
        'other_money': 160,
        'passeger_per_kilom': 2.7,
        'amount_sotrudniki': 66,
        'zarplata_sotrudnikov': 83,
        'average_zarplata_region': 68,
        'tonn_per_kilometer': 3,
        'pogryzka': 102,
        'perevezeno_pass': 145,
    },
    {
        'name': 'Калининградская железная дорога',
        'key': 'kaliningradskaya_key',
        'budget': 1220274867,
        'sostoyanie_puti': 90,
        'len_of_put': 1100,
        'stat': 100,
        'gryzovye_vagoni': 1324,
        'pass_vogoni': 188,
        'lokomotivi': 146,
        'pass_poesda': 15,
        'gryz_poesda': 20,
        'other_money': 10,
        'passeger_per_kilom': 2.7,
        'amount_sotrudniki': 4,
        'zarplata_sotrudnikov': 60,
        'average_zarplata_region': 55,
        'tonn_per_kilometer': 3,
        'pogryzka': 8,
        'perevezeno_pass': 8,
    },
    {
        'name': 'Московская железная дорога',
        'key': 'moskovskaya_key',
        'budget': 67115117680,
        'sostoyanie_puti': 90,
        'len_of_put': 13000,
        'stat': 100,
        'gryzovye_vagoni': 3310,
        'pass_vogoni': 20172,
        'lokomotivi': 8054,
        'pass_poesda': 1005,
        'gryz_poesda': 37,
        'other_money': 570,
        'passeger_per_kilom': 3,
        'amount_sotrudniki': 69,
        'zarplata_sotrudnikov': 75,
        'average_zarplata_region': 136,
        'tonn_per_kilometer': 3,
        'pogryzka': 20,
        'perevezeno_pass': 860,
    },
    {
        'name': 'Горьковская железная дорога',
        'key': 'gorkovskaya_key',
        'budget': 5109901005,
        'sostoyanie_puti': 90,
        'len_of_put': 11506,
        'stat': 100,
        'gryzovye_vagoni': 4800,
        'pass_vogoni': 891,
        'lokomotivi': 613,
        'pass_poesda': 56,
        'gryz_poesda': 53,
        'other_money': 43,
        'passeger_per_kilom': 3.3,
        'amount_sotrudniki': 49,
        'zarplata_sotrudnikov': 50,
        'average_zarplata_region': 78,
        'tonn_per_kilometer': 3,
        'pogryzka': 29,
        'perevezeno_pass': 38,
    },
    {
        'name': 'Северная железная дорога',
        'key': 'severnaya_key',
        'budget': 5414969722,
        'sostoyanie_puti': 90,
        'len_of_put': 8500,
        'stat': 100,
        'gryzovye_vagoni': 9434,
        'pass_vogoni': 328,
        'lokomotivi': 650,
        'pass_poesda': 21,
        'gryz_poesda': 104,
        'other_money': 46,
        'passeger_per_kilom': 3.5,
        'amount_sotrudniki': 65,
        'zarplata_sotrudnikov': 69,
        'average_zarplata_region': 58,
        'tonn_per_kilometer': 3,
        'pogryzka': 57,
        'perevezeno_pass': 14,
    },
    {
        'name': 'Северо-Кавказская железная дорога',
        'key': 'severo_kavkazskaya_key',
        'budget': 8770725606,
        'sostoyanie_puti': 90,
        'len_of_put': 6357,
        'stat': 100,
        'gryzovye_vagoni': 9599,
        'pass_vogoni': 1337,
        'lokomotivi': 1052,
        'pass_poesda': 84,
        'gryz_poesda': 106,
        'other_money': 75,
        'passeger_per_kilom': 2.6,
        'amount_sotrudniki': 55,
        'zarplata_sotrudnikov': 45,
        'average_zarplata_region': 64,
        'tonn_per_kilometer': 3,
        'pogryzka': 58,
        'perevezeno_pass': 57,
    },
    {
        'name': 'Юго-Восточная железная дорога',
        'key': 'yugo_vostochnaya_key',
        'budget': 7702985097,
        'sostoyanie_puti': 90,
        'len_of_put': 10000,
        'stat': 100,
        'gryzovye_vagoni': 14896,
        'pass_vogoni': 258,
        'lokomotivi': 924,
        'pass_poesda': 26,
        'gryz_poesda': 147,
        'other_money': 65,
        'passeger_per_kilom': 2.5,
        'amount_sotrudniki': 31,
        'zarplata_sotrudnikov': 65,
        'average_zarplata_region': 60,
        'tonn_per_kilometer': 3,
        'pogryzka': 90,
        'perevezeno_pass': 11,
    },
    {
        'name': 'Восточно-Сибирская железная дорога',
        'key': 'vostochno-sibirskaya_key',
        'budget': 5186168184,
        'sostoyanie_puti': 90,
        'len_of_put': 6300,
        'stat': 100,
        'gryzovye_vagoni': 9268,
        'pass_vogoni': 281,
        'lokomotivi': 622,
        'pass_poesda': 18,
        'gryz_poesda': 102,
        'other_money': 30,
        'passeger_per_kilom': 2.3,
        'amount_sotrudniki': 27,
        'zarplata_sotrudnikov': 65,
        'average_zarplata_region': 58,
        'tonn_per_kilometer': 3,
        'pogryzka': 36,
        'perevezeno_pass': 11,
    },
        {
        'name': 'Приволжская железная дорога',
        'key': 'privolzhskaya_key',
        'budget': 3584557422,
        'sostoyanie_puti': 90,
        'len_of_put': 6300,
        'stat': 100,
        'gryzovye_vagoni': 5958,
        'pass_vogoni': 258,
        'lokomotivi': 430,
        'pass_poesda': 16,
        'gryz_poesda': 66,
        'other_money': 30,
        'passeger_per_kilom': 2.3,
        'amount_sotrudniki': 27,
        'zarplata_sotrudnikov': 65,
        'average_zarplata_region': 58,
        'tonn_per_kilometer': 3,
        'pogryzka': 36,
        'perevezeno_pass': 11,
        },
{
        'name': 'Куйбышевская железная дорога',
        'key': 'kuybish_key',
        'budget': 6330175872,
        'sostoyanie_puti': 90,
        'len_of_put': 8125,
        'stat': 100,
        'gryzovye_vagoni': 10593,
        'pass_vogoni': 446,
        'lokomotivi': 760,
        'pass_poesda': 28,
        'gryz_poesda': 117,
        'other_money': 54,
        'passeger_per_kilom': 2.6,
        'amount_sotrudniki': 45,
        'zarplata_sotrudnikov': 48,
        'average_zarplata_region': 61,
        'tonn_per_kilometer': 3,
        'pogryzka': 64,
        'perevezeno_pass': 19,
    },
{
        'name': 'Свердловская железная дорога',
        'key': 'sverdlovksaya_key',
        'budget': 13346756357,
        'sostoyanie_puti': 90,
        'len_of_put': 9800,
        'stat': 100,
        'gryzovye_vagoni': 23668,
        'pass_vogoni': 751,
        'lokomotivi': 1602,
        'pass_poesda': 47,
        'gryz_poesda': 261,
        'other_money': 113,
        'passeger_per_kilom': 3.1,
        'amount_sotrudniki': 60,
        'zarplata_sotrudnikov': 47,
        'average_zarplata_region': 60,
        'tonn_per_kilometer': 3,
        'pogryzka': 143,
        'perevezeno_pass': 32,
    },
{
        'name': 'Южно-Уральская железная дорога',
        'key': 'yuzhural_key',
        'budget': 5720038439,
        'sostoyanie_puti': 90,
        'len_of_put': 7567,
        'stat': 100,
        'gryzovye_vagoni': 10924,
        'pass_vogoni': 211,
        'lokomotivi': 686,
        'pass_poesda': 17,
        'gryz_poesda': 121,
        'other_money': 49,
        'passeger_per_kilom': 2,
        'amount_sotrudniki': 43,
        'zarplata_sotrudnikov': 47,
        'average_zarplata_region': 60,
        'tonn_per_kilometer': 3,
        'pogryzka': 66,
        'perevezeno_pass': 9,
    },
{
        'name': 'Западная-Сибирская железная дорога',
        'key': 'zapadsibir_key',
        'budget': 3149834500,
        'sostoyanie_puti': 90,
        'len_of_put': 8985,
        'stat': 100,
        'gryzovye_vagoni': 50,
        'pass_vogoni': 962,
        'lokomotivi': 378,
        'pass_poesda': 60,
        'gryz_poesda': 36,
        'other_money': 27,
        'passeger_per_kilom': 3,
        'amount_sotrudniki': 52,
        'zarplata_sotrudnikov': 63,
        'average_zarplata_region': 65,
        'tonn_per_kilometer': 3,
        'pogryzka': 0.3,
        'perevezeno_pass': 41,
    },
{
        'name': 'Красноярская железная дорога',
        'key': 'krasnoyarskaya_key',
        'budget': 6635244589,
        'sostoyanie_puti': 90,
        'len_of_put': 4572,
        'stat': 100,
        'gryzovye_vagoni': 13075,
        'pass_vogoni': 188,
        'lokomotivi': 796,
        'pass_poesda': 12,
        'gryz_poesda': 144,
        'other_money': 56,
        'passeger_per_kilom': 2.7,
        'amount_sotrudniki': 26,
        'zarplata_sotrudnikov': 80,
        'average_zarplata_region': 77,
        'tonn_per_kilometer': 3,
        'pogryzka': 79,
        'perevezeno_pass': 8,
    },
{
        'name': 'Забайкальская железная дорога',
        'key': 'zabaikal_key',
        'budget': 2059213838,
        'sostoyanie_puti': 90,
        'len_of_put': 8300,
        'stat': 100,
        'gryzovye_vagoni': 3972,
        'pass_vogoni': 70,
        'lokomotivi': 247,
        'pass_poesda': 18,
        'gryz_poesda': 44,
        'other_money': 18,
        'passeger_per_kilom': 2.7,
        'amount_sotrudniki': 40,
        'zarplata_sotrudnikov': 54,
        'average_zarplata_region': 80,
        'tonn_per_kilometer': 3,
        'pogryzka': 24,
        'perevezeno_pass': 3,
    },
{
        'name': 'Дальневосточная железная дорога',
        'key': 'dalnevostochnaya_key',
        'budget': 6482710230,
        'sostoyanie_puti': 90,
        'len_of_put': 1582,
        'stat': 100,
        'gryzovye_vagoni': 12248,
        'pass_vogoni': 258,
        'lokomotivi': 778,
        'pass_poesda': 16,
        'gryz_poesda': 135,
        'other_money': 55,
        'passeger_per_kilom': 2.6,
        'amount_sotrudniki': 53,
        'zarplata_sotrudnikov': 60,
        'average_zarplata_region': 73,
        'tonn_per_kilometer': 3,
        'pogryzka': 74,
        'perevezeno_pass': 11,
    }

]

'''def check_room_existence(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        room, created = Room.objects.get_or_create(number=room_number)
        if created:
            # Дополнительно можно установить имя или другие поля, если требуется
            room.save()
        return redirect('choose_railway', room_id=room.id)
    return render(request, 'check_room_existence.html')
'''


def check_room_existence(request):
    rooms = Room.objects.all()
    room_data = []
    for room in rooms:
        occupied_railways = Railways.objects.filter(room=room, is_occupied=True)
        occupied_count = occupied_railways.count()
        total_railways_count = room.railways_set.all().count()
        room_data.append({
            'room': room,
            'occupied_count': occupied_count,
            'total_railways_count': total_railways_count
        })
    context = {
        'room_data': room_data
    }
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        room, created = Room.objects.get_or_create(number=room_number)
        if created:
            room.save()
        return redirect('choose_railway', room_id=room.id)
    return render(request, 'check_room_existence.html', context)

def choose_railway(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    occupied_railways = Railways.objects.filter(room=room).values_list('key', flat=True)
    available_railways = [railway for railway in RAILWAYS_DATA if railway['key'] not in occupied_railways]

    if request.method == 'POST':
        form = RailwayChoiceForm(request.POST,
                                 choices=[(railway['key'], railway['name']) for railway in available_railways])
        if form.is_valid():
            selected_railway_key = form.cleaned_data['selected_railway']
            selected_railway = next(
                (railway for railway in available_railways if railway['key'] == selected_railway_key), None)
            if selected_railway:
                railway = Railways.objects.create(
                    name=selected_railway['name'],
                    room=room,
                    key=selected_railway['key'],
                    budget=selected_railway['budget'],
                    sostoyanie_puti=selected_railway['sostoyanie_puti'],
                    len_of_put=selected_railway['len_of_put'],
                    stat=selected_railway['stat'],
                    gryzovye_vagoni=selected_railway['gryzovye_vagoni'],
                    pass_vogoni=selected_railway['pass_vogoni'],
                    lokomotivi=selected_railway['lokomotivi'],
                    pass_poesda=selected_railway['pass_poesda'],
                    gryz_poesda=selected_railway['gryz_poesda'],
                    other_money=selected_railway['other_money'],
                    passeger_per_kilom=selected_railway['passeger_per_kilom'],
                    amount_sotrudniki=selected_railway['amount_sotrudniki'],
                    zarplata_sotrudnikov=selected_railway['zarplata_sotrudnikov'],
                    average_zarplata_region=selected_railway['average_zarplata_region'],
                    tonn_per_kilometer=selected_railway['tonn_per_kilometer'],
                    pogryzka=selected_railway['pogryzka'],
                    perevezeno_pass=selected_railway.get('perevezeno_pass', 0),
                    pass_vagoni=selected_railway['pass_vagoni'],
                    is_occupied=True
                )
                return redirect('manage_railway', railway_id=railway.id)
    else:
        form = RailwayChoiceForm(choices=[(railway['key'], railway['name']) for railway in available_railways])

    return render(request, 'choose_railway.html', {'form': form, 'room': room})

def calculate_key_indicators(railway):
    data = {
        'gryzovye_vagoni': railway.gryzovye_vagoni,
        'gryz_poesda': railway.gryz_poesda,
        'tonn_per_kilometer': railway.tonn_per_kilometer,
        'pass_poesda': railway.pass_poesda,
        'financi_po_prochim': railway.other_money,
        'sostoyanie_puti': railway.sostoyanie_puti,
        'stat': railway.stat,
        'pass_vogoni':railway.p
    }
    key_indicators = {
        'Выручка от грузов': (data['gryzovye_vagoni'] / data['gryz_poesda'] * 120 * data['tonn_per_kilometer']) * uniform(1, 1.05),
        'Себестоимость': (185 * data['gryz_poesda'] + 173 * data['pass_poesda'] * 0.25 + 3840 * data['pass_poesda'] * 0.75) * uniform(1, 1.05),
        'Финансы по прочим видам деятельности': data['financi_po_prochim'] * 1.02,
        'Дебиторка': uniform(0, 100),
        'Кредиторка': uniform(0, 100),
        'Погрузка грузов': data['gryzovye_vagoni'] + 120,
        'Расписание пассажирских поездов': (uniform(0.95, 1) + data['sostoyanie_puti'] + data['stat']) / 3,
        'Расписание пригородных поездов': (uniform(0.95, 1) + data['sostoyanie_puti'] + data['stat']) / 3,
        'Доля грузовых отправок': (uniform(0.95, 1) + data['sostoyanie_puti'] + data['stat']) / 3,
        'Средняя скорость': ((uniform(0.95, 1) + data['sostoyanie_puti'] + data['stat']) / 3) * int((50 + 35)/2),
        'Средняя производиьелььность локомотива': data['gryzovye_vagoni'] / data['gryz_poesda'] * 143 / 365,
        'Время задержки': 1 - (data['sostoyanie_puti'] + (data['gryzovye_vagoni'] / data['gryz_poesda'] * 143 / 365)) / 2,
        'Безопасность': railway.pogryzka,
    }
    return key_indicators

def get_current_move(railway):
    for move_number in range(1, 61):
        move_field = f'move_{move_number}'
        if getattr(railway, move_field) == -1:
            return move_number
    return 60

def process_next_move(railway):
    current_move = get_current_move(railway)
    move_field = f'move_{current_move}'
    setattr(railway, move_field, railway.budget)
    railway.current_move = current_move + 1 if current_move < 60 else 60
    railway.save()

import plotly.graph_objs as go
import plotly.offline as pyo
def manage_railway(request, railway_id):
    railway = get_object_or_404(Railways, id=railway_id)
    room = railway.room
    key_indicators = calculate_key_indicators(railway)

    current_move = railway.current_move if railway.current_move is not None else 0

    if request.method == 'POST':
        form = RailwayManageForm(request.POST, instance=railway)
        if form.is_valid():
            form.save()
            if 'calculate' in request.POST:
                key_indicators = calculate_key_indicators(railway)
                return render(request, 'manage_railway.html', {
                    'form': form,
                    'railway': railway,
                    'room': room,
                    'key_indicators': key_indicators,
                    'calculated': True,
                    'current_move': current_move,
                })
            elif 'next_move' in request.POST:
                if current_move <= 60:
                    setattr(railway, f'move_{current_move}', railway.budget)
                    current_move += 1
                    railway.current_move = current_move
                    railway.save()
                if current_move >= 61:
                    #railway.delete()
                    return redirect('end_game', railway_id=railway.id)
                return redirect('manage_railway', railway_id=railway.id)
            return redirect('manage_railway', railway_id=railway.id)
    else:
        form = RailwayManageForm(instance=railway)

    return render(request, 'manage_railway.html', {
        'form': form,
        'railway': railway,
        'room': room,
        'key_indicators': key_indicators,
        'calculated': False,
        'current_move': current_move,
    })

def room_railways_graph(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    railways_in_room = Railways.objects.filter(room=room)

    # Получаем railway_id из запроса, если он есть
    railway_id = request.GET.get('railway_id')
    railway = get_object_or_404(Railways, id=railway_id) if railway_id else railways_in_room.first()

    # Подготовка данных для графика
    names = [r.name for r in railways_in_room]
    budgets = [r.budget for r in railways_in_room]
    current_moves = [r.current_move for r in railways_in_room]

    # Создание столбчатой диаграммы
    bar_data = go.Bar(
        x=budgets,
        y=names,
        orientation='h',
        text=[f'Дорога: {r.name}<br>Баланс: {r.budget}<br>Ход: {r.current_move}' for r in railways_in_room],
        hoverinfo='text'
    )
    layout = go.Layout(
        title='Бюджеты железных дорог в комнате',
        xaxis_title='Бюджет',
        yaxis_title='Железная дорога'
    )
    fig = go.Figure(data=[bar_data], layout=layout)
    bar_graph_div = pyo.plot(fig, output_type='div')

    return render(request, 'room_railways_graph.html', {
        'room': room,
        'bar_graph_div': bar_graph_div,
        'railway': railway
    })


import plotly.graph_objs as go
import plotly.offline as pyo
from django.http import HttpResponse

def end_game(request, railway_id):
    railway = get_object_or_404(Railways, id=railway_id)
    room = railway.room
    # Подготовка данных для графика
    moves = list(range(1, 61))
    budgets = [getattr(railway, f'move_{i}', 0) for i in moves]

    # Создание графика
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=moves, y=budgets, mode='lines', name='Бюджет'))
    fig.update_layout(
        title='Изменение бюджета по ходам',
        xaxis_title='Ход',
        yaxis_title='Бюджет'
    )
    graph_div = pyo.plot(fig, output_type='div')

    # Удаление железной дороги из базы данных
    railway.delete()

    return render(request, 'end_game.html', {'graph_div': graph_div, 'railway': railway, 'room':room})


def railway_calculation_view(request, railway_id):
    railway = get_object_or_404(Railways, id=railway_id)

    if request.method == 'POST':
        form = RailwayCalculationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Выполнение вычислений
            virychka_ot_gryzov = (data['gryzovye_vagoni'] / data['gryz_poesda'] * 120 * data['tonn_per_kilometer']) * uniform(1, 1.05)
            sebestoimost = (185 * data['gryz_poesda'] + 173 * data['pass_poesda'] * 0.25 + 3840 * data['pass_poesda'] * 0.75) * uniform(1, 1.05)
            financi_po_prochim = data['financi_po_prochim'] * 1.02
            debitorka = uniform(0, 100)
            kreditorka = uniform(0, 100)
            pogruzka_gryzov = data['pogruzka_gryzov'] + 120 #Погрузка грузов = начальняа в таблице, а с каждым новым грузовым вагоном + 120т
            raspisanie_pass_poesdov = (uniform(0.95, 1) + data['sostoyanie_puti'] + data['stat']) / 3
            raspisanie_prigoroda = (uniform(0.95, 1) + data['sostoyanie_puti'] + data['stat']) / 3
            dolya_gryzovix_otpravok = raspisanie_pass_poesdov
            average_speed_pass = raspisanie_pass_poesdov * 50
            average_speed_gryz = raspisanie_pass_poesdov * 35
            average_proivoditelnost_loko = data['gryzovye_vagoni'] / data['gryz_poesda'] * 143 / 365
            time_zadershka = 1 - (data['sostoyanie_puti'] + data['average_proivoditelnost_loko']) / 2
            besopasnost = data['besopasnost']  # Пример значения

            # Сохранение результатов в базу данных
            result = CalculationResult(
                railway=railway,
                virychka_ot_gryzov=virychka_ot_gryzov,
                sebestoimost=sebestoimost,
                financi_po_prochim=financi_po_prochim,
                debitorka=debitorka,
                kreditorka=kreditorka,
                pogruzka_gryzov=pogruzka_gryzov,
                raspisanie_pass_poesdov=raspisanie_pass_poesdov,
                raspisanie_prigoroda=raspisanie_prigoroda,
                dolya_gryzovix_otpravok=dolya_gryzovix_otpravok,
                average_speed_pass=average_speed_pass,
                average_speed_gryz=average_speed_gryz,
                average_proivoditelnost_loko=average_proivoditelnost_loko,
                time_zadershka=time_zadershka,
                besopasnost=besopasnost,
            )
            result.save()

            results = {
                'virychka_ot_gryzov': virychka_ot_gryzov,
                'sebestoimost': sebestoimost,
                'financi_po_prochim': financi_po_prochim,
                'debitorka': debitorka,
                'kreditorka': kreditorka,
                'pogruzka_gryzov': pogruzka_gryzov,
                'raspisanie_pass_poesdov': raspisanie_pass_poesdov,
                'dolya_gryzovix_otpravok': dolya_gryzovix_otpravok,
                'average_speed_pass': average_speed_pass,
                'average_speed_gryz': average_speed_gryz,
                'average_proivoditelnost_loko': average_proivoditelnost_loko,
                'time_zadershka': time_zadershka,
                'besopasnost': besopasnost,
            }

            return render(request, 'railway_calculation.html', {'results': results, 'railway_id': railway_id})

    return redirect('manage_railway', railway_id=railway_id)



def create_room(request, room_number=None):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room_number = form.cleaned_data['number']
            room = Room.objects.create(number=room_number)
            return redirect('view_railways_by_room_number', room_id=room.id)
    else:
        form = RoomForm(initial={'number': room_number})
    return render(request, 'create_room.html', {'form': form})


def room_detail(request, room_id):
    room = Room.objects.get(pk=room_id)
    railways = Railways.objects.filter(room=room, is_occupied=True)
    occupied_count = railways.count()
    context = {
        'room': room,
        'occupied_count': occupied_count
    }
    return render(request, 'room_detail.html', context)


def view_railways_by_room_number(request, room_number):
    room = get_object_or_404(Room, number=room_number)
    railways = Railways.objects.filter(room=room)
    return render(request, 'view_railways.html', {'room': room, 'railways': railways})



def start(request):
    return render(request, 'index.html')


def rules(request):
    return render(request, 'rules.html')


def maps(request):
    return render(request, 'maps.html')
