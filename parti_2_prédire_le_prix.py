import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import Ridge

st.title("Estimation du prix d'une maison à Seattel" )
st.header("Entrez les informations") 

bedrooms = st.number_input("Number of bedrooms",value=1)
bathrooms=st.number_input("Number of bathrooms ",value=1)
sqft_living=st.number_input("Square footage of the apartment interior living space(sqft)",value=20)
sqft_lot=st.number_input("square footage of the land apace(sqft)",value=0)
floors=st.number_input("Number of floors",value=0)
waterfront = st.radio("The apartment is overlooking the waterfront: ", ('yes', 'no'), ) 
  
view =st.selectbox("How many good  view have the property",[1,2,3,4],index = 0)
condition=st.selectbox("Contition of the apartment",[1,2,3,4,5],index = 3)

grade= st.slider("From 1 to 13,where 1-3 falls short of building construction and design, 7 has an average level of construiction and design, and 11-13 have a higt quality level of construction and design ", 1, 13,value=8)

sqft_above=st.number_input("The square footage of the interior housing space that is above ground level(sqft)",value=10)

sqft_basement=st.number_input("The square footage of the interior housing space that is below ground level(sqft)",value=0)

yr_built=st.text_input("The year the house was built",value="1900")
yr_renovated = st.text_input("The year the house's last renovation",value="0")
zipcode=st.text_input("What zipcode area the house is in",value="98125")
month= st.text_input("the month of acquisition",value="02")


pickle_in = open('my_pipe_ridge.pkl', 'rb') 
my_pipe_ridge = pickle.load(pickle_in) 

if waterfront=="yes":
    waterfront=1
else:
    waterfront=0

donnee =np.array([[bedrooms, bathrooms, sqft_living, sqft_lot,floors, waterfront, view, condition, grade, sqft_above,sqft_basement, yr_built, yr_renovated, zipcode, month]])
df_X=pd.DataFrame(donnee,columns=["bedrooms", "bathrooms", "sqft_living", "sqft_lot","floors", "waterfront", "view", "condition", "grade", "sqft_above","sqft_basement", "yr_built", "yr_renovated", "zipcode", "month"])

if(st.button('Calculate the price')): 
    prediction = my_pipe_ridge.predict(df_X)
    st.text("The prediction price{}.".format(prediction))



"""
streamlit run parti_2_prédire_le_prix.py
"""