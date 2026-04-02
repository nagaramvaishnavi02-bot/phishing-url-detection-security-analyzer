import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.title("🛡️ Phishing URL Detection & Security Analyzer")


url = st.text_input("Enter a URL to check")


def check_url(url):
    score = 0
    features = {}

   
    features["Uses HTTPS"] = "https" in url
    if "https" not in url:
        score += 1


    features["Length"] = len(url)
    if len(url) > 50:
        score += 1

    
    features["Contains @"] = "@" in url
    if "@" in url:
        score += 1

    
    features["Contains -"] = "-" in url
    if "-" in url:
        score += 1

    return score, features


if st.button("Check URL"):
    if url:
        score, features = check_url(url)

        
        if score == 0:
            st.success("✅ Safe")
        elif score <= 2:
            st.warning("⚠️ Suspicious")
        else:
            st.error("❌ Phishing")

        
        st.subheader("🔍 URL Features")
        st.write(features)

       
        st.subheader("📊 Security Score Visualization")
        fig, ax = plt.subplots()
        values = [int(v) if isinstance(v, bool) else v for v in features.values()]
        ax.bar(features.keys(), values, color="skyblue")
        plt.xticks(rotation=45)
        plt.ylabel("Feature Value")
        st.pyplot(fig)

    else:
        st.warning("Please enter a URL")