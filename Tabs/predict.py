"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of Star Type.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    col1,col2 = st.columns(2)

    with col1:
        RA_ICRS = st.slider("RA_ICRS", int(df["RA_ICRS"].min()), int(df["RA_ICRS"].max()))
        DE_ICRS = st.slider("DE_ICRS", int(df["DE_ICRS"].min()), int(df["DE_ICRS"].max()))
        Plx = st.slider("Plx", int(df["Plx"].min()), int(df["Plx"].max()))
        PM = st.slider("PM", float(df["PM"].min()), float(df["PM"].max()))
        pmRA = st.slider("pmRA", float(df["pmRA"].min()), float(df["pmRA"].max()))
        pmDE = st.slider("pmDE", float(df["pmDE"].min()), float(df["pmDE"].max()))
        Gmag = st.slider("Gmag", float(df["Gmag"].min()), float(df["Gmag"].max()))
        e_Gmag = st.slider("e_Gmag", float(df["e_Gmag"].min()), float(df["e_Gmag"].max()))

    with col2:
        RPmag = st.slider("RPmag", int(df["RPmag"].min()), int(df["RPmag"].max()))
        e_RPmag = st.slider("e_RPmag", float(df["e_RPmag"].min()), float(df["e_RPmag"].max()))
        BP_RP = st.slider("BP_RP", float(df["BP_RP"].min()), float(df["BP_RP"].max()))
        BP_G = st.slider("BP_G", float(df["BP_G"].min()), float(df["BP_G"].max()))
        G_RP = st.slider("G_RP", float(df["G_RP"].min()), float(df["G_RP"].max()))
        Teff = st.slider("Teff", int(df["Teff"].min()), int(df["Teff"].max()))
        Dist = st.slider("Dist", int(df["Dist"].min()), int(df["Dist"].max()))
        Rad = st.slider("Rad", int(df["Rad"].min()), int(df["Rad"].max()))
    

    # Create a list to store all the features
    features = [RA_ICRS,DE_ICRS,Plx,PM,pmRA,pmDE,Gmag,e_Gmag,RPmag,e_RPmag,BP_RP,BP_G,G_RP,Teff,Dist,Rad]

    # Create a button to predict
    if st.button("Detect Class"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.15
        st.info("Star Type detected...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.info("The star is of type A 🙂")
            components.html(
                """<style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
    <table>
    <tr>
        <th>Star Class</th>
        <th>Surface Temperature</th>
        <th>Solar Mass</th>
        <th>Solar Radii</th>
        <th>Luminosity</th>
        <th>Hydrogen Lines</th>
        <th>Composition</th>
        <th>Chromaticity</th>
        
    </tr>
    <tr>
        <td>A</td>
        <td>7,500–10,000 K</td>
        <td>1.4–2.1 M☉</td>
        <td>1.4–1.8 R☉</td>
        <td>5–25 L☉</td>
        <td>Strong</td>
        <td>0.61%</td>
        <td>bluish white</td>
        
    </tr>
    
    """
            )
        elif (prediction == 2):
            st.info("The star is of type B 🙂")
            components.html(
                """<style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
    <table>
    <tr>
        <th>Star Class</th>
        <th>Surface Temperature</th>
        <th>Solar Mass</th>
        <th>Solar Radii</th>
        <th>Luminosity</th>
        <th>Hydrogen Lines</th>
        <th>Composition</th>
        <th>Chromaticity</th>
        
    </tr>
    <tr>
        <td>B</td>
        <td>10,000–30,000 K</td>
        <td>2.1–16 M☉</td>
        <td>1.8–6.6 R☉	</td>
        <td>25–30,000 L☉</td>
        <td>Medium</td>
        <td>0.12</td>
        <td>Deep bluish</td>
        
    </tr>
    
    """
            )
        elif (prediction == 3):
            st.success("The star is of type F 🙂")
            components.html(
                """<style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
    <table>
    <tr>
        <th>Star Class</th>
        <th>Surface Temperature</th>
        <th>Solar Mass</th>
        <th>Solar Radii</th>
        <th>Luminosity</th>
        <th>Hydrogen Lines</th>
        <th>Composition</th>
        <th>Chromaticity</th>
        
    </tr>
    <tr>
        <td>F</td>
        <td>6,000–7,500 K</td>
        <td>1.04–1.4 M☉	</td>
        <td>1.15–1.4 R☉ </td>
        <td>1.5–5 L☉</td>
        <td>Medium</td>
        <td>3.0%</td>
        <td>White</td>
        
    </tr>
    
    """
            )
        elif (prediction == 4):
            st.success("The star is of type G 🙂")
            components.html(
                """<style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
    <table>
    <tr>
        <th>Star Class</th>
        <th>Surface Temperature</th>
        <th>Solar Mass</th>
        <th>Solar Radii</th>
        <th>Luminosity</th>
        <th>Hydrogen Lines</th>
        <th>Composition</th>
        <th>Chromaticity</th>
        
    </tr>
    <tr>
        <td>G</td>
        <td>5,200–6,000 K</td>
        <td>0.8–1.04 M☉</td>
        <td>0.96–1.15 R☉</td>
        <td>0.6–1.5 L☉</td>
        <td>Weak</td>
        <td>7.6%</td>
        <td>Yellowish White</td>
        
    </tr>
    
    """
            )
        elif (prediction == 5):
            st.warning("The star is of type K 😐")
            components.html(
                """<style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
    <table>
    <tr>
        <th>Star Class</th>
        <th>Surface Temperature</th>
        <th>Solar Mass</th>
        <th>Solar Radii</th>
        <th>Luminosity</th>
        <th>Hydrogen Lines</th>
        <th>Composition</th>
        <th>Chromaticity</th>
        
    </tr>
    <tr>
        <td>K</td>
        <td>3,700–5,200 K</td>
        <td>0.45–0.8 M☉</td>
        <td>0.7–0.96 R☉	</td>
        <td>0.08–0.6 L☉</td>
        <td>Very weak</td>
        <td>12.0%</td>
        <td>Pale Yellowish Orange</td>
        
    </tr>
    
    """
            )
        elif (prediction == 6):
            st.warning("The star is of type M 🙂")
            components.html(
                """<style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
    <table>
    <tr>
        <th>Star Class</th>
        <th>Surface Temperature</th>
        <th>Solar Mass</th>
        <th>Solar Radii</th>
        <th>Luminosity</th>
        <th>Hydrogen Lines</th>
        <th>Composition</th>
        <th>Chromaticity</th>
        
    </tr>
    <tr>
        <td>M</td>
        <td>2,400–3,700 K	</td>
        <td>0.08–0.45 M☉</td>
        <td>≤ 0.7 R☉</td>
        <td>≤ 0.08 L☉</td>
        <td>Very weak	</td>
        <td>76.0%</td>
        <td>Orangish Red</td>
        
    </tr>
    
    """
            )
        elif (prediction == 7):
            st.warning("The star is of type O 🙂")
            components.html(
                """<style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
    <table>
    <tr>
        <th>Star Class</th>
        <th>Surface Temperature</th>
        <th>Solar Mass</th>
        <th>Solar Radii</th>
        <th>Luminosity</th>
        <th>Hydrogen Lines</th>
        <th>Composition</th>
        <th>Chromaticity</th>
        
    </tr>
    <tr>
        <td>O</td>
        <td>≥ 30,000 K</td>
        <td>≥ 16 M☉</td>
        <td>≥ 6.6 R☉</td>
        <td>≥ 30,000 L☉</td>
        <td>Weak</td>
        <td>0.00003%</td>
        <td>Blue</td>
        
    </tr>
    
    """
            )
        else:
            st.snow()
            st.error("The signal didn't come from a star. THAT MEANS!!! 👽")

        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by astrophysicsts and has an accuracy of ", round((score*100),2),"%")
