import frappe

def execute():
    if not frappe.db.exists("DocType", "Airplane Ticket"):
        return  # Exit if the DocType doesn't exist (avoiding errors)

    tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["is", "not set"]}, fields=["name"])
    
    for ticket in tickets:
        doc = frappe.get_doc("Airplane Ticket", ticket.name)
        doc.seat = assign_seat()  # Implement this function based on your rule
        doc.save(ignore_permissions=True)

    frappe.db.commit()  # Ensure changes persis