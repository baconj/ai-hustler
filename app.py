import streamlit as st

st.set_page_config(page_title="AI Prompt Hustler", page_icon="rocket")

st.title("AI Prompt Hustler")
st.write("**40yo Java dev built this in 2 hours. No $249 tools. Just results.**")
st.write("Answer 3 questions → Get 5 AI side hustles that make **$100 this weekend**")

name = st.text_input("Your name (or 'Anon')", placeholder="Billy")
job = st.text_input("Your job", placeholder="Java dev, state worker, etc.")
pain = st.text_input("Biggest frustration?", placeholder="No time, no ideas, stuck")

if st.button("Generate My $1k/mo Plan"):
    if name and job and pain:
        st.success(f"Here’s your plan, **{name}**!")
        st.balloons()

        st.write("### 1. AI Resume Roaster")
        st.code("Prompt: 'Roast this Java resume → turn it into a $500 freelance gig'")

        st.write("### 2. Java-to-Python Converter")
        st.code("Prompt: 'Convert this Java method to clean Python + tests'")

        st.write("### 3. AI Side Hustle Name Generator")
        st.code("Prompt: '10 viral names for a Java dev AI tool'")

        st.write("### 4. Sell Prompt Packs on Gumroad")
        st.code("$29/pop → $1k/mo in 30 days")

        st.write("### 5. NEPQ DM Closer")
        st.code("DM: 'What happens if you stay stuck another year?'")

        st.info("**Want my $1,200/mo affiliate system?** Reply **'HUSTLE'** on my X post!")
    else:
        st.warning("Fill all 3 — this is your future.")

st.markdown("---")
st.caption("Built by a 40yo Java dev who was stuck like you. Now shipping. [X: @JaimeBaconX]")