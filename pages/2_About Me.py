import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="About Me",
    page_icon="people"
)

# Custom CSS to change the background color of the title
st.markdown(
    """
    <style>
        .title-wrapper {
            background-color: red;
        }
        img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(":red[About Me]:male-technologist:")

st.markdown("<br><br>", unsafe_allow_html=True)

# Define the layout for each team member
def team_member_layout(image_path, name, roll_number, description, linkedin_link, github_link):
    # Image column
    st.image(image_path)
    # Text column
    st.header(f":blue[**{name} ({roll_number})**] ")
    st.write(description)

    # Social media links

    st.subheader(f":red[Connect] with {name}:")
    col1, col2 = st.columns(2)
    col1.subheader(f":link:[LinkedIn]({linkedin_link})")
    col2.subheader(f":computer:[GitHub]({github_link})")

# Siddhanth Garg
team_member_layout(
    image_path="images/aman.jpeg",
    name="Aman Deep",
    roll_number="21BIT0225",
    description="I'm a dedicated and motivated learner with a burning curiosity for all things data-driven. "
                "Currently pursuing my studies in Computer Science, I'm on a mission to unravel the mysteries hidden within vast data sets, "
                "harnessing their power to drive innovation and solve real-world problems. Through hands-on projects and rigorous coursework, "
                "I have gained a solid foundation in various ML algorithms, predictive modeling, and data visualization techniques. "
                "My experience spans from developing supervised learning models to exploring the exciting realm of deep learning and neural networks.",
    linkedin_link="https://www.linkedin.com/in/aman-deep-28619b216/",
    github_link="https://github.com/Berntalz"

)

st.markdown("<br>", unsafe_allow_html=True)

# Closing statement
st.write("I hope you liked the effort for this model and show some love ❤️.")
