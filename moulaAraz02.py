import streamlit as st
import requests
st.set_page_config(page_title="Bored Activity Suggestions", page_icon="🤹") 
st.title('Bored API app')
st.sidebar.header('input')## a heading sidebar na andar awse
selected_type = st.sidebar.selectbox('select an activity type'  ,['education', 'recreational', 'social', 'diy', 'charity', 'cooking', 'relaxation', 'music', 'busywork'])

suggested_activity_url = f'https://www.boredapi.com/api/activity/?type={selected_type}'
#defingin the api to be send
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json() # make the incoming data form the api in the json formait

c1 , c2 = st.columns(2)# dividing the page in 2 columns 

with c1: ## working on the first column , we firs oepn it as afile
    with st.expander('about this page'):# addin an expander in th efirst columns
        st.write('are you bored? the ** Bored API app** provides suggestions for you')
with c2: 
    with st.expander('JSON'):
        st.write(suggested_activity) ## giving the name of the acitivt in the json format

# giving extra informaiton abou the activiy in the humanf readable form


st.header('suggested activity')
st.info(suggested_activity['activity'])# giving the name of the activiy from the first part of the json 

col1 , col2 , col3 = st.columns(3)# making three columns to givev information abouthe the acticity specifics
with col1:
    st.metric(label = 'number of the participants' , value = suggested_activity['participants']  ,delta= '')
    st.metric(label = 'type of the activity' , value= suggested_activity['type'] , delta= '')
    st.metric(label = 'price' , value = suggested_activity['price'] , delta= '')



