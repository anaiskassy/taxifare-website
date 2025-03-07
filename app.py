import streamlit as st
import requests
import pandas as pd
# from folium import LatLngPopup,Map
# from streamlit_folium import st_folium
'''
# TaxiFareModel predictions in NYC
'''


'''
## Please enter informations for the ride :
'''
col1, col2, col3 = st.columns(3,border=True)
with col1 :
    st.subheader('General info')
    #- date and time to str
    d = st.date_input('Insert pickup date')
    t = st.time_input("Set pickup time")
    pickup = f'{d}+{t}'
    #- passenger count to int
    passenger = st.number_input('Insert the number of passengers',min_value=1, max_value=8,step=1)
with col2 :
    st.subheader('Pickup location')
    #- pickup longitude to float
    p_long = st.number_input('Insert pickup longitude',format="%0.6f",value=-73.950655)
    #- pickup latitude to float
    p_lat = st.number_input('Insert pickup latitude',format="%0.6f",value=40.783282)
with col3 :
    st.subheader('Dropoff location')
    #- dropoff longitude to float
    d_long = st.number_input('Insert dropoff longitude',format="%0.6f",value=-73.984365)
    #- dropoff latitude to float
    d_lat = st.number_input('Insert dropoff latitude',format="%0.6f",value=40.769802)

data = pd.DataFrame([[p_lat,p_long],
                   [d_lat,d_long]],
                   columns=["lat",'lon'])
st.map(data)

# m = Map()
# m.add_child(LatLngPopup())
# map = st_folium(m, height=350, width=700)
# data = map['last_clicked']['lat'],map['last_clicked']['lng']

# if data is not None:
    # st.write(data)

'''
## Click to see an estimated fare for the ride :
'''
info = f'pickup_datetime={pickup}&pickup_longitude={p_long}&pickup_latitude={p_lat}&dropoff_longitude={d_long}&dropoff_latitude={d_lat}&passenger_count={passenger}'
url = 'https://taxifare-159309351831.europe-west1.run.app'+'/predict?'+info

left, center, _3 = st.columns(3)
fare = None
with left :
    if st.button("Request fare", type="primary") :
        req = requests.get(url).json()
        fare = round(req['fare'],2)
        st.snow()
with center :
    if not fare is None :
        st.metric(label="Expected fare", value=f"$ {fare}",border=True)
