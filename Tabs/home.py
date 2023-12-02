"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Star Category Detection")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Star type categorization involves classifying stars based on their characteristics like temperature, size, and brightness. Random Forest Regression, a machine learning algorithm, can be used for this. It operates by constructing multiple decision trees during training and outputs the mode of the classes or mean prediction of the individual trees. To categorize star types, data on various features like luminosity, temperature, radius, and spectral class are collected and used to train the Random Forest Regression model. The algorithm learns patterns within the data to predict the star types based on these features. By considering the multitude of decision trees and their collective predictions, it offers more accurate classifications compared to individual decision trees. This method allows astronomers to efficiently categorize stars into their respective types, aiding in astronomical research and understanding the universe's stellar composition.
        </p>
    """, unsafe_allow_html=True)