import streamlit as st


pg = st.navigation([st.Page('model.py'), st.Page('second_page.py')])

pg.run()