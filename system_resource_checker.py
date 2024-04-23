import streamlit as st
import psutil

def display_system_resources():
    # Get system information
    total_ram = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
    cpu_freq = psutil.cpu_freq().current / 1000  # Convert MHz to GHz

    # Display system resources
    st.write(f"Total RAM: {total_ram:.2f} GB")
    st.write(f"CPU Frequency: {cpu_freq:.2f} GHz")

# Streamlit UI
st.title("System Resource Viewer")

if st.button("View System Resources"):
    display_system_resources()
