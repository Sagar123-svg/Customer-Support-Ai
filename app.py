import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from backend.database import (
    get_all_tickets,
    get_ticket_stats,
    export_tickets
)   

st.title("🤖 Customer Support AI")

stats = get_ticket_stats()
#st.write(stats)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Tickets",
    stats["total"]
)

col2.metric(
    "Billing",
    stats["billing"]
)

col3.metric(
    "Shipping",
    stats["shipping"]
)

col4.metric(
    "Technical",
    stats["technical"]
)

col5.metric(
    "Escalated",
    stats["escalated"]
)
st.subheader("Ticket Categories Overview")

chart_data = pd.DataFrame({
    "Category": [
        "Billing",
        "Shipping",
        "Technical"
    ],
    "Count": [
        stats["billing"],
        stats["shipping"],
        stats["technical"]
    ]
})

fig, ax = plt.subplots()

ax.bar(
    chart_data["Category"],
    chart_data["Count"]
)

ax.set_title("Tickets by Category")

st.pyplot(fig)
st.subheader("Category Distribution")

fig2, ax2 = plt.subplots()

ax2.pie(
    [
        stats["billing"],
        stats["shipping"],
        stats["technical"]
    ],
    labels=[
        "Billing",
        "Shipping",
        "Technical"
    ],
    autopct="%1.1f%%"
)

st.pyplot(fig2)  

ticket = st.text_area(
    "Describe your issue"
)

if st.button("Submit"):

    if not ticket.strip():
        st.error("Please enter a ticket description.")
        st.stop()


    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={
            "ticket": ticket
        }
    )

    result = response.json()

    st.subheader("Category")
    st.write(result["category"])

    st.subheader("Sentiment")
    st.write(result["sentiment"])
    
    st.subheader("Escalation Required")
    st.write(result["escalate"])

    st.subheader("Retrieved Document")
    st.write(result["retrieved_document"])

    st.subheader("Response")
    st.write(result["response"])
    
st.subheader("Ticket History")

search_text = st.text_input(
    "Search Tickets",
    key="ticket_search"
)


if st.button("Show Ticket History"):

    tickets = get_all_tickets()

    for ticket in tickets:

        if search_text:

            if search_text.lower() not in ticket[1].lower():
                continue

        with st.expander(f"Ticket #{ticket[0]}"):

            st.write(f"**Ticket:** {ticket[1]}")
            st.write(f"**Category:** {ticket[2]}")
            st.write(f"**Sentiment:** {ticket[3]}")
            st.write(f"**Document:** {ticket[4]}")
            st.write(f"**Created At:** {ticket[5]}")
            st.write(f"**Response:** {ticket[6]}")
        st.markdown("---")
if st.button("Export Tickets to CSV"):

    file_path = export_tickets()

    with open(file_path, "rb") as file:

        st.download_button(
            label="Download CSV",
            data=file,
            file_name="ticket_report.csv",
            mime="text/csv"
        )
