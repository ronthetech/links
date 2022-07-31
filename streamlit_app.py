import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('profile-img.jpeg'))

st.header('Ron Jean-Francois')

st.info('Front End Developer proficient in HTML/CSS, Javascript, React, Node.js || Data Analyst proficient in SQL, Excel, Python || Content Creator and Tech-enthusiast with an interest in Data Science and Web Development')

icon_size = 20

# st_button('youtube', 'https://youtube.com/dataprofessor',
#          'Data Professor YouTube channel', icon_size)
# st_button('youtube', 'https://youtube.com/codingprofessor',
#          'Coding Professor YouTube channel', icon_size)
# st_button('medium', 'https://data-professor.medium.com/',
#          'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/rjthetech',
          'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/ron-jean-francois-224066136',
          'Follow me on LinkedIn', icon_size)
# st_button('newsletter', 'https://sendfox.com/dataprofessor/',
#          'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/ronjtech',
          'Buy me a Coffee', icon_size)
