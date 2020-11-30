import pandas as pd
import datetime
import matplotlib.pyplot as plt


def days(df, alder_ved_start):
    t_0 = datetime.datetime.strptime(df['date'][0], '%Y-%m-%d')
    days = []
    for index in df.index:
        t = datetime.datetime.strptime(df['date'][index], '%Y-%m-%d')
        dt = t - t_0
        days.append(dt.days + alder_ved_start)
    return days


def days_at_first_measurement(df, birth_date):
    date_of_first_measurement = datetime.datetime.strptime(df['date'][0], '%Y-%m-%d')
    dt = date_of_first_measurement - datetime.datetime.strptime(birth_date, '%Y-%m-%d')
    return dt.days

nuka_df = pd.read_csv('data/nuka.csv')
malo_df = pd.read_csv('data/malo.csv')
elsa_df = pd.read_csv('data/elsa.csv')

nuka_df['days'] = days(nuka_df, days_at_first_measurement(nuka_df, '2020-06-24'))
malo_df['days'] = days(malo_df, days_at_first_measurement(malo_df, '2020-06-24'))
elsa_df['days'] = days(elsa_df, days_at_first_measurement(elsa_df, '2019-10-11'))

fig, ax = plt.subplots()
nuka_df.plot(x='days', y='vekt', ax=ax, label='Nuka')
malo_df.plot(x='days', y='vekt', ax=ax, label='Malo')
elsa_df.plot(x='days', y='vekt', ax=ax, label='Elsa')

plt.show()