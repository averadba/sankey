import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


st.title("Sankey Plot for Process Flow Generator")
st.write("*By:* A. Vera")

# Ask user for the steps in the process
steps = st.text_input("Enter the steps in the process, separated by commas:")
steps = steps.split(',')

# Create empty dataframe to store values
data = pd.DataFrame(columns=steps)

# Ask user for values for each step
values = []
for step in steps:
    value = st.number_input(f"Enter value for {step}:")
    values.append(value)
    data = data.append({step: value}, ignore_index=True)

# Create Sankey plot
fig = go.Figure(data=[go.Sankey(node = dict(label = steps),
                                 link = dict(source = [i for i in range(len(steps)-1)], # source of the link
                                             target = [i for i in range(1,len(steps))], # target of the link
                                             value = values))])

fig.update_layout(title_text="Process Flow", font_size=10)

if not data.empty:
    st.plotly_chart(fig)
else:
    st.warning("No data provided. Please provide values for each step.")
