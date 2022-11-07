import streamlit as st
import requests
import json

st.title('Travel Recommender System')
st.subheader('Welcome, in this travel recommender, select the top 5 categories you would like to do as part of an activity in overseas!')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    sightseeing = st.checkbox('Sightseeing', help='Visting places of Interest')
with col2:
    land_tour = st.checkbox('Land Tour', help='Tour in the Land with Guide')
with col3:
    air_tour = st.checkbox('Air Tour', help='Tour in the Air with Guide')
with col4:
    sea_tour = st.checkbox('Sea Tour', help='Tour in the Sea with Guide')
with col5:
    park = st.checkbox('Park', help='Visiting Parks and Gardens')

col6, col7, col8, col9, col10 = st.columns(5)

with col6:
    city = st.checkbox('Located In City', help='Activities that takes place in the City')
with col7:
    nature = st.checkbox('Located In Nature', help='Activities that takes place in Nature/Mountain')
with col8:
    accommodation = st.checkbox('Accommodation', help='Activites that include accommodation')
with col9:
    camping = st.checkbox('Camping', help='Activites that involves camping')
with col10:
    cruise = st.checkbox('River Cruise', help='E.g. Wildlife watching, river cruise, ferry to another island')
    
col11, col12, col13, col14, col15 = st.columns(5)

with col11:
    island = st.checkbox('Island Hopping', help='Visiting an island')   
with col12:
    entertainment = st.checkbox('Entertainment', help='Live Entertainment')   
with col13:
    classes_and_workshops = st.checkbox('Classes and Workshop', help='Activities that involves an instructor')
with col14:
    transport = st.checkbox('Includes Transport', help='Transport from A to B, includes passes and hop-on/off tours')
with col15:
    experience = st.checkbox('Unique Experience', help='Experience an activity/do something "extra-ordinary"')    

col16, col17, col18, col19, col20 = st.columns(5)

with col16:
    brew_dis_win = st.checkbox('Brewery/ Distillery/ Winery', help='Visiting Brewery/Distillery/Winery')
with col17:
    photography = st.checkbox('Photoshoot', help='Photography service is provided/included')
with col18:
    wildlife = st.checkbox('Wildlife Spotting', help ='Spotting wildlife')
with col19:
    adventure = st.checkbox('Adventure', help='Ziplining, Rafting, Snowshoeing and more')
with col20:
    beach = st.checkbox('Beach', help='Visiting a beach')

col21, col22,col23,col24,col25 = st.columns(5)
with col21:
    hiking = st.checkbox('Hiking', help='Involves hiking')
with col22:
    rental = st.checkbox('Equipment Rental', help='Only renting of equipment (snowboard, bicycle, boat, etc), no tours')
with col23:
    activities = st.checkbox('Activities', help='Engaging in an activity')
with col24:
    mountain_views = st.checkbox('Mountain Views',help='Having Mountain Views')
with col25:
    food = st.checkbox('Food', help='Food is included')
    
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
if activities:
    st.subheader('Engaging in an activity:')
    activity = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="23")
else: 
    activity = 0
if mountain_views:
    st.subheader('Having Mountain views:')
    mount_views = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="24")
else: 
    mount_views = 0
if food:
    st.subheader('Food Must be included in the activity:')
    foods = st.slider('On a scale of 1(Its ok to have) to 5(Must Have)', 1,5,3, key="25")
else: 
    foods = 0

values = (sightseeing + land_tour + air_tour + sea_tour + park + city + nature + accommodation + 
          camping + cruise + island + entertainment + classes_and_workshops + transport + experience + 
          brew_dis_win + photography + wildlife + adventure + beach + hiking + rental + activities + mountain_views + food)

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

submit3 = st.button("DO NOT PRESS")

if submit3:
    st.image(
    "https://i.postimg.cc/k5W6txRc/Screenshot-2022-10-13-145818-removebg-preview.png",
    width=400, # Manually Adjust the width of the image as per requirement
    )
    
# if submit3:

#     # https://drive.google.com/file/d/1EtUyVygCCtpMSCEE-EV615u53fi8dGOW/view?usp=share_link

#     def add_bg_from_url():
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image: url("https://drive.google.com/file/d/1EtUyVygCCtpMSCEE-EV615u53fi8dGOW/view?usp=share_link");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

#     add_bg_from_url() 
    
    
#     st.markdown(   f"""   <style>
#        p {
#        background-image: url("https://images.pexels.com/photos/3935702/pexels-photo-3935702.jpeg?auto=compress&cs=tinysrgb&w=1600");
#        }
#        </style>   """,   unsafe_allow_html=True)
            
submit = st.button('Show Recommendation')

if submit:
    if values != 5:
        st.error("**Choose exactly 5 options!**")
        
    else:
        profile = {'sightseeing': sight, 'land tour': land_t, 'air tour': air_t, 'sea tour': sea_t,
           'park': parks, 'city': in_city, 'nature': nat, 'accommodation': accom,
           'camping': camp, 'cruise': crui, 'island': islands, 'entertainment': enter, 
           'classes & workshops': class_work, 'transport': trans, 'experience': exp, 
           'brewery': brewery, 'distillery': distillery, 'winery': winery, 'photography': photo,
           'wildlife': wild, 'adventure': advent, 'beach': beaches, 'hiking': hike, 
           'rental': rentals, 'activities': activity, 'mountain views': mount_views, 'food': foods}
                      
        api_url = 'https://dsicapstone-l7bv2piloq-as.a.run.app'
        api_route = '/predict'

        response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) # json.dumps() converts dict to JSON
        output = response.json()
        names = output['names']
        url = output['url']
        
        #display with the columns
        colres1, colres2, colres3 = st.columns(3)
        # col1 = st.columns(1)
        with colres1:
            st.markdown(f"[{(' '.join(names[0].split('_'))).title()}](%s)" % url[0])
        # #     st.image(posters[0])
        with colres2:
            st.markdown(f"[{(' '.join(names[1].split('_'))).title()}](%s)" % url[1])
        # #     st.image(posters[1])
        with colres3:
            st.markdown(f"[{(' '.join(names[2].split('_'))).title()}](%s)" % url[2])
        # #     st.image(posters[2])
        colres4, colres5, colres6 = st.columns(3)
        with colres4:
            st.markdown(f"[{(' '.join(names[3].split('_'))).title()}](%s)" % url[3])
        # #     st.image(posters[3])
        with colres5:
            st.markdown(f"[{(' '.join(names[4].split('_'))).title()}](%s)" % url[4])
        # #     st.image(posters[4])
        with colres6:
            st.markdown(f"[{(' '.join(names[5].split('_'))).title()}](%s)" % url[5])
