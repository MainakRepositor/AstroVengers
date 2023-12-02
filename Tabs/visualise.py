"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
'''from sklearn.metrics import plot_confusion_matrix'''
from sklearn import tree
import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise the Stress Level")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize = (10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()                             # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)                    # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot(fig)

    
    if st.checkbox("Display Boxplot"):
        fig, ax = plt.subplots(figsize=(15,5))
        df.boxplot(["RA_ICRS","DE_ICRS","Plx","PM","pmRA","pmDE"],ax=ax)
        st.pyplot()

    if st.checkbox("Show Sample Results"):
        A = (df['SpType_ELS'] == 1).sum()
        B = (df['SpType_ELS'] == 2).sum()
        F = (df['SpType_ELS'] == 3).sum()
        G = (df['SpType_ELS'] == 4).sum()
        K = (df['SpType_ELS'] == 5).sum()
        M = (df['SpType_ELS'] == 6).sum()
        O = (df['SpType_ELS'] == 7).sum()
        data = [A,B,F,G,K,M,O]
        labels = ['A', 'B','F','G','K','M','O']
        colors = sns.color_palette('pastel')[0:7]
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
        st.pyplot()

    

    
    
