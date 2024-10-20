import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
from streamlit_option_menu import option_menu

model = tf.keras.models.load_model('vgg-16-nail.h5')

st.set_page_config(
    page_title="Disease prediction Model",
    page_icon="cast"
)

# Dictionary containing disease names, prevention steps, and additional information
disease_info = {
    'Darier_s disease': {
        'prevention': [" - Do consult a dermatologist for diagnosis and treatment.",
                       " - Management may include topical medications, oral retinoids, or other therapies based on the severity of the condition."],

    },
    'Muehrck-e_s lines': {
        'prevention': ["Prevention steps for Muehrck-e_s lines."],
        'additional_info': ["Additional information for Muehrck-e_s lines."]
    },
    'eczema': {
        'prevention': [
            "Do follow your dermatologist's recommended treatment plan, which may include:",
            "- Using moisturizers regularly.",
            "- Applying topical corticosteroids or immunomodulators.",
            "- Avoiding triggers like certain soaps or allergens.",
            "- Don't scratch the affected areas, as it can exacerbate the condition."
        ],

    },

    'half and half nailes (Lindsay_s nails)': {
        'prevention': [
            "- Do consult with a healthcare professional for proper evaluation and diagnosis.",
            "- The cause of the nail discoloration should be determined to guide treatment."
        ],

    },

    'leukonychia': {
        'prevention': [
            "- Do seek medical advice if you have leukonychia, as it can be related to various causes, including trauma or fungal infections.",
            " - Treatment depends on the underlying cause. Fungal infections may require antifungal therapy."
        ],

    },

    'koilonychia': {
        'prevention': [
            "- Do see a doctor for a diagnosis and management, as it may be related to iron deficiency anemia or other medical issues.",
            "- Addressing the underlying condition is crucial. Iron supplements may be prescribed."
        ],

    },

    'Muehrck-e_s lines': {
        'prevention': [

            "- Do consult with a healthcare professional to identify the underlying cause.",
            " - Management focuses on addressing the underlying condition or cause."
        ],

    },

    'splinter hemmorrage': {
        'prevention': [
            "- Do consult with a healthcare professional for a proper evaluation, as it can be related to various medical conditions.",
            "- Treatment is based on addressing the underlying cause, which may involve managing infections or other health issues."
        ],

    },

    'red lunula': {
        'prevention': [
            "- Do seek medical advice if you notice red lunula, as it can indicate underlying health problems.",
            "- Management involves identifying and treating the underlying condition."
        ],

    },

    'onycholycis': {
        'prevention': [
            "Do follow your dermatologist's recommended treatment plan, which may include:",
            "- Avoid activities that may worsen onycholysis, such as exposing your nails to moisture for extended periods."
        ],

    },

    'pale nail': {
        'prevention': [
            "- Do consult a healthcare provider to determine the cause of pale nails, as it may be due to anemia or other medical issues.",
            " - Treatment should address the underlying cause, which may include iron supplements or other interventions."
        ],

    },

    'terry_s nail': {
        'prevention': [
            "- Do see a doctor for a proper diagnosis, as Terry's nails can be a sign of liver or kidney disease.",
            "- Managing the underlying health condition is the primary focus.",
        ],

    },

    'white nail': {
        'prevention': [
            "- Do consult a healthcare provider if you have white nails, as it can be associated with several conditions, including liver disease.",
            "- Treatment should target the underlying cause, which may include addressing liver issues or other health problems."
        ],

    },

    'yellow nails': {
        'prevention': [
            "- Do seek medical advice if you have yellow nails, as it can be caused by fungal infections or other health issues.",
            "- Management may involve antifungal treatment or addressing underlying health concerns."
        ],

    },

    'clubbing': {
        'prevention': [
            "- Do seek medical evaluation if you notice clubbing of the fingers, as it can be a sign of various underlying conditions such as lung or heart disease.",
            " - Management focuses on treating the underlying cause."
        ],

    },

    'bluish nail': {
        'prevention': [
            "- Do consult a doctor if you have bluish nails, as it may indicate poor oxygenation or circulation problems.",
            " - Treatment depends on the underlying cause and may include addressing respiratory or cardiac issues."
        ],

    },

    'beau_s lines': {
        'prevention': [
            "- Do seek medical attention if you notice Beau's lines, as they can indicate underlying health issues like infection, trauma, or systemic diseases.",
            "- The underlying cause should be treated to resolve the lines."
        ],

    },

    'aloperia areata': {
        'prevention': [
            "- Do consult with a dermatologist for diagnosis and treatment options.",
            " - Treatment may include corticosteroid injections, topical treatments, or immunotherapy.",
            " - Consider support groups or counseling for emotional well-being."
        ],

    },
}

st.title("Predict the health condition :white_check_mark: ")

# Create a file uploader widget to allow users to upload images
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

label_dict = {
    0: 'Darier_s disease',
    1: 'Muehrck-e_s lines',
    2: 'aloperia areata',
    3: 'beau_s lines',
    4: 'bluish nail',
    5: 'clubbing',
    6: 'eczema',
    7: 'half and half nailes (Lindsay_s nails)',
    8: 'koilonychia',
    9: 'leukonychia',
    10: 'onycholycis',
    11: 'pale nail',
    12: 'red lunula',
    13: 'splinter hemmorrage',
    14: 'terry_s nail',
    15: 'white nail',
    16: 'yellow nails'
}

if uploaded_file is not None:
    # Perform image classification using your classification model
    image = Image.open(uploaded_file)
    image = image.resize((224, 224))  # Resize the image to match the input size of your model
    image = image.convert("RGB")
    # Convert the image to a NumPy array and normalize it
    image = np.array(image) / 255.0

    # Reshape the image to match the input shape expected by your model
    image = np.expand_dims(image, axis=0)

    classification_result = model.predict([image])
    result = label_dict[np.argmax(classification_result)]
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", width=250)

    # Display classification result
    st.header(":red[Classification Result:]")
    st.header(result)

    # Display prevention steps
    if result in disease_info:
        st.header(":green[Prevention Steps:]")
        for step in disease_info[result]['prevention']:
            st.write(step)
    else:
        st.warning("Prevention steps information not available for this disease.")

    st.markdown("It is recommended to consult with a healthcare professional for further evaluation and diagnosis.")
