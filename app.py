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

        job_lower = job.lower()
        pain_lower = pain.lower()

        # Clean ideas (no ** in strings)
        ideas = [
            f"AI {job} Resume Roaster - Turn resume into $500 gig",
            f"{job} to Python/JS Converter - Charge $50 per job",
            f"AI {job} Side Hustle Name Generator - Sell for $29",
            f"Sell {job}-Specific Prompt Packs - $29 on Gumroad = $1k/mo",
            f"NEPQ DM Closer for {job}s - 'What if you stay stuck?'"
        ]

        # Personalize by job
        if any(k in job_lower for k in ["java", "dev", "programmer"]):
            ideas[0] = "Java-to-AI Consultant - Help migrate with AI"
            ideas[1] = "Spring Boot to AI API Wrapper - Sell for $99"
        elif any(k in job_lower for k in ["teacher", "educator"]):
            ideas[0] = "AI Lesson Plan Generator - $19 per teacher"
            ideas[1] = "Quiz Maker Pro - $49 per school"
        elif any(k in job_lower for k in ["market", "sales"]):
            ideas[0] = "AI Cold Email Writer - $99 per campaign"
            ideas[1] = "LinkedIn Post Generator - $29/mo"

        # Bonus by pain
        if "time" in pain_lower:
            ideas.append("BONUS: 2-Hour AI Workflow - Do it tonight")
        if "idea" in pain_lower:
            ideas.append("BONUS: 50 Viral Idea Prompts - Copy-paste")

        # Show 5 ideas
        selected = random.sample(ideas[:5], 5)
        for i, idea in enumerate(selected, 1):
            title, desc = idea.split(" - ", 1) if " - " in idea else (idea, "")
            st.write(f"### {i}. **{title}**")
            if desc:
                st.write(f"   {desc}")
            prompt = f"Prompt: '{title.strip()}' for a {job} with '{pain}'"
            st.code(prompt)

        # Your handle here
        st.info("Want my **$1,200/mo affiliate system + bonus prompts**? DM **'HUSTLE'** on X: [**@JaimeBaconX**](https://x.com/jaimebaconx)")

    else:
        st.warning("Fill all 3 — this is *your* future.")

st.markdown("---")
st.caption("Built by @JaimeBaconX — 40yo Java dev who was stuck. Now shipping.")
