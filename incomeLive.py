import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

st.set_page_config(
    page_title="Live Income Dashboard",
    page_icon='💵',
    layout='wide',
)

st.title('Live Income Data Monitoring App')

# Load the dataset
df = pd.read_csv('incomeData.csv')

# Create a select box for choosing a job
job_filter = st.selectbox('Choose a job', df['occupation'].unique(), index=5)

# Filter the data based on the selected job
df = df[df['occupation'] == job_filter]

# Create an empty placeholder for real-time updates
placeholder = st.empty()

# Real-time update loop
while True:
    # Generate random multipliers for age and hours per week
    age_multiplier = np.random.uniform(0.5, 1.5, size=len(df))
    hpw_multiplier = np.random.uniform(0.5, 1.5, size=len(df))

    df['new_age'] = df['age'] * age_multiplier
    df['whpw_new'] = df['hours.per.week'] * hpw_multiplier

    avg_age = np.mean(df['new_age'])
    count_married = int(df[df['marital.status'] == 'married-civ-spouse'].shape[0] + np.random.randint(1, 30))
    hpw = np.mean(df['whpw_new'])

    # Update the placeholder with the real-time data
    with placeholder.container():
        kpi1, kpi2, kpi3 = st.columns(3)

        kpi1.metric(label='Average Age', value=round(avg_age), delta=0)
        kpi2.metric(label='Married Count 💍', value=int(round(count_married)), delta=0)
        kpi3.metric(label='Average Hours/Week', value=round(hpw), delta=0)

        figcol1, figcol2 = st.columns(2)
        with figcol1:
            st.markdown('### Age vs Marital Status')
            fig = px.scatter(data_frame=df, x='new_age', y='marital.status',
                             labels={'new_age': 'Age', 'marital.status': 'Marital Status'})
            st.plotly_chart(fig)
        with figcol2:
            st.markdown('### Age Distribution')
            fig2 = px.histogram(data_frame=df, x='new_age', nbins=20, labels={'new_age': 'Age', 'count': 'Count'})
            st.plotly_chart(fig2)

        st.markdown('### Data View As Selection')
        st.write(df)
        time.sleep(1)
