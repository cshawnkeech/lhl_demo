"""
Hello page
"""
import time
import streamlit as st


st.set_page_config(
    page_title='Hello World!',
    page_icon=':sunglasses:',
)

st.write('# Welcome to my app demo!')

st.markdown(
    """
    I created a multi-page app to demonstrate some of the capabilities of
    Streamlit.

    :sparkles: Feel free to explore :mag: what you can create.
    The possibilities are endless :infinity:!

    :sparkles: The cool sidebar on the left :point_left: lets you
        navigate between the different pages.

    :sparkles: Go ahead... try it out for yourself.
    Don't take ***my*** word for it :wink:!
"""
)


def ready():
    """
    a small example function
    """
    msg = st.toast("LET'S")
    time.sleep(1)
    msg.toast('GOOOOOOO...')
    time.sleep(1)
    msg.toast(':rocket: :rocket: :rocket: :rocket: :rocket:')


if st.button('ARE YOU READY?'):
    ready()
