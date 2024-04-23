import streamlit as st
import psutil

def display_system_resources():
    # Get system information
    total_ram = psutil.virtual_memory().total / (1024 * 1024)  # Convert bytes to MB
    cpu_freq = psutil.cpu_freq().current  # Current CPU frequency in MHz

    # Display system resources
    st.write(f"Total RAM: {total_ram:.2f} MB")
    st.write(f"CPU Frequency: {cpu_freq:.2f} MHz")

# Streamlit UI
st.title("System Resource Viewer")

if st.button("View System Resources"):
    display_system_resources()
