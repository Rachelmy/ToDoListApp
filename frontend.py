import streamlit as st
import requests

# Base URL of your FastAPI backend
API_URL = "http://localhost:8000"

st.title("📝 To-Do List")

# --- Add a New Task ---
st.header("➕ Add a New Task")

# User input for task description
text = st.text_input("Task description")

# Checkbox for task completion status
is_done = st.checkbox("Completed?", value=False)

# Button to add the task
if st.button("Add Task"):
    if text.strip():
        response = requests.post(
            f"{API_URL}/items",
            json={"text": text, "is_done": is_done}
        )
        if response.status_code == 200:
            st.success("Task added successfully!")
        else:
            st.error("Failed to add task.")
    else:
        st.warning("Task description cannot be empty.")

# --- View Task List ---
st.header("📋 Task List")

# Slider to limit number of tasks shown
limit = st.slider("Number of tasks to view:", 1, 50, 10)

# Fetch tasks from the API
response = requests.get(f"{API_URL}/items", params={"limit": limit})

# Display tasks
if response.status_code == 200:
    tasks = response.json()
    for i, task in enumerate(tasks):
        status = "✅" if task["is_done"] else ""
        st.write(f"**{i}** - {task['text']} {status}")
else:
    st.error("Unable to fetch tasks.")
