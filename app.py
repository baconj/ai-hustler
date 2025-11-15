import streamlit as st
import random

st.set_page_config(page_title="AI Hustle Name Generator", page_icon="rocket")

st.title("AI Hustle Name Generator")
st.write("**Built by a 40yo Java dev in 2 hours. No $249 tools. Just results.**")
st.write("Enter your skill → Get **5 viral AI side hustle names** you can launch **TODAY**.")

skill = st.text_input("Your skill / job", placeholder="Java dev, teacher, marketer, etc.")

if st.button("Generate My Hustle Names"):
    if skill:
        st.success(f"Here are your **5 AI-powered hustle names** for a **{skill}**:")
        st.balloons()

        # === CURATED NAME TEMPLATES ===
        bases = [
            f"{skill}AI", f"{skill}Brew", f"{skill}Hustle", f"{skill}SideGig",
            f"AI{skill}", f"{skill}Caffeine", f"{skill}Script", f"{skill}Flow",
            f"{skill}Pulse", f"{skill}Forge", f"{skill}Spark", f"{skill}Nova"
        ]

        # Add flavor
        flavors = ["Pro", "Lab", "Hub", "Bot", "Gen", "X", "Max", "Core"]
        names = []
        for _ in range(5):
            base = random.choice(bases)
            flavor = random.choice(flavors)
            name = f"{base}{flavor}"
            if len(name) > 15:
                name = base  # keep short
            if name not in names:
                names.append(name)

        # Display clean
        for i, name in enumerate(names, 1):
            st.write(f"### {i}. **{name}**")
            st.code(f"Domain: {name.lower()}.com\nIdea: AI tool for {skill}s")

        st.info("Want my **$1,200/mo affiliate system + 50 bonus names**? DM **'NAME'** on X: [**@JaimeBaconX**](https://x.com/jaimebaconx)")

    else:
        st.warning("Enter your skill — this is *your* brand.")

st.markdown("---")
st.caption("Built by @JaimeBaconX — from state agency to side hustle. Shipping daily.")
