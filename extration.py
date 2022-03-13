import numpy
import pandas as pd
import datetime


def extractUsCovid():
    df = pd.read_csv("./Raw/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv", encoding="utf-8")
    keep = ['submission_date', 'state', 'tot_cases', 'new_case', 'tot_death', 'new_death']
    df = df[keep]
    # format datetime
    df = df.rename(columns={"submission_date": "date"}, errors="raise")
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by="date")
    df = df.reset_index(drop=True)
    df.to_csv("./Extraction data/US_Covid_stateLevel.csv", index=False)


def extractVaccination():
    df = pd.read_csv("./Raw/us_state_vaccinations.csv", encoding="utf-8")
    print(df.columns)
    keep = ['date', 'location', 'total_vaccinations', 'total_distributed',
            'people_vaccinated', 'people_fully_vaccinated',
            'daily_vaccinations', 'total_boosters']
    df = df[keep]
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by="date")
    df = df.reset_index(drop=True)
    df.to_csv("./Extraction data/USVaccination.csv", index=False)


extractUsCovid()
extractVaccination()
