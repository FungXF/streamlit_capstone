import streamlit as st
import requests
import json
from PIL import Image

#original_title = '<p style="font-family:helvetica; color:Black; font-size: 50px;"><b>Travel Recommender System</b></p>'
st.markdown('<p style="font-family:helvetica; color:White; font-size: 50px;"><b>Travel Recommender System</b></p>', unsafe_allow_html=True)
st.markdown('<p style="font-family:helvetica; color:White; font-size: 30px;"><b>Welcome! In this travel recommender, select the top 5 categories you would like to do as part of an activity in overseas!</b></p>', unsafe_allow_html=True)


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
    food = st.checkbox('Food', help='Food is included')
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
    accommodation = st.checkbox('Accommodation', help='Activites that include accommodation')
    
if sightseeing:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include Sightseeing:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    sight = st.slider('',1,5,3, key="1", label_visibility = "collapsed")
else: 
    sight = 0
if land_tour:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include Tour by Land:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    land_t = st.slider('',1,5,3, key="2", label_visibility = "collapsed")
else: 
    land_t = 0
if air_tour:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include Tour in Air:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    air_t = st.slider('',1,5,3, key="3", label_visibility = "collapsed")
else: 
    air_t = 0
if sea_tour:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include Tour of Sea:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    sea_t = st.slider('',1,5,3, key="4", label_visibility = "collapsed")
else: 
    sea_t = 0
if park:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include visiting Park/Garden:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    parks = st.slider('',1,5,3, key="5", label_visibility = "collapsed")
else: 
    parks = 0
if city:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to be in the city:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    in_city = st.slider('',1,5,3, key="6", label_visibility = "collapsed")
else: 
    in_city = 0
if nature:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include being in nature:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    nat = st.slider('',1,5,3, key="7", label_visibility = "collapsed")
else: 
    nat = 0
if accommodation:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include Accommodation:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    accom = st.slider('',1,5,3, key="8", label_visibility = "collapsed")
else: 
    accom = 0
if camping:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include Camping:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    camp = st.slider('',1,5,3, key="9", label_visibility = "collapsed")
else: 
    camp = 0
if cruise:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include Boat Tour:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    crui = st.slider('',1,5,3, key="10", label_visibility = "collapsed")
else: 
    crui = 0
if island:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include being on island:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    islands = st.slider('',1,5,3, key="11", label_visibility = "collapsed")
else: 
    islands = 0
if entertainment:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include entertainment:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    enter = st.slider('',1,5,3, key="12", label_visibility = "collapsed")
else: 
    enter = 0
if classes_and_workshops:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include classes and workshops:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    class_work = st.slider('',1,5,3, key="13", label_visibility = "collapsed")
else: 
    class_work = 0
if transport:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include Transport:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    trans = st.slider('',1,5,3, key="14", label_visibility = "collapsed")
else: 
    trans = 0
if experience:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include a unique experience:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    exp = st.slider('',1,5,3, key="15", label_visibility = "collapsed")
else: 
    exp = 0
if brew_dis_win:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include brewery/distillery/winery:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    brewery_distillery_winery = st.slider('',1,5,3, key="16", label_visibility = "collapsed")
else: 
    brewery_distillery_winery = 0
if photography:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include photoshoots:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    photo = st.slider('',1,5,3, key="17", label_visibility = "collapsed")
else: 
    photo = 0
if wildlife:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include observing wildlife:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    wild = st.slider('',1,5,3, key="18", label_visibility = "collapsed")
else: 
    wild = 0
if adventure:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to be adventurous:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    advent = st.slider('',1,5,3, key="19", label_visibility = "collapsed")
else: 
    advent = 0
if beach:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include visting a beach:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    beaches = st.slider('',1,5,3, key="20", label_visibility = "collapsed")
else: 
    beaches = 0
if hiking:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Activity needs to include hiking:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    hike = st.slider('',1,5,3, key="21", label_visibility = "collapsed")
else: 
    hike = 0
if rental:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Renting of an equipment:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    rentals = st.slider('',1,5,3, key="22", label_visibility = "collapsed")
else: 
    rentals = 0
if activities:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Engaging in an activity:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    activity = st.slider('',1,5,3, key="23", label_visibility = "collapsed")
else: 
    activity = 0
if mountain_views:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Having Mountain views:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    mount_views = st.slider('',1,5,3, key="24", label_visibility = "collapsed")
else: 
    mount_views = 0
if food:
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 25px;"><b>Food Must be included in the activity:</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:helvetica; color:White; font-size: 15px;"><b>On a scale of 1(Its ok to have) to 5(Must Have)</b></p>', unsafe_allow_html=True)
    foods = st.slider('',1,5,3, key="25", label_visibility = "collapsed")
else: 
    foods = 0

values = (sightseeing + land_tour + air_tour + sea_tour + park + city + nature + accommodation + 
          camping + cruise + island + entertainment + classes_and_workshops + transport + experience + 
          brew_dis_win + photography + wildlife + adventure + beach + hiking + rental + activities + mountain_views + food)

submit2 = st.button("Help me decide!")

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
        st.image((output['image'][0]),width=300,)
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

# submit3 = st.button("DO NOT PRESS")

# if submit3:
#     st.image(
#     "https://i.postimg.cc/k5W6txRc/Screenshot-2022-10-13-145818-removebg-preview.png",
#     width=400, # Manually Adjust the width of the image as per requirement
#     )
    
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


# https://i.etsystatic.com/10250157/r/il/4c1bc8/3733438535/il_1080xN.3733438535_f6tl.jpg
#https://iphoneswallpapers.com/wp-content/uploads/2021/10/World-Map-iPhone-Wallpaper.jpg
# https://i.ebayimg.com/images/g/zncAAOSw5DBiaQuz/s-l1600.jpg
# https://images.pexels.com/photos/3935702/pexels-photo-3935702.jpeg?auto=compress&cs=tinysrgb&w=1600


submit = st.button('Show Recommendation')

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

        response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) # json.dumps() converts dict to JSON
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

            
            
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1527998257557-0c18b22fa4cc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1336&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         a {{
             color: #f65282;
         }}

         a:hover {{
             color: #ffc4c0;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
