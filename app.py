import streamlit as st
import csv

file =  open("places.csv", "r")
reader = csv.DictReader(file)
places = list(reader)
file.close()

st.image("logo.png", width=200)

st.title("🌍 TripMatch AI")
st.write("Welcome to TripMatch AI! Please select your preferences below.")

all_hobbies = ["Beach","Hiking","Food","History","Photography","Surfing","Skiing","Nature","Relaxing","Nightlife","Party","City","Culture","Adventure"]
user_hobbies = st.multiselect("Select your hobbies:", all_hobbies)

user_budget = st.selectbox("Pick your budget:", ["low", "mid", "high"])

if st.button("Find My Destination"):
    results = []
    for place in places:
        score = 0
        matched = []
        for hobby in user_hobbies:
            if place.get(hobby) =="1":
                score += 1
                matched.append(hobby)
        
        if place.get("Budget","") == user_budget:
            score += 2

        results.append({"Name": place["Name"], "Country": place["Country"], "Budget": place["Budget"], "Score": score, "Image": place.get("Image_url", ""),"Description": place.get("Description", ""), "Matched Hobbies": matched})
    results.sort(key=lambda x: x["Score"], reverse=True)

    st.subheader("Top 3 Matches : ")
    for i in range(min(3, len(results))):
        r = results[i]
        st.markdown(f"""
        <div style="border:2px solid #333; border-radius:15px; padding:15px; margin-bottom:20px; background-color:#1a1a2e;">
        <img src="{r['Image']}" style="width:100%; border-radius:10px;">
        <h3 style="color:white; margin:0;">#{i+1} {r['Name']} , {r['Country']}</h3>
        <p style="color:#ccc;">⭐ Score: {r['Score']} | 💰 Budget: {r['Budget']}</p>
        <p style="color:#aaa; font-size:14px;">{r['Description']}</p>
        <p style="color:#888; font-size:14px;">Matched Hobbies: {', '.join(r['Matched Hobbies'])}</p>
        </div>
        """, unsafe_allow_html=True)