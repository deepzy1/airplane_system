# Copyright (c) 2025, Deepak and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "flight",
            "label": "Flight",
            "fieldtype": "Data"
        },
        {
            "fieldname": "passenger_name",
            "label": "Passenger",
            "fieldtype": "Data"
        },
    ]

    # Fetching flight and passenger details
    data = frappe.get_all("Airplane Ticket",
                          fields=["flight", "passenger"],
                          filters=filters)  # Apply filters if provided

    # Convert passenger IDs to names
    for row in data:
        row["passenger_name"] = frappe.db.get_value("Flight Passenger", row["passenger"], "full_name")

    # Grouping passengers by flight
    flight_counts = {}
    for row in data:
        flight_counts[row["flight"]] = flight_counts.get(row["flight"], 0) + 1

    flight_labels = list(flight_counts.keys())
    passenger_counts = list(flight_counts.values())

    # Pie Chart - Number of passengers per flight
    pie_chart = {
        "title": "Passengers per Flight (Pie Chart)",
        "data": {
            "labels": flight_labels,
            "datasets": [{"values": passenger_counts}]
        },
        "type": "pie",
    }

   

    # Return both charts in a list
    return columns, data, "Passengers per Flight Report", pie_chart
