import streamlit as st
import random
import time

st.set_page_config(page_title="SocialHub", page_icon="📤")

st.title("SocialHub")
st.markdown("**Post once. Broadcast everywhere. No fluff. $0 forever? Free MVP. Pro: $19/mo or $199 lifetime.**")
st.markdown("*X, LinkedIn, Reddit. IG/TikTok/scheduling in Pro.*")

# === LEAN LOGIN (Session State) ===
if "logins" not in st.session_state:
    st.session_state.logins = {"X": False, "LinkedIn": False, "Reddit": False}

platforms = ["X", "LinkedIn", "Reddit"]
cols = st.columns(3)
for i, plat in enumerate(platforms):
    with cols[i]:
        if st.button(f"🔐 Login {plat}", key=f"login_{plat}"):
            st.session_state.logins[plat] = True
            st.rerun()
        if st.session_state.logins[plat]:
            st.success(f"✅ {plat}")

# === WRITE & POST ===
post_text = st.text_area("Your post (280 chars)", placeholder="Just shipped my lean social tool...", max_chars=280)
st.caption(f"{len(post_text)}/280")

if st.button("🚀 POST TO ALL", type="primary"):
    if post_text and all(st.session_state.logins.values()):
        with st.spinner("Broadcasting..."):
            time.sleep(1.5)  # Simulate
        st.success("✅ Posted to X, LinkedIn, Reddit!")
        st.balloons()
        
        # === MINIMAL "ANALYTICS" (No Fluff) ===
        st.markdown("**Quick Stats:**")
        col1, col2, col3 = st.columns(3)
        col1.metric("X Views", random.randint(50, 500))
        col2.metric("LinkedIn Likes", random.randint(5, 50))
        col3.metric("Reddit Votes", random.randint(3, 30))
        
        st.info("**Pro ($19/mo or $199 LT)**: Real APIs, IG/TikTok, scheduling, unlimited. [Buy Now](https://gumroad.com/your-link)")
    else:
        if len(post_text) > 280:
            st.error("Too long — trim it.")
        elif not all(st.session_state.logins.values()):
            st.warning("Login to all 3 first.")
        else:
            st.warning("Write something!")

st.markdown("---")
st.caption("Built lean by @JaimeBaconX. No data stored. Ships fast.")