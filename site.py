from streamlit_extras.grid import grid
import streamlit as st 
st.set_page_config(
    page_title=("Ihsan's very goofy website"))
st.title("Ihsan's very goofy website ")
st.image("https://emojiisland.com/cdn/shop/products/Emoji_Icon_-_Smiling_grande.png?v=1571606089","HAPPY FACE")

# Creates a grid where each row has 3 equal-width columns
my_grid = grid(3, vertical_align="bottom")
projects_per_row = 3
cols = st.columns(projects_per_row)
with cols[0]:
    st.container()
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmJINGQbCB9Ejrzlq0iP3JJUvAA0YkOBUmww&s")
    st.write("hi")

with cols[1]:
    st.container()
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmJINGQbCB9Ejrzlq0iP3JJUvAA0YkOBUmww&s")
    st.write("this")

class Project:
    def __init__(self, name, image, link):
        self.name = name 
        self.image = image 
        self.link = link



projects = [
    Project("PONGY", "./Pictures/PONGY.png" ,"https://trinket.io/python/8aa6f3197031" ),
    Project("Mario Jump","./Pictures/Mario jump.png", "https://trinket.io/python/9a9e2db567ec")
]





# [0, 1, 2]
for i in range(len(cols)):
    column = cols[i]
    with column:
        st.container()
        current_project = projects [i+0]
        st.image(current_project.image)
        st.write(current_project.name)
        

# 1 - we want to store our project information somehow
# Classes and objects
# 2 - make our projects into a list
# Common sense
# 3 - Use a for loop and go over each project
#why do I need to do this 0 my god
# 4 - For every project, let's make a grid box