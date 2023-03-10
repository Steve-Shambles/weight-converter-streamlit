import streamlit as st

def convert_weight(weight, unit):
    try:
        weight = float(weight)
    except ValueError as value_error:
        st.error(value_error)
        return

    stones = 0
    pounds = 0
    kg = 0

    if unit == 'stones':
        stones = weight
        pounds = weight * 14
        kg = weight * 6.35
    elif unit == 'pounds':
        stones = weight / 14
        pounds = weight
        kg = weight * 0.453592
    elif unit == 'kgrams':
        stones = weight / 6.35
        pounds = weight / 0.453592
        kg = weight

    message = f'{round(kg, 2)} kgrams\n'
               '{round(stones, 2)} stones\n'
               '{round(pounds, 2)} pounds'
    st.success(message)

st.title('Weight Converter')

weight = st.text_input('Enter weight:')
unit = st.selectbox('Select unit:', ('stones', 'pounds', 'kgrams'))

if st.button('Convert'):
    convert_weight(weight, unit)
