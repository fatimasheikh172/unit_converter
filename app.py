import streamlit as st

def convert_temperature(value, from_unit, to_unit):
    """Handle temperature conversions between Celsius, Fahrenheit, and Kelvin"""
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

# ===============================================
# Interface Setup
# ===============================================
st.set_page_config(page_title="Universal Converter", layout="wide")
st.markdown("## 🔄 Universal Unit Converter")
st.divider()

# Sidebar for category selection
with st.sidebar:
    st.header("Settings")
    category = st.selectbox(
        "Conversion Type",
        ["Length", "Mass", "Temperature", "Volume", "Speed"],
        help="Select the type of conversion you want to perform"
    )

# Unit icons display
unit_icons = {
    "Length": "📏",
    "Mass": "⚖️",
    "Temperature": "🌡️",
    "Volume": "🧪",
    "Speed": "💨"
}
st.subheader(f"{unit_icons[category]} {category} Conversion")

# ===============================================
# Conversion Definitions
# ===============================================
conversion_data = {
    "Length": {
        "units": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "factors": {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Feet": 0.3048,
            "Inches": 0.0254
        }
    },
    "Mass": {
        "units": ["Grams", "Kilograms", "Pounds", "Ounces"],
        "factors": {
            "Grams": 0.001,
            "Kilograms": 1,
            "Pounds": 0.453592,
            "Ounces": 0.0283495
        }
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
    },
    "Volume": {
        "units": ["Liters", "Milliliters", "Gallons", "Cubic Meters"],
        "factors": {
            "Liters": 1,
            "Milliliters": 0.001,
            "Gallons": 3.78541,
            "Cubic Meters": 1000
        }
    },
    "Speed": {
        "units": ["km/h", "mph", "m/s", "Knots"],
        "factors": {
            "km/h": 1,
            "mph": 1.60934,
            "m/s": 3.6,
            "Knots": 1.852
        }
    }
}

# ===============================================
# Input Widgets
# ===============================================
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    from_unit = st.selectbox("From", conversion_data[category]["units"])
with col2:
    to_unit = st.selectbox("To", conversion_data[category]["units"])
with col3:
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

# ===============================================
# Conversion Logic
# ===============================================
if st.button("✨ Convert", help="Click to perform conversion"):
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        # Convert through base unit
        base = value * conversion_data[category]["factors"][from_unit]
        result = base / conversion_data[category]["factors"][to_unit]
    
    # Display result with animation
    st.balloons()
    st.success(f"**Result:** {value:.2f} {from_unit} = **{result:.4f} {to_unit}**")
    st.ballons()
    st.captions("Made by fatima sheikh")
