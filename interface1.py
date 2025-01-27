import requests
import pandas as pd
import streamlit as st

st.title("""🏀🏀🏀  BASKET TALENT INSPECTOR 🏀🏀🏀 """)

url = 'https://nba-test-draft-public-xam5swm3da-ew.a.run.app/predict'



uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:

    input_data = pd.read_csv(uploaded_file)

    st.write("Uploaded CSV Data:")
    st.dataframe(input_data)
    predictions = []

    for index, row in input_data.iterrows():
        params = {
            'Name': row['Name'],
            'GP': row['GP'],
            'MIN': row['MIN'],
            'PTS': row['PTS'],
            'FGM': row['FGM'],
            'FGA': row['FGA'],
            'FG_': row['FG%'],
            '_3P_Made': row['3P Made'],
            '_3PA': row['3PA'],
            '_3P_': row['3P%'],
            'FTM': row['FTM'],
            'FTA': row['FTA'],
            'FT_': row['FT%'],
            'OREB': row['OREB'],
            'DREB': row['DREB'],
            'REB': row['REB'],
            'AST': row['AST'],
            'STL': row['STL'],
            'BLK': row['BLK'],
            'TOV': row['TOV']
            }

    if st.button('Tu veux vérifier son potentiel ⭐⭐⭐?'):

        response = requests.get(url, params=params)
        pred = f"{response.json()['forecast']}"
        st.markdown(pred)
        if pred =="1.0":
            st.balloons()
            st.markdown("C'est la pépite que vous cherchiez !!!")
            st.image("lebron.webp")
        else:
            st.markdown("Peut-être pas la meilleur idée pour le moment ...")
            st.image("red-stop-sign-3d-illustration-free-png.webp")


st.title("Remplir les données à la main:")

Name = st.text_input('Player Name', value='Player 1')
GP = st.number_input('Games Played (GP)', value=0.0)
MIN = st.number_input('Minutes Played (MIN)', value=0.0)
PTS = st.number_input('Points Scored (PTS)', value=0.0)
FGM = st.number_input('Field Goals Made (FGM)', value=0.0)
FGA = st.number_input('Field Goals Attempted (FGA)', value=0.0)
FG_ = st.number_input('Field Goal Percentage (FG%)', value=0.0)
_3P_Made = st.number_input('3-Pointers Made (_3P_Made)', value=0.0)
_3PA = st.number_input('3-Pointers Attempted (_3PA)', value=0.0)
_3P_ = st.number_input('3-Point Percentage (_3P_)', value=0.0)
FTM = st.number_input('Free Throws Made (FTM)', value=0.0)
FTA = st.number_input('Free Throws Attempted (FTA)', value=0.0)
FT_ = st.number_input('Free Throw Percentage (FT%)', value=0.0)
OREB = st.number_input('Offensive Rebounds (OREB)', value=0.0)
DREB = st.number_input('Defensive Rebounds (DREB)', value=0.0)
REB = st.number_input('Total Rebounds (REB)', value=0.0)
AST = st.number_input('Assists (AST)', value=0.0)
STL = st.number_input('Steals (STL)', value=0.0)
BLK = st.number_input('Blocks (BLK)', value=0.0)
TOV = st.number_input('Turnovers (TOV)', value=0.0)

params = {
    'Name': Name,
    'GP': GP,
    'MIN': MIN,
    'PTS': PTS,
    'FGM': FGM,
    'FGA': FGA,
    'FG_': FG_,
    '_3P_Made': _3P_Made,
    '_3PA': _3PA,
    '_3P_': _3P_,
    'FTM': FTM,
    'FTA': FTA,
    'FT_': FT_,
    'OREB': OREB,
    'DREB': DREB,
    'REB': REB,
    'AST': AST,
    'STL': STL,
    'BLK': BLK,
    'TOV': TOV}


url = 'https://nba-test-draft-public-xam5swm3da-ew.a.run.app/predict'

if st.button('La prochaine légende ⭐⭐⭐?'):
    response = requests.get(url, params=params)

    pred = f"{response.json()['forecast']}"


    st.markdown(pred)

    if pred =="1.0":
        st.balloons()
        st.markdown("C'est la pépite que vous cherchiez !!!")
        st.image("lebron.webp")

    else:
        st.markdown("Peut-être pas la meilleur idée pour le moment ...")
        st.image("red-stop-sign-3d-illustration-free-png.webp")
