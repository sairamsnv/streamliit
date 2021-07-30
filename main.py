import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(page_title="Inventory Analytics", page_icon=":sunglasses:", initial_sidebar_state='expanded')
st.title("INVENTORY AND SALES ANALYSIS OF SCMS")

df = pd.read_csv("https://raw.githubusercontent.com/Ajaybabuds/App/main/COGS1.csv", sep=',', engine='python')
df = df.drop([0])
x = df.columns
print(x)
col1, col2, col3 = st.beta_columns(3)
with col1:
    item = st.selectbox("Select an Item", options=df[x[0]].values)
with col2:
    slct = st.selectbox("Select a Customised Metric", options=['Inventory', 'Ratio Analysis'])
with col3:
    chrt = st.selectbox("Select a Chart", options=['Bar', 'Circle', 'Area'])
for i in df[x[0]].values:
    if i in item:
        if 'Inventory' in slct:
            j=[df.columns[j] for j in range(1, 7) if j != 4]
            result = df.loc[df.Item == i,j]
            st.table(result)
            chart_data = pd.DataFrame()
            chart_data['Quantity'] = result.values.ravel()
            chart_data['Inventory'] = result.columns
            if "Bar" in chrt:
                chart_v1 = alt.Chart(chart_data).mark_bar().encode(x='Inventory', y='Quantity',
                                                                   color=alt.value("red")).properties(width=500,
                                                                                                      height=300)
                st.write("", "", chart_v1)
            elif "Circle" in chrt:
                chart_v2 = alt.Chart(chart_data).mark_circle().encode(x='Inventory', y='Quantity',
                                                                      color=alt.value("blue")).properties(width=500,
                                                                                                          height=300)
                st.write("", "", chart_v2)
            else:
                chart_v3 = alt.Chart(chart_data).mark_area().encode(x="Inventory", y='Quantity',
                                                                    color=alt.value('green')).properties(width=500,
                                                                                                         height=300)
                st.write("", "", chart_v3)
        else:
            z=[df.columns[z] for z in range(4, 11) if z != 5 if z != 6]
            answer = df.loc[df.Item == i, z]
            st.table(answer)
