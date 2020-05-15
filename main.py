from datetime import datetime, timedelta
from operator import itemgetter
import math


records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):
    sortedList = sorted(records, key=itemgetter('source'))
    bills = []

    for call in sortedList:
        newEndtime = datetime.fromtimestamp(call['end'])
        newStartTime = datetime.fromtimestamp(call['start'])
        subs = newEndtime - newStartTime
        subsMins = math.trunc(subs / timedelta(minutes=1))
        # Agradecimentos a Ennio Aoki pela ideia do trunc!
        # Agradecimentos também a Fernando Aragão, Carlos Augusto Moreno
        # Ribeiro e Leonardo Fernandes por me ajudarem a iterar sobre ints
        # ao invés de strs

        if newStartTime.hour < 22 and newStartTime.hour >= 6:
            taxRounded = round(0.36 + (0.09*subsMins), 2)

        else:
            taxRounded = 0.36

        newSource = call['source']
        bills.append({'source': f'{newSource}', 'total': taxRounded})

    beg = []
    end = []
    i = 0
    while (i < len(bills)-1):
        beg.append(i)
        source = bills[i]['source']
        for j in range(i+1, len(bills)):
            if not (source == bills[j]['source']):
                end.append(j)
                i = j
                break
            elif (j == len(bills)-1):
                end.append(j+1)
                i = j

    result = []
    for i in range(0, len(beg)):
        nome = bills[beg[i]]['source']
        total = 0
        for j in range(beg[i], end[i]):
            total = round(total + float(bills[j]['total']), 2)
        result.append({'source': f'{nome}', 'total': total})

    result.sort(key=lambda k: k['total'], reverse=True)
    return result


classify_by_phone_number(records)
