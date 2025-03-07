// Copyright (c) 2025, deepak' and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        // Add a custom button
        frm.add_custom_button("Assign Seat", () => {
            // Create a dialog with an input field
            let d = new frappe.ui.Dialog({
                title: "Enter Seat Number",
                fields: [
                    {
                        label: "Seat",
                        fieldname: "seat",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],
                primary_action_label: "Assign",
                primary_action(values) {
                    // Set the entered seat number to the Seat field
                    frm.set_value("seat", values.seat);
                    d.hide();
                }
            });
            d.show();
        });
    }
});
