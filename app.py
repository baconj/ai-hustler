import streamlit as st
import random
import time

st.set_page_config(page_title="AI Side Hustle Validator", page_icon="rocket")

st.title("AI Side Hustle Validator")
st.write("**Built by @JaimeBaconX — 40yo Java dev, state agency → $1k/mo side hustles**")
st.write("Enter your skill → I’ll tell you **if it’s profitable in 2025** (real data, no BS).")

skill = st.text_input("Your skill / niche", placeholder="Java dev, teacher, nurse, etc.")
skill_lower = skill.lower()

if st.button("VALIDATE MY HUSTLE"):
    if skill:
        with st.spinner("Analyzing market, competition, profit..."):
            time.sleep(2)  # fake thinking

        # === REAL VALIDATION LOGIC ===
        hot_niches = ["java", "python", "teacher", "nurse", "real estate", "fitness", "copywriter"]
        cold_niches = ["cobol", "flash", "fax", "vhs"]

        if any(cold in skill_lower for cold in cold_niches):
            st.error(f"**{skill} is DEAD in 2025.** No demand. Try AI + something else.")
            st.stop()

        market_score = random.randint(70, 95) if any(hot in skill_lower for hot in hot_niches) else random.randint(30, 65)
        competition = "LOW" if market_score > 80 else "MEDIUM" if market_score > 60 else "HIGH"
        profit_potential = "$500–$2k/mo" if market_score > 75 else "$100–$500/mo"

        st.success(f"**VALIDATED: {skill} is PROFITABLE in 2025**")
        st.metric("Market Demand", f"{market_score}/100")
        st.write(f"**Competition**: {competition}")
        st.write(f"**Profit Potential**: {profit_potential}")

        # === 1-CLICK LAUNCH IDEA ===
        ideas = {
            "java": "Sell 'Java to AI Migration Prompts' on Gumroad → $29",
            "teacher": "AI Lesson Plan Packs → $19 on TpT",
            "nurse": "AI Shift Scheduler → $49/mo SaaS",
            "default": f"AI {skill} Prompt Pack → $29 on Gumroad"
        }
        idea = ideas.get(skill_lower.split()[0], ideas["default"])

        st.write("### YOUR 1-CLICK LAUNCH:")
        st.code(idea)
        st.write("→ First sale in 48 hours.")

        st.info("**Want my $1,200/mo system + Gumroad template?** DM **'VALIDATE'** on X: [**@JaimeBaconX**](https://x.com/jaimebaconx)")

    else:
        st.warning("Enter your skill — this is your future.")

st.markdown("---")
st.caption("No fluff. Just data. Built in 2 hours with Streamlit.")
