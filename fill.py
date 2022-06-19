import pandas as pd
import random
import time
from datetime import date
import numpy as np
import mysql.connector as mysql
import datetime as dt
from pandasql import sqldf
from dateutil.relativedelta import relativedelta
import itertools as it
from scipy.stats import beta

from generators import *


def fill(cursor):

    """
    Funkcja wypełnia tabele w bazie danych.
    """
    
    staff_depart_dates = []
    staff_depart_id = []
    c = 0 
    def info_fill_staff():

        """
        Funkcja wypełnia tabelę Info dla pracowników.
        """


        info = []
        for i in range(1, 16):

            gender = generate_gender()
            if gender == "FEMALE":
                file1 = "Data/IMIONA_ZENSKIE.csv"
                file1 = "Data/IMIONA_ZENSKIE.csv"
                file2 = "Data/NAZWISKA_ZENSKIE.csv"
            elif gender == "MALE":
                file1 = "Data/IMIONA_MESKIE.csv"
                file2 = "Data/NAZWISKA_MESKIE.csv"
            else:
                x = random.random()
                if 0 < x < 0.5:
                    file1 = "Data/IMIONA_ZENSKIE.csv"
                    file2 = "Data/NAZWISKA_ZENSKIE.csv"
                else:
                    file1 = "Data/IMIONA_MESKIE.csv"
                    file2 = "Data/NAZWISKA_MESKIE.csv"


            first_name = generate_name(file1)
            last_name = generate_surname(file2)
            address = generate_address("Data/ADRESY.csv")
            join_date = dt.date(2020, 9, 1)
            depart_date = generate_depart_date(dt.date(2020, 10, 1), dt.date.today())

            if depart_date != dt.date(9999, 1, 1):
                staff_depart_dates.append((i, depart_date))

            birth_date = random_date(dt.date(1958, 1, 1), dt.date(2002, 1, 1))
            email = generate_email(first_name, last_name)
            phone = generate_phone()

            info.append((i, first_name, last_name, address, join_date, depart_date, birth_date, email, phone, gender))

        
            
        
        for i in range(1, len(staff_depart_dates)+1):
            
            gender = generate_gender()
            if gender == "FEMALE":
                file1 = "Data/IMIONA_ZENSKIE.csv"
                file2 = "Data/NAZWISKA_ZENSKIE.csv"
            elif gender == "MALE":
                file1 = "Data/IMIONA_MESKIE.csv"
                file2 = "Data/NAZWISKA_MESKIE.csv"
            else:
                x = random.random()
                if 0 < x < 0.5:
                    file1 = "Data/IMIONA_ZENSKIE.csv"
                    file2 = "Data/NAZWISKA_ZENSKIE.csv"
                else:
                    file1 = "Data/IMIONA_MESKIE.csv"
                    file2 = "Data/NAZWISKA_MESKIE.csv"


            first_name = generate_name(file1)
            last_name = generate_surname(file2)
            address = generate_address("Data/ADRESY.csv")
            birth_date = random_date(dt.date(1958, 1, 1), dt.date.today())
            email = generate_email(first_name, last_name)
            phone = generate_phone()
            join_date = staff_depart_dates[i-1][1]
            depart_date = dt.date(9999, 1, 1)

            info.append((i+15, first_name, last_name, address, join_date, depart_date, birth_date, email, phone, gender))
            
            
        qr = ('INSERT INTO team9.Info ' 
              '(InfoID, FirstName, LastName, Address, JoinDate, DepartDate, BirthDate, Email, Phone, Gender) ' 
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
        cursor.executemany(qr, info)
        
        global num_of_staff
        num_of_staff = len(staff_depart_dates) + 15
            
        for i in staff_depart_dates:
            staff_depart_id.append(i[0])
            
    def info_fill_players():

        """
        Funkcja wypełnia tabelę Info dla graczy.
        """
        
        info = []
        for i in range(25):
            
            gender = "FEMALE"
            file1 = "Data/IMIONA_ZENSKIE.csv"
            file2 = "Data/NAZWISKA_ZENSKIE.csv"
            first_name = generate_name(file1)
            last_name = generate_surname(file2)
            address = generate_address("Data/ADRESY.csv")
            join_date = dt.date(2020, 10, 1) # miesiąc po otwarciu firmy
            depart_date = dt.date(9999, 1, 1) 
            birth_date = random_date(dt.date(1954, 1, 1), dt.date(1962, 1, 1)) 
            email = generate_email(first_name, last_name)
            phone = generate_phone()
            
            info.append((first_name, last_name, address, join_date, depart_date, birth_date, email, phone, gender))
            
        for i in range(25):
            
            gender = "FEMALE"
            file1 = "Data/IMIONA_ZENSKIE.csv"
            file2 = "Data/NAZWISKA_ZENSKIE.csv"
            first_name = generate_name(file1)
            last_name = generate_surname(file2)
            address = generate_address("Data/ADRESY.csv")
            join_date = dt.date(2020, 10, 1) # miesiąc po otwarciu firmy
            depart_date = dt.date(9999, 1, 1) 
            birth_date = random_date(dt.date(1932, 1, 1), dt.date(1949, 1, 1))
            email = generate_email(first_name, last_name)
            phone = generate_phone()
            
            info.append((first_name, last_name, address, join_date, depart_date, birth_date, email, phone, gender))
            
        for i in range(25):
            
            gender = "MALE"
            file1 = "Data/IMIONA_MESKIE.csv"
            file2 = "Data/NAZWISKA_MESKIE.csv"
            first_name = generate_name(file1)
            last_name = generate_surname(file2)
            address = generate_address("Data/ADRESY.csv")
            join_date = dt.date(2020, 10, 1) # miesiąc po otwarciu firmy
            depart_date = dt.date(9999, 1, 1) 
            birth_date = random_date(dt.date(1954, 1, 1), dt.date(1962, 1, 1)) 
            email = generate_email(first_name, last_name)
            phone = generate_phone()
            
            info.append((first_name, last_name, address, join_date, depart_date, birth_date, email, phone, gender))
            
        for i in range(25):
            
            gender = "MALE"
            file1 = "Data/IMIONA_MESKIE.csv"
            file2 = "Data/NAZWISKA_MESKIE.csv"
            first_name = generate_name(file1)
            last_name = generate_surname(file2)
            address = generate_address("Data/ADRESY.csv")
            join_date = dt.date(2020, 10, 1) # miesiąc po otwarciu firmy
            depart_date = dt.date(9999, 1, 1) 
            birth_date = random_date(dt.date(1932, 1, 1), dt.date(1949, 1, 1)) 
            email = generate_email(first_name, last_name)
            phone = generate_phone()
            
            info.append((first_name, last_name, address, join_date, depart_date, birth_date, email, phone, gender))

        qr = ('INSERT INTO team9.Info ' 
              '(FirstName, LastName, Address, JoinDate, DepartDate, BirthDate, Email, Phone, Gender) ' 
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)')
        cursor.executemany(qr, info)
                 
            
    def staff_fill():

        """
        Funkcja wypełnia tabelę Staff.
        """
        
        positions = {1:"CHAIRMAN", 2:"VICE CHAIRMAN", 3:"ACCOUNTANT", 4:"CARETAKER", 13:"PHYSIOTHERAPIST", 14:"ICETAKER",
                    15:"HANDYMAN"}
        positions.update(dict.fromkeys([5, 6, 7, 8, 9, 10, 11, 12], "COACH"))

        staff = []
        for i in range(1,16):
            
            if i in staff_depart_id:
                active = False
            else:
                active = True

            staff.append((i, positions[i], i, active)) 
            
        for i in range(1, len(staff_depart_dates)+1):
            
            active = True
            
            staff.append((i+15, positions[staff_depart_dates[i-1][0]], i+15, active)) 
            

        qr = ('INSERT INTO team9.Staff ' 
              '(StaffID, Position, InfoID, Active) ' 
              'VALUES (%s, %s, %s, %s)')
        cursor.executemany(qr, staff)
            
    def cash_flow_salaries():

        """
        Funkcja zwraca listę informacji o wypłatach dla pracowników.
        """
        
        salaries = {"CHAIRMAN":15000.0, "VICE CHAIRMAN":10000.0, "ICETAKER":4000.0}
        salaries.update(dict.fromkeys(["ACCOUNTANT","CARETAKER"], 3100.0))
        salaries.update(dict.fromkeys(["PHYSIOTHERAPIST", "HANDYMAN"], 3500.0))
        salaries.update(dict.fromkeys(["COACH"], 4000.0))
        
        qr = """SELECT COUNT(*) FROM team9.Staff"""
        cursor.execute(qr)
        k = cursor.fetchone()[0]
        
        
        salaries_list = []    
        for i in range(1,k+1):
            
            qr = ('SELECT JoinDate, DepartDate FROM team9.Info WHERE InfoID = %s ')
            cursor.execute(qr, [i])
            join_date, depart_date = cursor.fetchone()
            
            qr = ('SELECT Position FROM team9.Staff WHERE StaffID = %s ')
            cursor.execute(qr, [i])
            position = cursor.fetchone()[0]
            
            flag = 0 
            time_change = relativedelta(months = 1)
            month_later = join_date + time_change
            date = dt.date(month_later.year, month_later.month, 10) # pierwsza wypłata
            salary = salaries[position]
            while flag == 0:
                
                salaries_list.append((date, -salary, None, i, None, None, None)) # pierwsza wypłata normalna
                
                if np.random.binomial(1,0.05):
                    salary += 100 # premia
                elif np.random.binomial(1,0.02) and salary >= 3110: # minimalna krajowa
                    salary -= 100 # kara
                
            
                if date >= depart_date:
                    flag += 1
                date += time_change
                if date >= dt.date.today():
                    flag += 1
                    
        return salaries_list
                    
    def teams_fill():

        """
        Funkcja wypełnia tabelę Teams.
        """
        
        team_names = ["ŻABKI", "PSZCZÓŁKI", "KANGURY", "SŁONIKI", "ŁOSOSIE", "TYGRYSY", "PANTERY", "WILKI", 
                     "SZCZUPAKI", "KUNY", "MOTYLKI", "DELFINY", "KOZY", "IGUANY", "SARENKI", "KRÓWKI",
                     "KURY", "OWIECZKI", "RYSIE", "ZEBRY"]
        
        teams = []
        for i in range(5):
            
            team_name = team_names.pop(random.randint(0,len(team_names)-1))
            _type = "FEMALE"
            age_category = "JUNIORS"
            
            teams.append((team_name, _type, age_category))
            
        for i in range(5):
            
            team_name = team_names.pop(random.randint(0,len(team_names)-1))
            _type = "FEMALE"
            age_category = "SENIORS"
            
            teams.append((team_name, _type, age_category))
            
        for i in range(5):
            
            team_name = team_names.pop(random.randint(0,len(team_names)-1))
            _type = "MALE"
            age_category = "JUNIORS"
            
            teams.append((team_name, _type, age_category))
            
        for i in range(5):
            
            team_name = team_names.pop(random.randint(0,len(team_names)-1))
            _type = "MALE"
            age_category = "SENIORS"
            
            teams.append((team_name, _type, age_category))

        qr = ('INSERT INTO team9.Teams ' 
              '(TeamName, Type, AgeCategory) ' 
              'VALUES (%s, %s, %s)')
        cursor.executemany(qr, teams)
            
    def players_fill():

        """
        Funkcja wypełnia tabelę Players.
        """
        
        team_id = 1 
        players_list = []
        info_id = num_of_staff
        for i in range(1, 101):
                
            active = True
            info_id += 1
            
            players_list.append((team_id, active, info_id))
            
            if i%5 == 0:
                team_id += 1
                
        qr = ('INSERT INTO team9.Players ' 
                      '(TeamID, Active, InfoID) ' 
                      'VALUES (%s, %s, %s)')
                
        cursor.executemany(qr, players_list)
        
    def cash_flow_player_tuition():

        """
        Funkcja zwraca listę informacji o składkach od graczy.
        """
        
        qr = """SELECT COUNT(*) FROM team9.Players"""
        cursor.execute(qr)
        k = cursor.fetchone()[0] # liczba graczy
        
        
        tuition_list = []    
        for i in range(1,k+1):
            
            qr = ('SELECT JoinDate, DepartDate FROM team9.Info WHERE InfoID = %s ')
            cursor.execute(qr, [i + num_of_staff])
            join_date, depart_date = cursor.fetchone()
            
            flag = 0 
            time_change = relativedelta(months = 1)
            date = dt.date(join_date.year, join_date.month, 10) 
            amount = 50
            while flag == 0:
                
                tuition_list.append((date, amount, i, None, None, None, None)) # pierwsza wypłata normalna
                
                if date >= depart_date:
                    flag += 1
                date += time_change
                if date >= dt.date.today():
                    flag += 1
                    
        return tuition_list
        
        
    def matches_fill():

        """
        Funkcja wypełnia tabelę Matches.
        """
        
        # 3 sezony, bo 2 w tył i 1 w przód
        seasons = {0:"2020/2021", 1:"2021/2022", 2:"2022/2023"}
        
        matches = []
        for n in range(3): # mamy 3 sezony 
            
            # plan meczy 
            female_juniors = match_schedule([1,2,3,4,5])
            female_seniors = match_schedule([6,7,8,9,10])
            male_juniors = match_schedule([11,12,13,14,15])
            male_seniors = match_schedule([16,17,18,19,20])
            
            season_start = dt.datetime(2020 + n, 11, 7 - n, 12, 0)
            season_end = dt.datetime(2021 + n, 3, 21 - n, 16, 0)
            middle = season_start + (season_end - season_start) / 2
            
            date = season_start
            
            schedules = {1:female_juniors, 2:female_seniors, 3:male_juniors, 0:male_seniors}
            
            k = 0
            for i in range(1, 81):
            
                
                if n != 2: # tylko dla przeszłych meczy
                    spectators = num_of_spectators(date, middle)
                    score_a, score_b = score()
                else:
                    spectators = None
                    score_a, score_b = None, None
                    
                season = seasons[n]
                team_a, team_b = schedules[i%4][k]
                
                matches.append((spectators, season, date, score_a, score_b, team_a, team_b))
                
                if i%4 == 0:
                    date += dt.timedelta(hours = 140)
                elif i%2 == 0:
                    date += dt.timedelta(hours = 20)
                else:
                    date += dt.timedelta(hours = 4)
                    
                if i%4 == 0:
                    k += 1
                
        qr = ('INSERT INTO team9.Matches ' 
                  '(Spectators, Season, Date, ScoreA, ScoreB, TeamA, TeamB) ' 
                  'VALUES (%s, %s, %s, %s, %s, %s, %s)')
        
        cursor.executemany(qr, matches)
        
    def player_match_performance_fill():

        """
        Funkcja wypełnia tabelę PlayerMatchPerformance.
        """
        
        positions_team_a = ["LEAD", "SECOND", "THIRD", "FOURTH", "SUBSTITUTE"]
        positions_team_b = ["LEAD", "SECOND", "THIRD", "FOURTH", "SUBSTITUTE"]

        match_performance = []
        
        qr = """SELECT ScoreA, ScoreB, TeamA, TeamB FROM team9.Matches"""
        cursor.execute(qr)
        match_info = cursor.fetchall()
        
        for i in range(1, 161):
            
                score_a, score_b, team_a, team_b = match_info[i - 1]
                
                random.shuffle(positions_team_a) # tasujemy 
                random.shuffle(positions_team_b) # tasujemy 
                
                for j in range(1, 6):
                    
                    player_id_a = int(team_a * 5 - 5 + j)
                    player_id_b = int(team_b * 5 - 5 + j)
                    
                    position_a = positions_team_a[j-1]
                    position_b = positions_team_b[j-1]
                    
                    if position_a == "SUBSTITUTE":
                        effectiveness_a = None
                    else:
                        effectiveness_a = effectiveness_in_match(score_a)
                        
                    if position_b == "SUBSTITUTE":
                        effectiveness_b = None
                    else:
                        effectiveness_b = effectiveness_in_match(score_b)
                        
                    match_performance.append((effectiveness_a, position_a, player_id_a, i))
                    match_performance.append((effectiveness_b, position_b, player_id_b, i))
                    
        qr = ('INSERT INTO team9.PlayerMatchPerformance ' 
              '(Effectiveness, Position, PlayerID, MatchID) ' 
              'VALUES (%s, %s, %s, %s)')

        cursor.executemany(qr, match_performance)
        
        
    def items_fill():

        """
        Funkcja wypełnia tabelę Items.
        """
        
        qr = """SELECT TeamName FROM team9.Teams"""
        cursor.execute(qr)
        team_names = cursor.fetchall()
        
        items = []
        for i in range(len(team_names)):
            
            if i < 10:
                size = "UNIVERSAL FEMALE"
            else:
                size = "UNIVERSAL MALE"
                
            description = team_names[i][0] + " - TEAM UNIFORM"
            price = 359
            quantity = 5
            items.append((size, description, price, quantity)) 
            
        # buty
        shoes_sizes = {37:2}
        shoes_sizes.update(dict.fromkeys([35, 36, 43, 44, 45], 1))
        shoes_sizes.update(dict.fromkeys([38, 39, 40, 41, 42], 3))
        
        for i in range(35, 46):
            
            size = str(i)
            description = "CURLING SHOES"
            price = 359 
            quantity = shoes_sizes[i]
            items.append((size, description, price, quantity)) 
            
        # szczotki
            
        size = "UNIVERSAL"
        description = "BROOM"
        price = 259
        quantity = 30
        items.append((size, description, price, quantity)) 
        
        # kamienie
        
        size = "UNIVERSAL"
        description = "MATCH STONE"
        price = 2137 # papieżowa
        quantity = 16 
        items.append((size, description, price, quantity)) 
        
        description = "TRAINING STONE"
        price = 1069
        quantity = 32
        items.append((size, description, price, quantity)) 
        
        qr = ('INSERT INTO team9.Items ' 
              '(Size, Description, Price, Quantity) ' 
              'VALUES (%s, %s, %s, %s)')

        cursor.executemany(qr, items)
        
    def cash_flow_items():

        """
        Funkcja zwraca listę informacji o wydatkach na przedmioty.
        """
        
        qr = """SELECT ItemID, Quantity, Price FROM team9.Items"""
        cursor.execute(qr)
        items_info = cursor.fetchall()
        
        items_list = []
        for i in range(len(items_info)):
            
            item_id = items_info[i][0]
            date = dt.date(2020, 9, 1)
            amount = items_info[i][1] * items_info[i][2]
            
            items_list.append((date, -amount, None, None, item_id, None, None))
            
        return items_list
    
    def outside_income_fill():

        """
        Funkcja wypełnia tabelę OutsideIncome.
        """
        
        outside_income = [("EUROPEAN UNION", 1000000.0, dt.date(2020, 9, 1), dt.date(2020, 9, 2)), 
                         ("CITY COUNCIL", 10000.0, dt.date(2020, 9, 1), dt.date(9999, 1, 1)),
                         ("TARCZYŃSKI", 20000.0, dt.date(2020, 9, 1), dt.date(9999, 1, 1)),
                         ("VOLTAREN", 20000.0, dt.date(2020, 11, 1), dt.date(2021, 3, 1)),
                         ("ZAKŁAD POGRZEBOWY AS BYTOM", 10000.0, dt.date(2021,1, 1), dt.date(2021, 12, 1)),
                         ("STOPERAN", 15000.0, dt.date(2021,11, 1), dt.date(2022, 3, 1)),
                         ("BIEDRONKA", 19000.0, dt.date(2022,1, 1), dt.date(2022, 12, 1)),]
        
        
        qr = ('INSERT INTO team9.OutsideIncome ' 
              '(SponsorName, Amount, StartDate, EndDate) ' 
              'VALUES (%s, %s, %s, %s)')

        cursor.executemany(qr, outside_income)
        
        
    def cash_flow_outside_income():

        """
        Funkcja zwraca listę informacji o przychodach zewnętrznych.
        """
        
        qr = """SELECT SponsorID, Amount, StartDate, EndDate from team9.OutsideIncome"""
        cursor.execute(qr)
        outside_income_info = cursor.fetchall()
        
        outside_income = []
        for i in range(len(outside_income_info)):
            
            sponsor_id = outside_income_info[i][0]
            amount = outside_income_info[i][1]
            start_date = outside_income_info[i][2]
            end_date = outside_income_info[i][3]
            
            time_change = relativedelta(months = 1)
            date = start_date
            while date < end_date and date < dt.date.today():
                
                outside_income.append((date, amount, None, None, None, sponsor_id, None))
                
                date += time_change
            
        return outside_income
    
    def other_costs_fill():

        """
        Funkcja wypełnia tabelę OtherCosts.
        """
        
        descriptions_not_funny = ["MAINTENANCE OF THE ICE RINK", "BILLS", 
                                 "FOOD", "ADVERTISEMENT", "UPKEEP OF THE EQUIPMENT"]
        descriptions_funny = ["REFREEZING THE ICE", "SANITARY INSPECTION FEE", "THEFT", "CLEANING THE GRAFFITI",
                            "MAFIA EXTORTION", "BAIL FOR CHAIRMAN'S NEPHEW", "BRIBE FOR THE CITY COUNCIL", 
                             "WEDDING OF TWO VERY CUTE OLD PEOPLE", "FEEDING PLUFFY"]
        
        other_costs = [("CLUB'S BIRTHDAY", True)]
        for i in range(len(descriptions_not_funny)):
            
            description = descriptions_not_funny[i]
            periodic = True
            other_costs.append((description, periodic))
            
        for i in range(len(descriptions_funny)):
            
            description = descriptions_funny[i]
            periodic = False
            other_costs.append((description, periodic))
            
        qr = ('INSERT INTO team9.OtherCosts ' 
              '(Description, Periodic) ' 
              'VALUES (%s, %s)')

        cursor.executemany(qr, other_costs)
        
    def cash_flow_other_costs():
        
        qr1 = """SELECT OtherPaymentID FROM team9.OtherCosts WHERE Periodic = TRUE"""
        cursor.execute(qr1)
        other_costs_periodic = cursor.fetchall()
        
        qr2 = """SELECT OtherPaymentID FROM team9.OtherCosts WHERE Periodic = FALSE"""
        cursor.execute(qr2)
        other_costs_non_periodic = cursor.fetchall()
        
        other_costs = [(dt.date(2021, 9, 1), -10000.0, None, None, None, None, 1)]
        
        for i in range(1, len(other_costs_periodic)):
            
            date = dt.date(2020, 10, 10)
            time_change = relativedelta(months = 1)
            other_cost_id = other_costs_periodic[i][0]
            
            while date < dt.date.today():
                
                amount = float(random.randint(1000, 3000))
                if date.month in [5, 6, 7, 8, 9, 10]:
                    
                    amount = amount / 2 # poza sezonem
                    
                other_costs.append((date, -amount, None, None, None, None, other_cost_id))
                
                date += time_change
                
        for i in range(len(other_costs_non_periodic)):
            
            date = random_date(dt.date(2020, 9, 1), dt.date.today())
            amount = random.randint(200, 8000)
            other_cost_id = other_costs_non_periodic[i][0]
            
            other_costs.append((date, amount, None, None, None, None, other_cost_id))
                
        return other_costs
            
            
    def cash_flow_fill():

        """
        Funkcja wypełnia tabelę CashFlow.
        """
        
        salaries = cash_flow_salaries()
        tuitions = cash_flow_player_tuition()
        items = cash_flow_items()
        outside_income = cash_flow_outside_income()
        other_costs = cash_flow_other_costs()
        
        cash_flows = salaries + tuitions + items + outside_income + other_costs
        
        cash_flows.sort()
        
        qr = ('INSERT INTO team9.CashFlow ' 
              '(Date, Amount, PlayerID, StaffID, ItemID, SponsorID, OtherPaymentID) ' 
              'VALUES (%s, %s, %s, %s, %s, %s, %s)')

        cursor.executemany(qr, cash_flows)

    # wywołujemy każdą z funkcji po kolei
    info_fill_staff()
    staff_fill()
    info_fill_players()
    teams_fill()
    players_fill()
    matches_fill()
    player_match_performance_fill()
    items_fill()
    outside_income_fill()
    other_costs_fill()
    cash_flow_fill()