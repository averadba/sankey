import streamlit as st
import plotly.graph_objects as go

# Optional: page config
st.set_page_config(
    page_title="Sankey Plot for Process Flow Generator",
    layout="centered"
)

# Hide Streamlit UI elements
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Sankey Plot for Process Flow Generator")
st.write("*By:* A. Vera")

# Ask user for the steps in the process
steps_input = st.text_input(
    "Enter the steps in the process, separated by commas:"
)

if not steps_input:
    st.info("Type at least two steps separated by commas to get started.")
    st.stop()

# Clean and split steps
steps = [s.strip() for s in steps_input.split(",") if s.strip()]

if len(steps) < 2:
    st.warning("Please enter at least two steps (e.g. Step 1, Step 2, Step 3).")
    st.stop()

st.subheader("Flow values between steps")

# Ask user for values for each link (step i -> step i+1)
values = []
for i in range(len(steps) - 1):
    from_step = steps[i]
    to_step = steps[i + 1]
    value = st.number_input(
        f"Enter value from '{from_step}' to '{to_step}':",
        min_value=0.0,
        key=f"value_{i}"
    )
    values.append(value)

# Only draw the Sankey if there is at least one non-zero value
if all(v == 0 for v in values):
    st.info("Enter values greater than 0 to generate the Sankey diagram.")
    st.stop()

# Create Sankey plot
fig = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                label=steps,
                pad=20,
                thickness=20
            ),
            link=dict(
                source=[i for i in range(len(steps) - 1)],
                target=[i for i in range(1, len(steps))],
                value=values,
            ),
        )
    ]
)

fig.update_layout(
    title_text="Process Flow",
    font_size=12,
    height=500
)

st.plotly_chart(fig, use_container_width=True)
