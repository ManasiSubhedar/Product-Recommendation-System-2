import streamlit as st
import sklearn
import spacy
import re
import joblib

vectorizer = joblib.load("tfidf.pkl")
similarity = joblib.load("similarity.pkl")
df = joblib.load("products.pkl")

def recommend(item,n_top=5):
    idx=df[df['Name']==item].index[0]
    distances=similarity[idx]

    product_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:n_top+1]
    recommendations=[]
    for i in product_list:
        recommendations.append(df.iloc[i[0]]['Name'])
    return recommendations

st.title("Product Recommendation System")

selected_product = st.selectbox(
    "Select a Product",
    df["Name"]
)

if st.button("Recommend"):
    recommendations = recommend(selected_product)

    st.subheader("Recommended Products")
    for product in recommendations:
        st.write(product)