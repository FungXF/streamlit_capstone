import streamlit as st
import requests
import json

st.title('Travel Recommender System')
st.subheader('Welcome, in this travel recommender, select the top 5 categories you would like to do as part of an activity in overseas!')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    sightseeing = st.checkbox('Sightseeing')
with col2:
    land_tour = st.checkbox('Land Tour')
with col3:
    air_tour = st.checkbox('Air Tour')
with col4:
    sea_tour = st.checkbox('Sea Tour')
with col5:
    park = st.checkbox('Park')

col6, col7, col8, col9, col10 = st.columns(5)

with col6:
    city = st.checkbox('Located In City')
with col7:
    nature = st.checkbox('Located In Nature')
with col8:
    accommodation = st.checkbox('Accommodation')
with col9:
    camping = st.checkbox('Camping')
with col10:
    cruise = st.checkbox('Boat Tours')
    
col11, col12, col13, col14, col15 = st.columns(5)

with col11:
    island = st.checkbox('Island Hopping')   
with col12:
    entertainment = st.checkbox('Entertainment')   
with col13:
    classes_and_workshops = st.checkbox('Classes and Workshop')
with col14:
    transport = st.checkbox('Includes Transport')
with col15:
    experience = st.checkbox('Unique Experience')    

col16, col17, col18, col19, col20 = st.columns(5)

with col16:
    brew_dis_win = st.checkbox('Brewery/ Distillery/ Winery')
with col17:
    photography = st.checkbox('Photoshoot')
with col18:
    wildlife = st.checkbox('Wildlife Spotting')
with col19:
    adventure = st.checkbox('Adventure')
with col20:
    beach = st.checkbox('Beach')

col21, col22,col23,col24,col25 = st.columns(5)
with col21:
    hiking = st.checkbox('Hiking')
with col22:
    rental = st.checkbox('Equipment Rental')
with col23:
    ''
with col24:
    ''
with col25:
    ''
    
if sightseeing:
    st.subheader('Activity needs to include Sightseeing:')
    sight = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="1")
else: 
    sight = 0
if land_tour:
    st.subheader('Activity needs to include Tour by Land:')
    land_t = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="2")
else: 
    land_t = 0
if air_tour:
    st.subheader('Activity needs to include Tour in Air:')
    air_t = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="3")
else: 
    air_t = 0
if sea_tour:
    st.subheader('Activity needs to include Tour of Sea:')
    sea_t = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="4")
else: 
    sea_t = 0
if park:
    st.subheader('Activity needs to include visiting Park/Garden:')
    parks = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="5")
else: 
    parks = 0
if city:
    st.subheader('Activity needs to be in the city:')
    in_city = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="6")
else: 
    in_city = 0
if nature:
    st.subheader('Activity needs to include being in nature:')
    nat = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="7")
else: 
    nat = 0
if accommodation:
    st.subheader('Activity needs to include Accommodation:')
    accom = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="8")
else: 
    accom = 0
if camping:
    st.subheader('Activity needs to include Camping:')
    camp = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="9")
else: 
    camp = 0
if cruise:
    st.subheader('Activity needs to include Boat Tour:')
    crui = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="10")
else: 
    crui = 0
if island:
    st.subheader('Activity needs to include being on island:')
    islands = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="11")
else: 
    islands = 0
if entertainment:
    st.subheader('Activity needs to include entertainment:')
    enter = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="12")
else: 
    enter = 0
if classes_and_workshops:
    st.subheader('Activity needs to include classes and workshops:')
    class_work = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="13")
else: 
    class_work = 0
if transport:
    st.subheader('Activity needs to include Transport:')
    trans = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="14")
else: 
    trans = 0
if experience:
    st.subheader('Activity needs to include a unique experience:')
    exp = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="15")
else: 
    exp = 0
if brew_dis_win:
    st.subheader('Activity needs to include brewery/distillery/winery:')
    brewery_distillery_winery = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="16")
    brewery = brewery_distillery_winery/3
    distillery = brewery_distillery_winery/3
    winery = brewery_distillery_winery/3
