# Curling-Masters

Adres do strony z opisem projektu: http://prac.im.pwr.edu.pl/~giniew/doku.php?id=rok2122:letni:bd:projekt

## Dokumentacja Curling-Masters
Joanna Matuszak, Joanna Wojciechowicz, Wiktoria Marzec, Tymoteusz Kempa, Krystian Walewsk

## Spis użytych technologii

- Lucid.app
- Python 3.9 z paczkami z pliku requirements.txt
- Visual Studio Code version 1.68 z ERD Editor, MySQL
- MariaDB 10.4.8
- RStudio 2021.09.0
- R 4.4.1

## Lista plików wraz z opisem ich zawartości

- main.py - skypt generujący i wypełniający bazę (w przypadku ponownego uruchamiania tabele w bazie oraz ich zawartość są nadpisywane)
- generators.py - plik zawierający pomniejsze funkcje potrzebne do wypełnienia bazy
- fill.py - plik zawierający funkcję potrzebną do wypełnienia bazy
- clear.py - plik czyszczący tabele w bazie
- requirements.txt - potrzebne pythonowe paczki
- Data
    - ADRESY.csv - plik z adresami w Warszawie
    - IMIONA\textunderscore MESKIE.csv - plik z najczęstszymi imionami męskimi
    - IMIONA\textunderscore ZENSKIE.csv - plik z najczęstszymi imionami damskimi
    - NAZWISKA\textunderscore MESKIE.csv - plik z najczęstszymi nazwiskami męskimi
    - NAZWISKA\textunderscore ZENSKIE.csv - plik z najczęstszymi nazwiskami damskimi
- DataBaseSchema

    - clear\textunderscore database.txt - plik z poleceniami do czyszczenia tabeli w bazie oraz resetowania AI kluczy
    - curlingmasters.vuerd.json - schemat bazy danych
    - curlingmasters\textunderscore create.sql - kod tworzacy bazę danych
- report.Rnw - plik generujący raport z analizą danych
- report.pdf - raport z analizą danych



\section{Kolejność i sposób uruchamiania plików, aby uzyskać gotowy projekt}

\begin{itemize}
    \item Zainstaluj Python 3.9 z paczkami z pliku requirements.txt.
    \item Uruchom plik main.py.
    \item Skompiluj plik report.Rnw (przycisk Compile PDF).
\end{itemize}

\section{Schemat projektu bazy danych}

\begin{figure}[!htb]
\centering
\includegraphics[width=15cm]{schemat.png}
\caption{Schemat bazy danych}
\label{fig:1}
\end{figure}

\section{Lista zależności funkcyjnych z wyjaśnieniem}

Lista zależności funkcyjnych dla każdej z tabel.

