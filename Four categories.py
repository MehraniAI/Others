import streamlit as st 

st.title("🔄 Unit Convertor 🔄")
st.header("⚡ Convert Units Easily And Quickly! ⚡")
st.subheader("📏 Enter The Value And Choose Your Units. 📏")  

def convert_length(value , from_unit, to_unit):
    if from_unit == "meters" and to_unit == "kilometers":
        return value / 1000
    elif from_unit == "kilometers" and to_unit == "meters":
        return value * 1000
    elif from_unit == "grams" and to_unit == "kilograms":
        return value / 1000
    elif from_unit == "kilograms" and to_unit == "grams":
        return value * 1000
    elif from_unit == "millimeters" and to_unit == "meters":
        return value / 1000
    elif from_unit == "meters" and to_unit == "millimeters":
        return value * 1000
    elif from_unit == "millimeter" and to_unit == "centimeters":
        return value / 10
    elif from_unit == "centimeters" and to_unit == "millimeters":
        return value * 10
    elif from_unit == "millimeters" and to_unit == "kilometers":
        return value / 1000000
    elif from_unit == "kilometers" and to_unit == "millimeters":
        return value * 1000000
    elif from_unit == "centimeters" and to_unit == "meters":
        return value / 100
    elif from_unit == "meters" and to_unit == "centimeters":
        return value * 100
    else:
        return "❌ invalid unit"
    
def convert_temperature(value , from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value* 9/5) + 32 
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "❌ invalid unit"

def convert_time(value , from_unit, to_unit):
    if from_unit == "seconds" and to_unit == "minutes":
        return value / 60
    elif from_unit == "seconds" and to_unit == "hours":
        return value / 3600
    elif from_unit == "minutes" and to_unit == "seconds":
        return value * 60
    elif from_unit == "minutes" and to_unit == "hours":
        return value / 60
    elif from_unit == "hours" and to_unit == "minutes":
        return value * 60
    elif from_unit == "hours" and to_unit == "seconds":
        return value * 3600
    elif from_unit == "hours" and to_unit == "days":
        return value / 24
    elif from_unit == "days" and to_unit == "hours":
        return value * 24
    elif from_unit == "days" and to_unit == "minutes":
        return value * 1440
    elif from_unit == "days" and to_unit == "seconds":
        return value * 86400
    else:
        return "❌ invalid unit"

def convert_weight(value , from_unit, to_unit):
    if from_unit == "kilogram" and to_unit == "gram":
        return value * 1000
    elif from_unit == "gram" and to_unit == "kilogram":
        return value / 1000
    elif from_unit == "kilogram" and to_unit == "pound":
        return value * 2.20462
    elif from_unit == "kilogram" and to_unit == "ounce":
        return value * 35.274
    elif from_unit == "kilogram" and to_unit == "milligram":
        return value * 1000000
    elif from_unit == "gram" and to_unit == "milligram":
        return value * 1000
    elif from_unit == "gram" and to_unit == "pound":
        return value / 453.592
    elif from_unit == "gram" and to_unit == "ounce":
        return value / 28.35
    elif from_unit == "pound" and to_unit == "gram":
        return value * 453.592
    elif from_unit == "pound" and to_unit == "kilogram":
        return value / 2.20462
    elif from_unit == "pound" and to_unit == "milligram":
        return value * 453592
    elif from_unit == "pound" and to_unit == "ounce":
        return value * 16
    elif from_unit == "milligram" and to_unit == "gram":
        return value / 1000
    elif from_unit == "milligram" and to_unit == "kilogram":
        return value / 1000000
    elif from_unit == "milligram" and to_unit == "pound":
        return value / 453592
    elif from_unit == "milligram" and to_unit == "ounce":
        return value / 28350
    elif from_unit == "ounce" and to_unit == "gram":
        return value * 28.35
    elif from_unit == "ounce" and to_unit == "kilogram":
        return value / 35.274
    elif from_unit == "ounce" and to_unit == "pound":
        return value / 16
    elif from_unit == "ounce" and to_unit == "milligram":
        return value * 28350
    else:
        return "❌ invalid unit"

unit_type = st.selectbox("📌 **Select Category:**",["📏 Length","🌡️ Temperature","⌛ Time","⚖️ Weight"])
value = st.number_input("**✎ Please enter the value:**") 

if unit_type == "📏 Length":
    length_unit = ["meters", "kilometers", "millimeters", "centimeters"] 
    from_unit = st.selectbox("🔹 **From Unit:**", length_unit)
    to_unit = st.selectbox("🔸 **To Unit:**", length_unit)
    if st.button("**🔄 Convert**"):
        result = convert_length(value , from_unit, to_unit)
        st.write(f"**📏 Result :** {result} {to_unit}")

elif unit_type == "🌡️ Temperature":
    temperature_unit = ["celsius", "fahrenheit", "kelvin"] 
    from_unit = st.selectbox("🔹 **From Unit:**", temperature_unit)
    to_unit = st.selectbox("🔸 **To Unit:**", temperature_unit)
    if st.button("**🔄 Convert**"):
        result = convert_temperature(value , from_unit, to_unit)
        st.write(f"**🌡️ Result :** {result} {to_unit}")

elif unit_type == "⌛ Time":
    time_unit = ["hours", "minutes", "seconds", "days"] 
    from_unit  = st.selectbox("🔹 **From Unit:**", time_unit)
    to_unit = st.selectbox("🔸 **To Unit:**", time_unit)
    if st.button("**🔄 Convert**"):
        result = convert_time(value , from_unit, to_unit)
        st.write(f"**⌛ Result :** {result} {to_unit}")

elif unit_type == "⚖️ Weight":
    weight_unit = ["kilogram", "gram", "pound", "milligram", "ounce"] 
    from_unit  = st.selectbox("🔹 **From Unit:**", weight_unit)
    to_unit = st.selectbox("🔸 **To Unit:**", weight_unit)
    if st.button("**🔄 Convert**"):
        result = convert_weight(value , from_unit, to_unit)
        st.write(f"**⚖️ Result :** {result} {to_unit}")
