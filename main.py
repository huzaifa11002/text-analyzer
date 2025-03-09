import streamlit as st
import modules

st.set_page_config(page_title="Text Analyzer", layout="centered")
st.title("Text Analyzer :mag_right:")


if "text" not in st.session_state:
    st.session_state.text = ""

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False


st.session_state.text = st.text_area("Enter your text here:", height=200)


def analyze_text():
    if st.session_state.text.strip():  
        st.session_state.words = modules.words_counter(st.session_state.text)
        st.session_state.num_chars = modules.char_counter(st.session_state.text)
        st.session_state.vowels = modules.vowels_counter(st.session_state.text)
        st.session_state.title_case = modules.title_case(st.session_state.text)
        st.session_state.lower_case = modules.lower_case(st.session_state.text)
        st.session_state.upper_case = modules.upper_case(st.session_state.text)
        st.session_state.analyzed = True 
    else:
        st.error("Please enter some text to analyze!")


if st.button("Analyze", key="analyze"):
    analyze_text()


if st.session_state.analyzed:
    st.subheader("Text Analysis :bar_chart:")
    st.write(f"**Number of Words:** {st.session_state.words}")
    st.write(f"**Number of Characters:** {st.session_state.num_chars}")
    st.write(f"**Number of Vowels:** {st.session_state.vowels}")
    st.subheader("Text Case :abc:")
    st.write(f"**Title Case:** {st.session_state.title_case}")
    st.write(f"**Lower Case:** {st.session_state.lower_case}")
    st.write(f"**Upper Case:** {st.session_state.upper_case}")

    col1,col2 = st.columns(2)
    with col1:
        find_val = st.text_input("Enter the value to find:")
    with col2:
        replace_val = st.text_input("Enter the value to replace with:")


    if st.button("Replace", key="replace"):
        updated_text = st.session_state.text.replace(find_val, replace_val)
        st.session_state.text = updated_text
        st.success("Text updated successfully!")
        st.text_area("Updated Text:", st.session_state.text, height=200)
