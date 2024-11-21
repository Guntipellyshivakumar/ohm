import streamlit as st

st.title("OHMS LAW")

# Function to calculate resistance
def calculate_resistance(v, i):
    r = v / i
    return r

# Create tabs
tab1, tab2 = st.tabs(["Compute", "Explain"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        with st.container():  # border=True is not valid in Streamlit
            vth = st.number_input("Voltage (V):", value=20.0)  # Use descriptive names
            Rth = st.number_input("Current (I):", value=2.0)   # Default value set to float
            compute = st.button("Compute")

    with col2:
        if compute:
            if Rth != 0:  # Avoid division by zero
                r = calculate_resistance(vth, Rth)
                st.write(f"Resistance = {r} ohms")
            else:
                st.write("Current cannot be zero to calculate resistance.")

with tab2:
    st.write("Ohm's Law is a fundamental principle in electrical circuits that describes the relationship between voltage, current, and resistance. It states that the voltage")