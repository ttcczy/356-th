import streamlit as st
st.title("Hello, reader!")
st.header("You need to look.")
st.subheader("story")
st.text("It's interesting.")

st.markdown("this is an image: \n \
            ![](https://img.zcool.cn/community/0114f5561bbea66ac7255b14c1eaea.jpg@1280w_1l_2o_100sh.jpg)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobbies = st.multiselect("Hobbies:",
               ['campus',
                'affection',
                'cliffhang',
                'dark love'])
st.write("You selected: ", hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    