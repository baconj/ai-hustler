import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import random
import time

st.set_page_config(page_title="AI Side Hustle Validator", page_icon="chart_with_upwards_trend")

st.title("AI Side Hustle Validator")
st.write("**Real Google Trends data. No BS. Built by @JaimeBaconX.**")
st.write("Enter your skill/niche → Get **actual demand**, profit estimate, and **proven launch ideas**.")

skill = st.text_input("Your skill / niche", placeholder="Java dev, teacher, nurse, etc.")
skill_lower = skill.lower().strip()

# === PROVEN LAUNCH IDEAS & FIRST SALE TIPS ===
launch_ideas = [
    "Sell prompt packs on Gumroad → $29",
    "Offer 1:1 AI consulting on Upwork → $99/hr",
    "Build a Notion template → $19 on Gumroad",
    "Create a YouTube tutorial series → monetize with affiliates",
    "Launch a 7-day email challenge → $49",
    "Sell Canva AI templates → $15 on Etsy",
    "Start a paid Discord community → $9/mo",
    "Offer AI resume reviews → $49 on Fiverr",
    "Build a Chrome extension → $29 one-time",
    "Create AI-generated stock photos → $5 on Creative Fabrica"
]

first_sale_tips = [
    "Post in 3 Reddit communities with your Gumroad link",
    "DM 10 people on X who complained about your niche",
    "Offer a free sample → upsell the full pack",
    "Run a 24-hour 50% off launch on X",
    "Cross-post to Indie Hackers + Product",
    "Send to your email list (even if it’s 10 people)",
    "Tag 5 influencers in your launch tweet",
    "Offer a bonus for first 5 buyers",
    "Post a Loom walkthrough of your product",
    "Join a launch thread on X (like @ThePeterMick)"
]

if st.button("VALIDATE WITH GOOGLE TRENDS"):
    if skill:
        with st.spinner("Pulling real Google Trends data..."):
            try:
                pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))
                pytrends.build_payload([skill], cat=0, timeframe='today 12-m', geo='US', gprop='')
                df = pytrends.interest_over_time()
                
                if df.empty or skill not in df.columns:
                    st.error(f"**No search data for '{skill}' in US.** Try 'Java programming' or 'AI teacher tools'.")
                    st.stop()
                
                interest = df[skill]
                avg_interest = round(interest.mean())
                
                # === DYNAMIC PROFIT BASED ON DEMAND ===
                if avg_interest < 20:
                    st.error(f"**{skill}: LOW DEMAND ({avg_interest}/100)**")
                    profit = "Skip it. No money here."
                elif avg_interest < 50:
                    st.warning(f"**{skill}: MEDIUM DEMAND ({avg_interest}/100)**")
                    profit = "$100–$500/mo with strong marketing"
                elif avg_interest < 75:
                    st.success(f"**{skill}: GOOD DEMAND ({avg_interest}/100)**")
                    profit = "$500–$2,000/mo"
                else:
                    st.success(f"**{skill}: HIGH DEMAND ({avg_interest}/100)** 🚀")
                    profit = "$1,000–$5,000+/mo"

                st.metric("Estimated Monthly Profit", profit)
                st.subheader("Search Interest (Google Trends - 12 Months)")
                st.line_chart(interest)

                # === RANDOM PROVEN LAUNCH IDEA ===
                st.subheader("Your Proven Launch Idea")
                idea = random.choice(launch_ideas)
                st.code(idea)

                # === RANDOM FIRST SALE TIP ===
                st.subheader("Your First $100 in 48 Hours")
                tip = random.choice(first_sale_tips)
                st.write(f"→ **{tip}**")

                st.info("**Want my $1,200/mo Gumroad system + 50 launch templates?** DM **'VALIDATE'** on X: [**@JaimeBaconX**](https://x.com/jaimebaconx)")

            except Exception as e:
                st.error(f"Trends error. Try a broader term. ({str(e)})")
    else:
        st.warning("Enter a niche — let’s validate it.")

st.markdown("---")
st.caption("Data from Google Trends (Nov 2025). Built in 2 hours with Streamlit + pytrends.")
