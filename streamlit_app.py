import streamlit as st
import requests
import json
from PIL import Image


st.set_page_config(layout="wide")
st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 50px;"><b>Travel Recommender System</b></p>', unsafe_allow_html=True)
st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 30px;"><b>Welcome! In this travel recommender, select the top 5 categories you would like to do as part of an activity when you are travelling!</b></p>', unsafe_allow_html=True)
st.markdown("By: Fung Xue Feng ([GitHub](https://github.com/FungXF))([Linkedin](https://www.linkedin.com/in/xue-feng-fung/))")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    accommodation = st.checkbox('Accommodation', help='Activites that include accommodation')
with col2:
    activities = st.checkbox('Activities', help='Engaging in an activity')
with col3:
    adventure = st.checkbox('Adventure', help='Ziplining, Rafting, Snowshoeing and more')
with col4:
    air_tour = st.checkbox('Air Tour', help='Tour in the Air with Guide')
with col5:
    beach = st.checkbox('Beach', help='Visiting a beach')


col6, col7, col8, col9, col10 = st.columns(5)
with col6:
    brew_dis_win = st.checkbox('Brewery/ Distillery/ Winery', help='Visiting Brewery/Distillery/Winery')
with col7:
    camping = st.checkbox('Camping', help='Activites that involves camping')
with col8:
    classes_and_workshops = st.checkbox('Classes and Workshop', help='Activities that involves an instructor')
with col9:
    entertainment = st.checkbox('Entertainment', help='Live Entertainment')
with col10:
    rental = st.checkbox('Equipment Rental', help='Only renting of equipment (snowboard, bicycle, boat, etc), no tours')

    
col11, col12, col13, col14, col15 = st.columns(5)
with col11:
    food = st.checkbox('Food', help='Food is included')
with col12:
    hiking = st.checkbox('Hiking', help='Involves hiking')   
with col13:
    transport = st.checkbox('Includes Transport', help='Transport from A to B, includes passes and hop-on/off tours')
with col14:
    island = st.checkbox('Island Hopping', help='Visiting an island')    
with col15:
    land_tour = st.checkbox('Land Tour', help='Tour in the Land with Guide')


col16, col17, col18, col19, col20 = st.columns(5)
with col16:
    city = st.checkbox('Located In City', help='Activities that takes place in the City')
with col17:
    nature = st.checkbox('Located In Nature', help='Activities that takes place in Nature/Mountain')
with col18:
    mountain_views = st.checkbox('Mountain Views',help='Having Mountain Views')
with col19:
    park = st.checkbox('Park', help='Visiting Parks and Gardens')
with col20:
    photography = st.checkbox('Photoshoot', help='Photography service is provided/included')

col21, col22,col23,col24,col25 = st.columns(5)
with col21:
    cruise = st.checkbox('River Cruise', help='E.g. Wildlife watching, river cruise, ferry to another island')
with col22:
    sea_tour = st.checkbox('Sea Tour', help='Tour in the Sea with Guide')
with col23:
    sightseeing = st.checkbox('Sightseeing', help='Visting places of Interest')
with col24:
    experience = st.checkbox('Unique Experience', help='Experience an activity/do something "extra-ordinary"')    
with col25:
    wildlife = st.checkbox('Wildlife Spotting', help ='Spotting wildlife')
    
if sightseeing:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include Sightseeing:</b></p>', unsafe_allow_html=True)
    sight = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="1")
else: 
    sight = 0
if land_tour:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include Tour by Land:</b></p>', unsafe_allow_html=True)
    land_t = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="2")
else: 
    land_t = 0
if air_tour:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include Tour in Air:</b></p>', unsafe_allow_html=True)
    air_t = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="3")
else: 
    air_t = 0
if sea_tour:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include Tour of Sea:</b></p>', unsafe_allow_html=True)
    sea_t = sst.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="4")
else: 
    sea_t = 0
if park:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include visiting Park/Garden:</b></p>', unsafe_allow_html=True)
    parks = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="5")
else: 
    parks = 0
if city:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to be in the city:</b></p>', unsafe_allow_html=True)
    in_city = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="6")
else: 
    in_city = 0
if nature:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include being in nature:</b></p>', unsafe_allow_html=True)
    nat = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="7")
else: 
    nat = 0
if accommodation:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include Accommodation:</b></p>', unsafe_allow_html=True)
    accom = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="8")
else: 
    accom = 0
if camping:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include Camping:</b></p>', unsafe_allow_html=True)
    camp = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="9")
else: 
    camp = 0
if cruise:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include Boat Tour:</b></p>', unsafe_allow_html=True)
    crui = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="10")
else: 
    crui = 0
if island:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include being on island:</b></p>', unsafe_allow_html=True)
    islands = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="11")
else: 
    islands = 0
if entertainment:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include entertainment:</b></p>', unsafe_allow_html=True)
    enter = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="12")
else: 
    enter = 0
if classes_and_workshops:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include classes and workshops:</b></p>', unsafe_allow_html=True)
    class_work = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="13")
else: 
    class_work = 0
if transport:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include Transport:</b></p>', unsafe_allow_html=True)
    trans = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="14")
else: 
    trans = 0
if experience:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include a unique experience:</b></p>', unsafe_allow_html=True)
    exp = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="15")
else: 
    exp = 0
if brew_dis_win:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include brewery/distillery/winery:</b></p>', unsafe_allow_html=True)
    brewery_distillery_winery = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="16")
else: 
    brewery_distillery_winery = 0
if photography:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include photoshoots:</b></p>', unsafe_allow_html=True)
    photo = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="17")
else: 
    photo = 0
if wildlife:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include observing wildlife:</b></p>', unsafe_allow_html=True)
    wild = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="18")
