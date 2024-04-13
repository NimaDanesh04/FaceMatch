import streamlit as st
import sqlite3 as sql
from hashlib import sha256

if 'key' in st.session_state:
    if st.session_state['key']:
        st.success(f'your in your accont {st.session_state["name"]} {st.session_state["last_name"]}')
else:
    st.title('login')
    U_name = st.text_input('plaese enter your email :')

    password = st.text_input('plaese enter your password :', type='password')
    
    conn = sql.connect('pass_data.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM pass')
    pass_x = password + U_name
    data = cur.fetchall()

    pass_2 = sha256(pass_x.encode()).hexdigest()
    
    start = st.button('click me')
    ww = False
    if start:
        for i in data:
            if U_name == i[2] and pass_2 == i[3]:
                st.write('You are in your account and have full access to the site')
                st.session_state["key"] = True
                ww = True
                st.session_state["name"] = i[0]
                st.session_state["last_name"] = i[1]
                break
        if not ww:
            st.write('Your email or password is wrong, please correct it')
        conn.close()
    
