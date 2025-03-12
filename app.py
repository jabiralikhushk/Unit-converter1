import streamlit as st

# Conversion factors
conversion_data = {
    "Length": {
        "Metre": 1,
        "Kilometre": 0.001,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Mile": 0.000621371,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
        "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9,
        "Celsius to Kelvin": lambda c: c + 273.15,
        "Kelvin to Celsius": lambda k: k - 273.15,
        "Fahrenheit to Kelvin": lambda f: (f - 32) * 5/9 + 273.15,
        "Kelvin to Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32
    }
}

# Streamlit UI
st.title("🔄 Unit Converter")

# Category selection
category = st.selectbox("Select a category", list(conversion_data.keys()))

# Temperature Conversion
if category == "Temperature":
    unit = st.selectbox("Select conversion", list(conversion_data[category].keys()))
    value = st.number_input("Enter value", format="%.2f")

    # Perform conversion
    if unit and value is not None:
        result = conversion_data[category][unit](value)
        st.write(f"### {value} {unit.split()[0]} = {result:.2f} {unit.split()[-1]}")
        st.markdown(f"📌 *Formula:* {unit.replace('to', '→')} calculation applied.")

# Length & Weight Conversion
else:
    col1, col2, col3 = st.columns([3, 1, 3])

    with col1:
        value = st.number_input("Enter value", min_value=0.0, format="%.2f")
        unit_from = st.selectbox("From", list(conversion_data[category].keys()))

    with col2:
        st.write("=")  # UI alignment

    with col3:
        unit_to = st.selectbox("To", list(conversion_data[category].keys()))
        result = 0
        if unit_from and unit_to:
            result = value * (conversion_data[category][unit_to] / conversion_data[category][unit_from])
        st.write(f"<h2>{result:.4f} {unit_to}</h2>", unsafe_allow_html=True)

    # Formula display
    formula = f"Multiply by {conversion_data[category][unit_to] / conversion_data[category][unit_from]:.4f}"
    st.markdown(f"📌 *Formula:* {formula}")