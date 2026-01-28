# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 08:51:26 2026

@author: akani
"""

import streamlit as st

st.title("Akani's first app")
st.write("Hello, Akani!")
st.header("Number selection")

number = st.slider("Select a number", 2,500)
st.write(f"You chose: {number}")