else: 
    wild = 0
if adventure:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to be adventurous:</b></p>', unsafe_allow_html=True)
    advent = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="19")
else: 
    advent = 0
if beach:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include visting a beach:</b></p>', unsafe_allow_html=True)
    beaches = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="20")
else: 
    beaches = 0
if hiking:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Activity needs to include hiking:</b></p>', unsafe_allow_html=True)
    hike = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="21")
else: 
    hike = 0
if rental:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Renting of an equipment:</b></p>', unsafe_allow_html=True)
    rentals = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="22")
else: 
    rentals = 0
if activities:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Engaging in an activity:</b></p>', unsafe_allow_html=True)
    activity = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="23")
else: 
    activity = 0
if mountain_views:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Having Mountain views:</b></p>', unsafe_allow_html=True)
    mount_views = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="24")
else: 
    mount_views = 0
if food:
    st.markdown('<p style="font-family:helvetica; color:#5A5A5A; font-size: 25px;"><b>Food Must be included in the activity:</b></p>', unsafe_allow_html=True)
    foods = st.slider('On a scale of 1 (Its ok to have) to 5 (Must Have)',1,5,3, key="25")
else: 
    foods = 0

values = (sightseeing + land_tour + air_tour + sea_tour + park + city + nature + accommodation + 
          camping + cruise + island + entertainment + classes_and_workshops + transport + experience + 
          brew_dis_win + photography + wildlife + adventure + beach + hiking + rental + activities + mountain_views + food)

# button1, button2, na1, na2, na3 = st.columns(5)
# with button1:
submit = st.button('Show Recommendation')    
# with button2:
submit2 = st.button("Help me decide!")

    
    
# Randomizer if they cannot decide on the type of activites
if submit2:
    api_url = 'https://dsicapstone-l7bv2piloq-as.a.run.app'
    api_route = '/random'
    
    profile = {'empty':'empty'}
    response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) # json.dumps() converts dict to JSON
    output = response.json()
    names = output['names']
    url = output['url']
    image = output['image']    
    
    #display with the columns
    colrand1, colrand2, = st.columns(2)

    with colrand1:
        st.image((output['image'][0]), use_column_width='always')
        st.markdown(f"[{(' '.join(names[0].split('_'))).title()}](%s)" % url[0])

    with colrand2:
        st.image((output['image'][1]),width=300,)
        st.markdown(f"[{(' '.join(names[1].split('_'))).title()}](%s)" % url[1])

    colrand3, colrand4 = st.columns(2)
    with colrand3:
        st.image((output['image'][2]),width=300,)
        st.markdown(f"[{(' '.join(names[2].split('_'))).title()}](%s)" % url[2])

    with colrand4:
        st.image((output['image'][3]),width=300,)
        st.markdown(f"[{(' '.join(names[3].split('_'))).title()}](%s)" % url[3])

    colrand5, colrand6 = st.columns(2)

    with colrand5:
        st.image((output['image'][4]),width=300,)
        st.markdown(f"[{(' '.join(names[4].split('_'))).title()}](%s)" % url[4])

    with colrand6:
        st.image((output['image'][5]),width=300,)
        st.markdown(f"[{(' '.join(names[5].split('_'))).title()}](%s)" % url[5])

# After selecting the 5 categories of activites, the recommender would then pull out the top 6 recommended activites
if submit:
    if values != 5:
        st.error("**Choose exactly 5 options!**")
        
    else:
        profile = {'sightseeing': sight, 'land tour': land_t, 'air tour': air_t, 'sea tour': sea_t,
           'park': parks, 'city': in_city, 'nature': nat, 'accommodation': accom,
           'camping': camp, 'cruise': crui, 'island': islands, 'entertainment': enter, 
           'classes & workshops': class_work, 'transport': trans, 'experience': exp, 
           'brewery/winery/distillery': brewery_distillery_winery, 'photography': photo,
           'wildlife': wild, 'adventure': advent, 'beach': beaches, 'hiking': hike, 
           'rental': rentals, 'activities': activity, 'mountain views': mount_views, 'food': foods}
                      
        api_url = 'https://dsicapstone-l7bv2piloq-as.a.run.app'
        api_route = '/predict'

        response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) 
        output = response.json()
        names = output['names']
        url = output['url']
        image = output['image']
        
        #display with the columns
        colres1, colres2, = st.columns(2)

        with colres1:
            st.image((image[0]),width=300,)
            st.markdown(f"[{(' '.join(names[0].split('_'))).title()}]")

        with colres2:
            st.image((image[1]),width=300,)
            st.markdown(f"[{(' '.join(names[1].split('_'))).title()}](%s)" % url[1])
        
        colres3, colres4 = st.columns(2)
        with colres3:
            st.image((image[2]),width=300,)
            st.markdown(f"[{(' '.join(names[2].split('_'))).title()}](%s)" % url[2])
        
        with colres4:
            st.image((image[3]),width=300,)
            st.markdown(f"[{(' '.join(names[3].split('_'))).title()}](%s)" % url[3])
        
        colres5, colres6 = st.columns(2)

        with colres5:
            st.image((image[4]),width=300,)
            st.markdown(f"[{(' '.join(names[4].split('_'))).title()}](%s)" % url[4])

        with colres6:
            st.image((image[5]),width=300,)
            st.markdown(f"[{(' '.join(names[5].split('_'))).title()}](%s)" % url[5])

# Changing the background and words styling and colours                       
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
         background-color: #F0FFFF;
         }}
         .css-1aqmucy svg {{
             stroke: rgb(49, 51, 63);
         }}
         .css-81oif8, .css-10y5sf6, .css-1inwz65 {{
             font-size: 17px;
             font-weight: bold;
             color:#5A5A5A;
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
