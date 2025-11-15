import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import time

st.set_page_config(page_title="AI Side Hustle Validator", page_icon="chart_with_upwards_trend")

st.title("AI Side Hustle Validator")
st.write("**Real Google Trends data. No BS. Built by @JaimeBaconX.**")
st.write("Enter your skill/niche → Get **actual search demand** + profit potential.")

skill = st.text_input("Your skill / niche", placeholder="Java dev, poop on a stick, etc.")
skill_lower = skill.lower().strip()

if st.button("VALIDATE WITH GOOGLE TRENDS"):
    if skill:
        with st.spinner("Pulling real Google Trends data..."):
            try:
                # Real Google Trends API
                pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))
                pytrends.build_payload([skill], cat=0, timeframe='today 12-m', geo='US', gprop='')
                df = pytrends.interest_over_time()
                
                if df.empty or skill not in df.columns:
                    st.error(f"**No search data for '{skill}' in US (last 12 months).** DEAD NICHE. Try 'Java dev AI'.")
                    st.stop()
                
                # Get average interest (0-100 scale)
                interest_series = df[skill]
                avg_interest = interest_series.mean()
                market_score = round(avg_interest)
                
                # Real validation
                if market_score < 20:
                    st.error(f"**{skill}: LOW DEMAND ({market_score}/100).** Skip it.")
                elif market_score < 50:
                    st.warning(f"**{skill}: MEDIUM DEMAND ({market_score}/100).** Niche potential.")
                else:
                    st.success(f"**{skill}: HIGH DEMAND ({market_score}/100).** PROFITABLE! 🚀")

                # Show trends chart
                st.subheader("Search Interest Over 12 Months (Google Trends)")
                st.line_chart(interest_series)

                # Profit estimate (based on score)
                profit = "$100–$500/mo" if market_score < 50 else "$500–$2k/mo" if market_score < 80 else "$1k–$5k+/mo"
                st.metric("Estimated Side Hustle Profit", profit)

                # 1-Click Idea
                ideas = {
                    "java dev": "Sell 'Java AI Migration Prompts' on Gumroad → $29",
                    "teacher": "AI Lesson Plans → $19 on Teachers Pay Teachers",
                    "nurse": "AI Shift Scheduler Tool → $49/mo",
                    "default": f"AI {skill} Prompt Pack → $29 on Gumroad"
                }
                idea = ideas.get(skill_lower, ideas["default"])
                st.subheader("Your 1-Click Launch Idea")
                st.code(idea)
                st.write("→ First sale: 48 hours with NEPQ DMs.")

                st.info("**Want my $1,200/mo Gumroad system + 50 prompts?** DM **'TRENDS'** on X: [**@JaimeBaconX**](https://x.com/jaimebaconx)")

            except Exception as e:
                st.error(f"Trends error (Google hiccup): {str(e)}. Try a broader term like 'Java programming'.")
    else:
        st.warning("Enter a niche — let's validate it.")

st.markdown("---")
st.caption("Powered by Google Trends API. Data as of Nov 2025. Built in 2 hours with Streamlit.")
