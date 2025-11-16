import streamlit as st
import random
import time

st.set_page_config(page_title="SocialHub", page_icon="megaphone")

st.title("SocialHub")
st.write("**Post to X, LinkedIn, Reddit — all at once. Built by @JaimeBaconX.**")
st.write("Log in → write once → broadcast everywhere.")

# === FAKE LOGINS (MVP) ===
platforms = ["X (Twitter)", "LinkedIn", "Reddit"]
logged_in = st.session_state.get("logged_in", {p: False for p in platforms})

cols = st.columns(len(platforms))
for i, platform in enumerate(platforms):
    with cols[i]:
        if not logged_in[platform]:
            if st.button(f"Login to {platform}"):
                st.session_state.logged_in[platform] = True
                st.rerun()
        else:
            st.success(f"✓ {platform}")

# === POST COMPOSER ===
post = st.text_area("Your post (280 chars max)", placeholder="Just shipped my AI market tool...", height=100)
char_count = len(post)
st.write(f"{char_count}/280")

if st.button("POST TO ALL"):
    if post and char_count <= 280 and all(logged_in.values()):
        with st.spinner("Posting..."):
            time.sleep(2)
        st.success("Posted to X, LinkedIn, Reddit!")
        st.balloons()
        
        # === FAKE ANALYTICS ===
        st.subheader("Post Analytics")
        col1, col2, col3 = st.columns(3)
        col1.metric("X Impressions", random.randint(100, 1000))
        col2.metric("LinkedIn Reactions", random.randint(10, 100))
        col3.metric("Reddit Upvotes", random.randint(5, 50))
        
        st.info("**Want IG, TikTok, scheduling, AI rewrite?** DM **'HUB'** on X: [**@JaimeBaconX**](https://x.com/jaimebaconx)")

    elif char_count > 280:
        st.error("Post too long!")
    elif not all(logged_in.values()):
        st.warning("Log in to all platforms first.")
    else:
        st.warning("Write a post!")

st.markdown("---")
st.caption("MVP: Free. Pro with 5+ platforms + AI coming soon. No data stored.")