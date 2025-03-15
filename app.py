import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

@st.cache_data
def get_data(user_value):
    data = np.random.randn(100) * user_value
    df = pd.DataFrame({'Value': data})
    return df

# TODO: replace this with any implementation you want to visualize (from current project this semester)
def create_chart(df, user_value):
    fig, ax = plt.subplots()
    ax.plot(df['Value'])
    ax.set_title(f'Chart for user input: {user_value}')
    return fig

def main():
    st.title("Put your title here")
    st.sidebar.header("This is a header")
    user_input = st.sidebar.number_input("Enter a number", value=1.0)
    st.sidebar.info("The data generation function is cached. If you enter the same value, the data loads instantly.")
    if st.sidebar.button("Generate Chart"):
        df = get_data(user_input)
        st.write("### Generated Data Preview")
        st.dataframe(df.head())
        fig = create_chart(df, user_input)
        st.pyplot(fig)
        # Tip: Always use f-strings to format!
        st.write(f"Data was generated with user input: **{user_input}**")

if __name__ == "__main__":
    main()
