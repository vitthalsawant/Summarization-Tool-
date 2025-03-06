import streamlit as st
from summarizer import summarize_text

def main():
    st.title("Summarization Tool")
    text = st.text_area("Enter text to summarize", height=200)
    if st.button("Summarize"):
        if text.strip() == "":
            st.warning("Please enter some text to summarize.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarize_text(text)
                st.subheader("Summary:")
                st.write(summary)

if __name__ == "__main__":
    main()
