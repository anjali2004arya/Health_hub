# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:39:10 2024

@author: akhil
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from PIL import Image
import altair as alt

def login():
    st.subheader("Login")
    

    # Hardcoded username and password (you might want to use a more secure authentication method)
    correct_username = "user"
    correct_password = "password"
   


    # Input fields for username and password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Login button
    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Login successful!")
            st.session_state.is_logged_in = True
        else:
            st.error("Invalid username or password")

# Check if the user is logged in
if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False

# If not logged in, show the login page
if not st.session_state.is_logged_in:
    login()
else:
    # Sidebar with different options accessible once logged in
    image = Image.open("C:/Streamlit_Hack/health_hub.png")

    # Display the image using st.image
    st.image(image, use_column_width=True)
   
    diabetes_model = pickle.load(open('C://Streamlit_Hack//saved models//diabetes_model.sav', 'rb'))

    heart_disease_model = pickle.load(open('C://Streamlit_Hack//saved models//heart_disease_model.sav','rb'))

    parkinsons_model = pickle.load(open('C://Streamlit_Hack//saved models//parkinsons_model.sav', 'rb'))



    # sidebar for navigation
    with st.sidebar:
        
        selected = option_menu('Welcome to Health Hub',
                              
                              ['Unhealthy Lifestyle',
                               'Common diseases in India',
                               'Healthcare Centres',
                               'Diabetes Prediction',
                               'Heart Disease Prediction',
                               'Parkinsons Prediction',
                               'Health and Essential Amenities'],
                              icons=['activity','person','person','activity','heart','person','heart'],
                              default_index=0)
        
        
    # Diabetes Prediction Page
    if (selected == 'Diabetes Prediction'):
        
        # page title
        st.title('Diabetes Prediction using ML')
        
        
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
            
        with col2:
            Glucose = st.text_input('Glucose Level')
        
        with col3:
            BloodPressure = st.text_input('Blood Pressure value')
        
        with col1:
            SkinThickness = st.text_input('Skin Thickness value')
        
        with col2:
            Insulin = st.text_input('Insulin Level')
        
        with col3:
            BMI = st.text_input('BMI value')
        
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
        with col2:
            Age = st.text_input('Age of the Person')
        
        
        # code for Prediction
        diab_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
              diab_diagnosis = '''Remember, individual dietary needs vary, and it is crucial to monitor blood sugar levels, consult with a healthcare professional, and adjust the plan accordingly.'''
              
              image = Image.open("C:/Streamlit_Hack/diabetes_1.jpg")

              # Display the image using st.image
              st.image(image, caption='Diet Chart', use_column_width=True)
              
              #diet plan
              st.write("You are Diabetic")
              st.write("But don't worry ,we have the proper dietary plan for you ")
              st.write("Diabetes-Friendly Diet Plan:")
              st.write("Breakfast:")
              st.write("1.Scrambled eggs with spinach and tomatoes")
              st.write("2.Whole-grain toast")
              st.write("3.Berries [blueberries, strawberries]")
              st.write("Lunch:")
              st.write("1.Grilled chicken breast")
              st.write("2.Quinoa or brown rice")
              st.write("3.Steamed broccoli and carrots")
              st.write("4.Salad with leafy greens and vinaigrette dressing")
              st.write("Snack:")
              st.write("1.Greek yogurt with a handful of almonds")
              st.write("Dinner:")
              st.write("1.Baked salmon")
              st.write("2.Roasted sweet potatoes")
              st.write("3.Asparagus or green beans")
              st.write("Note: General Tips for a Diabetes-Friendly Diet:")
              st.write("1.Control Portion Sizes: Pay attention to portion sizes to manage blood sugar levels effectively.")
              st.write("2.Choose Whole Grains: Opt for whole grains like brown rice, quinoa, and whole wheat bread over refined grains.")
              st.write("3.Lean Protein Sources: Include lean proteins such as poultry, fish, tofu, and legumes.")
              st.write("4.Fruits and Vegetables: Incorporate a variety of colorful fruits and vegetables for fiber and essential nutrients.")
              st.write("5.Healthy Fats: Include sources of healthy fats, such as avocados, nuts, and olive oil, in moderation.")
              
              
              
              
              
            else:
              diab_diagnosis = 'The person is not diabetic'
              image = Image.open("C:/Streamlit_Hack/diabetes.jpeg")

              # Display the image using st.image
              st.image(image, caption='Welcome to Health Hub', use_column_width=True)
            
        st.success(diab_diagnosis)




    # Heart Disease Prediction Page
    if (selected == 'Heart Disease Prediction'):
        
        # page title
        st.title('Heart Disease Prediction using ML')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.text_input('Age')
            
        with col2:
            sex = st.text_input('Sex')
            
        with col3:
            cp = st.text_input('Chest Pain types')
            
        with col1:
            trestbps = st.text_input('Resting Blood Pressure')
            
        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')
            
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
            
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')
            
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')
            
        with col3:
            exang = st.text_input('Exercise Induced Angina')
            
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')
            
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
            
        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')
            
        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
            
            
         
         
        # code for Prediction
        heart_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
            
            if (heart_prediction[0] == 1):
              heart_diagnosis = 'The person is having heart disease'
            else:
              heart_diagnosis = 'The person does not have any heart disease'
            
        st.success(heart_diagnosis)
            
        
        

    # Parkinson's Prediction Page
    if (selected == "Parkinsons Prediction"):
        
        # page title
        st.title("Parkinson's Disease Prediction using ML")
        
        col1, col2, col3, col4, col5 = st.columns(5)  
        
        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')
            
        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')
            
        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')
            
        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')
            
        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
            
        with col1:
            RAP = st.text_input('MDVP:RAP')
            
        with col2:
            PPQ = st.text_input('MDVP:PPQ')
            
        with col3:
            DDP = st.text_input('Jitter:DDP')
            
        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')
            
        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
            
        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')
            
        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')
            
        with col3:
            APQ = st.text_input('MDVP:APQ')
            
        with col4:
            DDA = st.text_input('Shimmer:DDA')
            
        with col5:
            NHR = st.text_input('NHR')
            
        with col1:
            HNR = st.text_input('HNR')
            
        with col2:
            RPDE = st.text_input('RPDE')
            
        with col3:
            DFA = st.text_input('DFA')
            
        with col4:
            spread1 = st.text_input('spread1')
            
        with col5:
            spread2 = st.text_input('spread2')
            
        with col1:
            D2 = st.text_input('D2')
            
        with col2:
            PPE = st.text_input('PPE')
            
        
        
        # code for Prediction
        parkinsons_diagnosis = ''
        
        # creating a button for Prediction    
        if st.button("Parkinson's Test Result"):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            if (parkinsons_prediction[0] == 1):
              parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
              parkinsons_diagnosis = "The person does not have Parkinson's disease"
            
        st.success(parkinsons_diagnosis)
        
    #statistics code
    if (selected == "Unhealthy Lifestyle"):
        # Load data from the CSV file
        data = pd.read_csv("C://Streamlit_Hack//Habits.csv")

        # Create a Streamlit app
        st.markdown(f"<h1 style='text-decoration: underline;'>Unhealthy Lifestyle </h1>", unsafe_allow_html=True)

        # Display the raw data
        st.subheader("Statistics")
        st.write(data)

        # Sidebar for filtering data
        st.sidebar.header("Filter Data")
        selected_state = st.sidebar.selectbox("Select State:", data['States'].unique())
        filtered_data = data[data['States'] == selected_state]

        # Show data for the selected state
        st.subheader(f"Smoking Habits in {selected_state}")
        st.write(filtered_data[['Districts', 'Personal Habits (age 15 years and above) (%) - Men who use any kind of smokeless tobacco', 'Personal Habits (age 15 years and above) (%) - Women who use any kind of smokeless tobacco']])

        # Plotting using Plotly Express
        fig = px.bar(filtered_data, x='Districts', y=['Personal Habits (age 15 years and above) (%) - Men who use any kind of smokeless tobacco', 'Personal Habits (age 15 years and above) (%) - Women who use any kind of smokeless tobacco'],
                     labels={'value': 'Percentage'},
                     title=f"Smoking Habits in {selected_state} - Men vs Women")
        fig.update_layout(barmode='group')
        st.plotly_chart(fig)

        #code for pie chart 
        st.subheader("Visualizations of Alcohol Habits")
        st.write(filtered_data[['Districts', 'Personal Habits (age 15 years and above) (%) - Men who consume alcohol', 'Personal Habits (age 15 years and above) (%) - Women who consume alcohol']])
        fig_pie = px.bar(filtered_data,x='Districts', y=['Personal Habits (age 15 years and above) (%) - Men who consume alcohol', 'Personal Habits (age 15 years and above) (%) - Women who consume alcohol'],
                        labels={'value':'Percentage'},
                        title=f"Distribution of Alcohol Habits in {selected_state}")
        fig_pie.update_layout(barmode='group')
        st.plotly_chart(fig_pie)
        
    if (selected == 'Healthcare Centres'):
         df = pd.read_csv("C://Streamlit_Hack//PHC_data.csv",encoding="latin1")

         # Sidebar for user input
         st.sidebar.header("PHC-Primary Healthcare Centre ")
         st.sidebar.header("HWC-Health and Wellness Centres")
         selected_disease = st.sidebar.selectbox("Choose the required field", ["PHCs and HWC-PHCs - In Position - P","PHCs and HWC-PHCs - Required - R","PHCs and HWC-PHCs - Shortfall - S","PHCs and HWC-PHCs - % Shorfall"])

         st.markdown(f"<h1 style='text-decoration: underline;'>Healthcare Centres across India </h1>", unsafe_allow_html=True)

         # Main content
         st.subheader(f"{selected_disease} Cases by State")


         # Bar chart using Altair
         chart = alt.Chart(df).mark_bar().encode(
             x=alt.X("State/UT:N", title="State"),
             y=alt.Y(f"{selected_disease}:Q", title=f"{selected_disease} Cases"),
             color=alt.Color("State/UT:N", legend=None),
         ).properties(width=600, height=400)

         st.altair_chart(chart)

         # Display data table for the selected disease
         st.write(f"{selected_disease} Cases by State")
         selected_disease_data = df[["State/UT", selected_disease]]
         st.write(selected_disease_data)
         
    if (selected == 'Common diseases in India'):
        df = pd.read_csv("C://Streamlit_Hack//common_dis.csv",encoding="latin1")

        # Sidebar for user input
        st.sidebar.header("Select Disease")
        selected_disease = st.sidebar.selectbox("Choose a disease", ["Hypertension or high blood pressure (%)", "Chronic heart diseases (%)","Cardiovascular diseases (CVDs) (%)46","Stroke (%)","Diabetes or high blood sugar (%)","High Cholesterol (%)","Anaemia (%)","Chronic lung diseases (%)47","Asthma (%)","Bone/Joint diseases (%)48","Arthritis (%)","Osteoporosis (%)","Neurological or psychiatric problems (%)49","Depression (%)","Alzheimer’s disease and dementia (%)","Psychiatric problems (%)50","Neurological problems (%)51"])

        st.markdown(f"<h1 style='text-decoration: underline;'>Common diseases across India </h1>", unsafe_allow_html=True)

        # Main content
        st.subheader(f"{selected_disease} Cases by State")


        # Bar chart using Altair
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("Indicators:N", title="State"),
            y=alt.Y(f"{selected_disease}:Q", title=f"{selected_disease} Cases"),
            color=alt.Color("Indicators:N", legend=None),
        ).properties(width=600, height=400)

        st.altair_chart(chart)

        # Display data table for the selected disease
        st.write(f"{selected_disease} Cases by State")
        selected_disease_data = df[["Indicators", selected_disease]]
        st.write(selected_disease_data)
        
    if (selected == 'Health and Essential Amenities'):
        # Load data from the CSV file
        data = pd.read_csv("C://Streamlit_Hack//insurance_data.csv")

        # Create a Streamlit app
        st.markdown(f"<h1 style='text-decoration: underline;'>Enhancing Quality of Life</h1>", unsafe_allow_html=True)
        st.title("Health and Essential Amenities")

        # Sidebar for filtering data
        st.sidebar.header("Filter Data")
        selected_state = st.sidebar.selectbox("Select State:", data['States/UTs'].unique())
        filtered_data = data[data['States/UTs'] == selected_state]

        # Show data for the selected state
        st.subheader(f"Factors that can eradicate Healthcare problems in {selected_state}")
        st.write(filtered_data[['Area', "Population living in households with an improved drinking-water source1 (%)","Population living in households that use an improved sanitation facility2 (%)","Households using clean fuel for cooking3 (%)","Households with any usual member covered under a health insurance/financing scheme (%)"]])

        # Plotting using Plotly Express
        fig = px.bar(filtered_data, x='Area', y=["Population living in households with an improved drinking-water source1 (%)","Population living in households that use an improved sanitation facility2 (%)","Households using clean fuel for cooking3 (%)","Households with any usual member covered under a health insurance/financing scheme (%)"],
                     labels={'value': 'Percentage'},
                     title=f"Health and essential amenities in {selected_state}")
        fig.update_layout(barmode='group')
        st.plotly_chart(fig)
        

         




