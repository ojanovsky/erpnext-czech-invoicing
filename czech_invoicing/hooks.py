# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "czech_invoicing"
app_title = "Czech Invoicing"
app_publisher = "Alarex-Group s.r.o."
app_description = "IC, DIC, VAT Date, czech invoice print format"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ondrej.janovsky@alarex.cz"
app_license = "MIT"
fixtures = ["Custom Field", "Client Script", "Translation", "Property Setter", {
	"doctype": "Print Format",
	"filters":	{
		"name": ["in", "czech invoice"]
 }    
	}]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/czech_invoicing/css/czech_invoicing.css"
# app_include_js = "/assets/czech_invoicing/js/czech_invoicing.js"

# include js, css files in header of web template
# web_include_css = "/assets/czech_invoicing/css/czech_invoicing.css"
# web_include_js = "/assets/czech_invoicing/js/czech_invoicing.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "czech_invoicing.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "czech_invoicing.install.before_install"
# after_install = "czech_invoicing.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "czech_invoicing.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"czech_invoicing.tasks.all"
# 	],
# 	"daily": [
# 		"czech_invoicing.tasks.daily"
# 	],
# 	"hourly": [
# 		"czech_invoicing.tasks.hourly"
# 	],
# 	"weekly": [
# 		"czech_invoicing.tasks.weekly"
# 	]
# 	"monthly": [
# 		"czech_invoicing.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "czech_invoicing.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "czech_invoicing.event.get_events"
# }

