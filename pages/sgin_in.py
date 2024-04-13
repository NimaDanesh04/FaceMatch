from hashlib import sha256
import streamlit as st
import sqlite3 as sql
import re

st.set_page_config(page_title='my web app', page_icon=":tada", layout='wide')

if 'key' in st.session_state:
    if st.session_state['key']:
        st.success(f'your in your accont {st.session_state["name"]} {st.session_state["last_name"]}')
else:
    st.header('sgin in')

    name = st.text_input('please enter your name')
    last_name = st.text_input('please enter your lasn name')
    email = st.text_input('plaese enter your User email :')
    password = st.text_input('please enter your password Only with 8 characters :', type='password')
    password_x = password+email
    password_2 = sha256(password_x.encode()).hexdigest()
    
    def email_re(email_2):
        if re.search(r'^[a-zA-Z1-9]+@[a-zA-Z1-9]+\.com$', email_2):
            return True
        return False
    

    def password_re(p):
        if re.search(r'^[a-zA-Z1-9]{8}$', p):
            return True
        return False


    conn = sql.connect('pass_data.db')
    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Pass(
        frist_name TEXT,
        last_name TEXT,
        u_name TEXT,
        password TEXT);
    """)

    rajex = False
    save = st.button('save')
    if email_re(email) and password_re(password) and save:
        st.success('your password and email is right')
        rajex = True
    elif not email_re(email) and email != '':
        st.error('your email is not right please fix it')
    if not password_re(password) and password != '':
        st.error('plase fixs your password')
    data = (name, last_name, email, password_2)
    if save and rajex:
        cur.execute('INSERT INTO Pass VALUES(?, ?, ?, ?)', data)
        st.session_state['key'] = True
        st.session_state['name'] = name
        st.session_state['last_name'] = last_name
    conn.commit()
    conn.close()
