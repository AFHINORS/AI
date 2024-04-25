
st.title('Powered By Shayan Farahani')

inp = st.text_area('معلم گرامی سوال خود را ذکر کنید')

ok = st.button('بزن بریم')

if inp != "" and ok:
    response =g4f.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": inp}],
        stream=True

    )

    for message in response:
        m = "".join(message)
        st.write(m)
