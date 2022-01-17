import frappe
@frappe.whitelist()
def mojefunc():
    return "hello"
