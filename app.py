import streamlit as st
import random

st.set_page_config(page_title="AI Prompt Hustler", page_icon="rocket")

st.title("AI Prompt Hustler")
st.write("**No $249 tools. No BS. Just results.**")
st.write("Answer 3 questions → Get **5 personalized** AI side hustles that make **$100 this weekend**")

name = st.text_input("Your name (or 'Anon')", placeholder="Roman")
job = st.text_input("Your job / skill", placeholder="Java dev, teacher, marketer, etc.")
pain = st.text_input("Biggest frustration?", placeholder="no time, no ideas, no clients")

if st.button("Generate My $1k/mo Plan"):
    if name and job and pain:
        st.success(f"Here’s your **personalized** plan, **{name}**!")
        st.balloons()

        # === DYNAMIC PROMPTS BASED ON INPUT ===
        job_lower = job.lower()

        # Base templates
        ideas = [
            f"**AI {job} Resume Roaster** → Turn your resume into a $500 freelance gig",
            f"**{job} to Python/JS Converter** → Charge $50 per conversion",
            f"**AI {job} Side Hustle Name Generator** → Sell names for $29 each",
            f"**Sell {job}-Specific Prompt Packs** → $29 on Gumroad → $1k/mo",
            f"**NEPQ DM Closer for {job}s** → 'What happens if you stay stuck?'"
        ]

        # Personalize based on job
        if "java" in job_lower or "dev" in job_lower or "programmer" in job_lower:
            ideas[0] = f"**Java-to-AI Consultant** → Help companies migrate with AI"
            ideas[1] = f"**Spring Boot → AI API Wrapper** → Sell for $99"
        elif "teacher" in job_lower or "educator" in job_lower:
            ideas[0] = f"**AI Lesson Plan Generator** → Sell to teachers for $19"
            ideas[1] = f"**Quiz Maker Pro** → $49/school"
        elif "market" in job_lower or "sales" in job_lower:
            ideas[0] = f"**AI Cold Email Writer** → $99 per campaign"
            ideas[1] = f"**LinkedIn Post Generator** → $29/mo"

        # Personalize based on pain
        pain_lower = pain.lower()
        if "time" in pain_lower:
            ideas.append("**BONUS: 2-Hour AI Workflow** → Do in 1 evening")
        if "idea" in pain_lower:
            ideas.append("**BONUS: 50 Viral Idea Prompts** → Copy-paste ready")

        # Show 5 random + personalized
        selected = random.sample(ideas[:5], 5)
        for i, idea in enumerate(selected, 1):
            st.write(f"### {i}. {idea}")
            prompt = f"Prompt: '{idea.split('→')[0].strip()} for a {job} with {pain}'"
            st.code(prompt)

        st.info("**Want my $1,200/mo affiliate system + bonus prompts?** DM **'HUSTLE'** on X!")
    else:
        st.warning("Fill all 3 — this is *your* future.")