else: 
    brewery = 0
    distillery = 0
    winery = 0
if photography:
    st.subheader('Activity needs to include photoshoots:')
    photo = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="17")
else: 
    photo = 0
if wildlife:
    st.subheader('Activity needs to include observing wildlife:')
    wild = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="18")
else: 
    wild = 0
if adventure:
    st.subheader('Activity needs to be adventurous:')
    advent = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="19")
else: 
    advent = 0
if beach:
    st.subheader('Activity needs to include visting a beach:')
    beaches = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="20")
else: 
    beaches = 0
if hiking:
    st.subheader('Activity needs to include hiking:')
    hike = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="21")
else: 
    hike = 0
if rental:
    st.subheader('Renting of an equipment:')
    rentals = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="22")
else: 
    rentals = 0

values = (sightseeing + land_tour + air_tour + sea_tour + park + city + nature + accommodation + 
          camping + cruise + island + entertainment + classes_and_workshops + transport + experience + 
          brew_dis_win + photography + wildlife + adventure + beach + hiking + rental)

# submit2 = st.button("I can't decide")

# if submit2:
#     user_input = 
#     namess = []
#     namess = random.choices(attractions['name'], k=6)
#         #display with the columns
#     colrand1, colrand2, colrand3 = st.columns(3)
#     with colrand1:
#         st.markdown((' '.join(namess[0].split('_'))).title())
#     #     st.image(posters[0])
#     with colrand2:
#         st.markdown((' '.join(namess[1].split('_'))).title())
#     # #     st.image(posters[1])
#     with colrand3:
#         st.markdown((' '.join(namess[2].split('_'))).title())
#     # #     st.image(posters[2])
#     colrand4, colrand5, colrand6 = st.columns(3)
#     with colrand4:
#         st.markdown((' '.join(namess[3].split('_'))).title())
#     # #     st.image(posters[3])
#     with colrand5:
#         st.markdown((' '.join(namess[4].split('_'))).title())
#     # #     st.image(posters[4])
#     with colrand6:
#         st.markdown((' '.join(namess[5].split('_'))).title())   

            
submit = st.button('Show Recommendation')

if submit:
    if values != 5:
        st.error("**Choose exactly 5 options!**")
        
    else:
        profile = {'sightseeing': sightseeing, 'land tour': land_t, 'air tour': air_t, 'sea tour': sea_t,
                   'park': park, 'city': in_city, 'nature': nat, 'accommodation': accom,
                   'camping': camp, 'cruise': crui, 'island': islands, 'entertainment': enter, 
                   'classes & workshops': class_work, 'transport': trans, 'experience': exp, 
                   'brewery': brewery, 'distillery': distillery, 'winery': winery, 'photography': photo,
                   'wildlife': wild, 'adventure': advent, 'beach': beaches, 'hiking': hike, 
                   'rental': rental}
        
        api_url = 'https://dsicapstone-l7bv2piloq-as.a.run.app'
        api_route = '/predict'

        response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) # json.dumps() converts dict to JSON
        names = response.json()['names']
        names = names['names']
        
        #display with the columns
        colres1, colres2, colres3 = st.columns(3)
        # col1 = st.columns(1)
        with colres1:
            st.markdown((' '.join(names[0].split('_'))).title())
        # #     st.image(posters[0])
        with colres2:
            st.markdown((' '.join(names[1].split('_'))).title())
        # #     st.image(posters[1])
        with colres3:
            st.markdown((' '.join(names[2].split('_'))).title())
        # #     st.image(posters[2])
        colres4, colres5, colres6 = st.columns(3)
        with colres4:
            st.markdown((' '.join(names[3].split('_'))).title())
        # #     st.image(posters[3])
        with colres5:
            st.markdown((' '.join(names[4].split('_'))).title())
        # #     st.image(posters[4])
        with colres6:
            st.markdown((' '.join(names[5].split('_'))).title())  