\begin{itemize}
    \item Staff
    \begin{itemize}
        \item klucze kandydujące: StaffID, InfoID
        \item klucz główny: StaffID
        \item zależności funkcyjne: trywialne, StaffID $\rightarrow$ pozostałe pozdbiory atrybutów relacji, InfoID $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym
    \end{itemize}
    
    \item Players
    \begin{itemize}
        \item klucze kandydujące: PlayerID, InfoID
        \item klucz główny: PlayerID
        \item zależności funkcyjne: trywialne, PlayerID $\rightarrow$ pozostałe pozdbiory atrybutów relacji, InfoID $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym
    \end{itemize}
    
    \item Info
    \begin{itemize}
        \item klucze kandydujące: InfoID
        \item klucz główny: InfoID
        \item zależności funkcyjne: trywialne, InfoID $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym, Name nie implikuje Gender, ponieważ uwzględniamy płeć OTHER, nie wymagamy, by Email lub Phone były unikatowe, ponieważ to klub dla seniorów, którzy często mają tylko telefon domowy i/lub nie mają adresu email, inne dane też moga się powtarzać, dlatego nie identyfikują jednoznacznie osoby
    \end{itemize}
    
    \item Items
    \begin{itemize}
        \item klucze kandydujące: ItemID
        \item klucz główny: ItemID
        \item zależności funkcyjne: trywialne, ItemID $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym
    \end{itemize}
    
    \item OutsideIncome
    \begin{itemize}
        \item klucze kandydujące: SponsorID
        \item klucz główny: SponsorID
        \item zależności funkcyjne: trywialne, SponsorID $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym, SponsorName nie jest kluczem kandydującym, ponieważ w przypadku drugiej umowy z tym samym sponsorem SponsorName powtórzy się
    \end{itemize}
    
    \item OtherCosts
    \begin{itemize}
        \item klucze kandydujące: OtherPaymentID
        \item klucz główny: OtherPaymentID
        \item zależności funkcyjne: trywialne, OtherPaymentID $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym
    \end{itemize}
    
    \item CashFlow
    \begin{itemize}
        \item klucze kandydujące: PaymentID
        \item klucz główny: PaymentID
        \item zależności funkcyjne: trywialne, PaymentID $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym
    \end{itemize}
    
    \item Teams
    \begin{itemize}
        \item klucze kandydujące: TeamID, TeamName
        \item klucz główny: TeamID
        \item zależności funkcyjne: trywialne, TeamID $\rightarrow$ pozostałe pozdbiory atrybutów relacji, TeamName $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym
    \end{itemize}
    
    \item Matches
    \begin{itemize}
        \item klucze kandydujące: MatchID, (TeamA, Date), (TeamB, Date)
        \item klucz główny: MatchID
        \item zależności funkcyjne: trywialne, MatchID $\rightarrow$ pozostałe pozdbiory atrybutów relacji, (TeamA, Date) $\rightarrow$ pozostałe pozdbiory atrybutów relacji, (TeamB, Date) $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny relacji jest atrybutem unikatowym, dana drużyna może grać maksymalnie jeden mecz w ciągu jednego dnia, dlatego (TeamA, Date) oraz (TeamB, Date) są kluczami kandydującymi, w sytuacjach takich jak pandemia niektóre mecze z zaległego sezonu grane są w terminie sezonu następnego, dlatego nie ma funkcyjnej zależności między Date a Season
    \end{itemize}
    
    \item PlayerMatchPerformance
    \begin{itemize}
        \item klucze kandydujące: (PlayerID, MatchID)
        \item klucz główny: (PlayerID, MatchID)
        \item zależności funkcyjne: trywialne, (PlayerID, MatchID) $\rightarrow$ pozostałe pozdbiory atrybutów relacji
        \item komenatrz: klucz główny jest kluczem kompozytowym, ponieważ podczas jednego meczu gra wielu graczy, a jeden gracz gra w wielu meczach
    \end{itemize}
    
\end{itemize}

\section{Uzasadnienie, że baza jest w EKNF}

Jak wykazaliśmy w poprzednim podpunkcie, każda nietrywialna zależność funkcyjna albo zaczyna się od nadklucza albo kończy się atrybutem elementarnym. Oznacza to, że baza jest w EKNF.


\section{Trudności podczas projektu}

\begin{itemize}
    \item Uzasadnienie, że baza jest w EKNF - musieliśmy zmieniać projekt bazy, by spełniała wszystkie wymagania.
    \item Pogodzenie normalizacji z wydajnościa/dobrymi zwyczajami przy projektowaniu bazy danych.
    \item Wygenerowanie możliwości odchodzenia pracowników w bazie danych.
    \item Stworzenie tabeli Info oraz CashFlow.
\end{itemize}

\section{Źródła danych}
\begin{itemize}
    \item \href{https://dane.gov.pl/pl/dataset/1667,lista-imion-wystepujacych-w-rejestrze-pesel-osoby-zyjace}{Zestawienie imion żeńskich i męskich występujących w rejestrze PESEL wraz z liczbą wystąpień}
    \item \href{https://dane.gov.pl/pl/dataset/1681,nazwiska-osob-zyjacych-wystepujace-w-rejestrze-pesel}{Zestawienie nazwisk żeńskich i męskich występujących w rejestrze PESEL wraz z liczbą wystąpień}
    \item \href{https://dane.gov.pl/pl/dataset/469,adresy-mst-warszawy?fbclid=IwAR2ChB2om1VFiwfd5kP8hQlfULNx-anTzDOqjL3b5ypQjpqKd2r61xxNDHE}{Adresy m.st. Warszawy}
\end{itemize}

\end{document}

