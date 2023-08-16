import streamlit as st
from thefuzz import process, fuzz
import pandas as pd

name_town = pd.DataFrame([{'restaurant':'McDonalds',
                      'town':'Lewes'},
                     {'restaurant':'Pizza Palace',
                      'town':'Lewes'},
                     {'restaurant':'Burger Hole',
                      'town':'Eastbourne'},
                     {'restaurant':'Spice Garden',
                      'town':'Bexhill'},
                     {'restaurant':'Jade Leaf',
                      'town':'Brighton'}])

name_cuisine = pd.DataFrame([{'restaurant':'McDonald',
                      'cuisine':'Lewes'},
                     {'restaurant':'Pizza Place',
                      'cuisine':'Lewes'},
                     {'restaurant':'Burger H0le',
                      'cuisine':'Eastbourne'},
                     {'restaurant':'Spice Gdn.',
                      'cuisine':'Bexhill'},
                     {'restaurant':'Jade Lotus',
                      'cuisine':'Brighton'}])

st.table(name_town)
st.table(name_cuisine)


# Basic fuzzy match
names_1 = list(name_town['restaurant'])
names_2 = list(name_cuisine['restaurant'])

def fuzzy_match(str1, str2):
    return fuzz.token_set_ratio(str1, str2)

m1 = []
for i in names_2:
    m1.append(process.extract(i, names_2, limit=2))
name_town['matches'] = m1
st.table(name_town)

p=[]
m2 = []
for j in name_town['matches']:
    for k in j:
        if k[1] >= 80:
            p.append(k[0])
    m2.append(','.join(str(i) for i in p))
    p = []

name_town['matches'] = m2
st.table(name_town)

# More complex fuzzy match to match just closest value
team_score = pd.DataFrame([{'teams':'Brighton vs Eastbourne','score':'2:1'},
                          {'teams':'New York Nets vs Boston Red Sox','score':'Basleball score?'},
                          {'teams':'Lakers vs. Bulls','score':'100:92'},
                          {'teams':'England Australia','score':'300:156'},
                          {'teams':'Rwanda vs. Finland','score':'0:0'},
                          {'teams':'Chile vs. Croatia','score':'0:0'},])

team_time = pd.DataFrame([{'teams':'Btn. vs Ebn.','time':'16:00'},
                          {'teams':'Nets vs Sox','time':'15:00'},
                          {'teams':'La Lakers vs Chicago Bulls','time':'13:00'},
                          {'teams':'Eng. Aus.','time':'1:00pm'},
                          {'teams':'Rda. vs. Fld.','time':'06:00'},])

st.table(team_score)
st.table(team_time)

m1 = []
m2 = []
p = []

teams_1_list = team_score['teams'].to_list()
teams_2_list = team_time['teams'].to_list()

for i in teams_1_list:
    m1.append(process.extractOne(i, teams_2_list, scorer=fuzz.ratio))
team_score['matches'] = m1
# we see we have a match even when as humans we know there is no match, so we need a threshold
# to stop matches we don't want
st.table(team_score)

for j in team_score['matches']:
    if j[1] > 50:
        p.append(j[0])
    m2.append(",".join(p))
    p = []

team_score['true_matches'] = m2
st.table(team_score)

team_score_time = team_score.merge(team_time, how='left', left_on='true_matches', right_on='teams')
team_score_time.drop(['matches', 'true_matches', 'teams_y'], axis=1, inplace=True)
team_score_time.rename(columns={'teams_x':'teams'}, inplace=True)
st.table(team_score_time)


# using get_close_matches
name_money = pd.DataFrame([{'name':'Will', 'money':'£0.10',},
                           {'name':'Georgie', 'money':'£30',},
                           {'name':'Alistair', 'money':'£10',},
                           {'name':'John', 'money':'£13',},
                           {'name':'Rob', 'money':'LOTS',},
                           {'name':'Joe', 'money':'Some',},])

name_number = pd.DataFrame([{'name':'Will', 'account_number':'£0.10',},
                           {'name':'Georgie', 'account_number':'£30',},
                           {'name':'Alistair', 'account_number':'£10',},
                           {'name':'John', 'account_number':'£13',},
                           {'name':'Rob', 'account_number':'LOTS',},
                           {'name':'Joe', 'account_number':'Some',},])

