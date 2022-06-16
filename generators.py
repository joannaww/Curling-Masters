import pandas as pd
import random
from datetime import date
import numpy as np

import mysql.connector as mysql
import datetime as dt
import matplotlib.pyplot as plt
from pandasql import sqldf
from dateutil.relativedelta import relativedelta
import itertools as it
from scipy.stats import beta

def match_schedule(list_of_teams):
    
    l1 = list(it.combinations(list_of_teams, 2))
    l2 = [list(i) for i in l1]
    l2[2].reverse()
    l2[3].reverse()
    l2[6].reverse()
    random.shuffle(l2) # pierwsza połowa ligi
    
    l3 = [list(reversed(i)) for i in l2] # druga połowa ligi
    
    return l2 + l3


def generate_name(file):
    """
    Funkcja zwraca wylosowane imię ze 100 najbardziej znanych w Polsce imion. 
    """
    
    df = pd.read_csv(file)[1:100]
    n = df["IMIĘ_PIERWSZE"].sample(1)
    
    return n.to_string(index=False)


def generate_surname(file):
    """
    Funkcja zwraca wylosowane nazwisko ze 100 najbardziej znanych w Polsce nazwisk. 
    """
    
    df = pd.read_csv(file)[1:500]
    n = df["Nazwisko aktualne"].sample(1)
    
    return n.to_string(index=False)


def str_time_prop(start, end, prop):
    """
    Zwraca datę pomiędzy dwiema ustalonymi (w odstępie takim jak argument (0,1))
    """

    prime = start + prop * (end - start)

    return prime


def random_date(start, end):
    """
    Losuje odstęp i wywołuje funkcje zwracającą date
    
    W ogólności funkcja za pomocą funkcji str_time_prop zwraca losową datę pomiędzy dwiema zadanymi 
    w argumentach danymi. Będzie do losowania JoinDate
    """
    
    prop=random.random()
    d = str_time_prop(start, end, prop)
    
    return d


def generate_email(name, surname):
    
    """
    Funkcja zwraca email osoby 
    """
    
    number = int(random.random()*10000)
    mail = name.lower() + '.' + surname.lower() + str(number) + '@giniewicz.it.com'
    
    return mail


def generate_phone():
    
    """
    Funkcja zwraca numer osoby 
    """
    
    phone = random.randint(500000000, 900000000)
    return phone


def generate_address(file): 
    
    df = pd.read_csv(file)
    row = df.sample(1)
    
    city = row["MIEJCOWOSC"].to_string(index=False)
    street = row["NAZWA_ULICY"].to_string(index=False)
    number = row["NUMER"].to_string(index=False)
    
    address = street + " " + number + " " + city
    
    return address


def generate_gender():

    x = random.random()
    
    if 0 < x < 0.01:
        return "OTHER"
    elif 0.01 < x < 0.522:
        return "FEMALE"
    else:
        return "MALE"


def generate_depart_date(company_start, current_date):
    
    """
    Funkcja zwraca datę odejścia pracownika lub gracza,
    musimy ustalić z jakimś prawdopodobieństwem ludzie odchodzą
    """
    
    x = random.random()
    
    if 0 < x < 0.1:
        date = random_date(company_start, current_date)
    else:
        date = dt.date(9999,1,1)
    
    
    return date


def generate_income(min_income, max_income):
    
    """
    Funckcja zwraca losowe dochody danego pracownika.
    """
    
    income = random.randint(min_income ,max_income)
    
    return income


def num_of_spectators(data, middle_of_season, _min = 0, _max = 200):
    
    """
    Funkcja zwraca liczbę osób na widowni w czasie meczu
    """
    
    delta = abs((middle_of_season - data).days) / 70 # różnica czasowa między środkiem sezonu, a naszym meczem /70, bo to polowa sezonu
    
    x = beta(2+3*delta, 5-3*delta).rvs()
    
    return round(x*200)  


def score():
    
    score_a = round(beta(5,9).rvs()*20)
    score_b = round(beta(5,9).rvs()*20)
    
    if score_a == score_b:
        if np.random.binomial(1,0.5):
            score_a += 1
        else:
            score_b += 1
            
    return score_a, score_b


def effectiveness_in_match(score):
    
    e = round(beta(score + 1,3).rvs(),2)
    
    return float(e)


