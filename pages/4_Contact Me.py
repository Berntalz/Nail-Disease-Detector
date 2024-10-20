import streamlit as st

st.header(":mailbox: GET IN TOUCH WITH ME!")

contact_form = """
<form action="https://formsubmit.co/aman0218.deep@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Name" required>
     <input type="email" name="email" placeholder="Email"  required>
     <textarea name="message" placeholder="Message"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Load and apply custom CSS
css_file_path = r"style.css"
with open(css_file_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
