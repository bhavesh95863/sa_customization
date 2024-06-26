from . import __version__ as app_version

app_name = "sa_customization"
app_title = "sa_customization"
app_publisher = "sa_customization"
app_description = "sa_customization"
app_email = "shahnandkishor512@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sa_customization/css/sa_customization.css"
# app_include_js = "/assets/sa_customization/js/sa_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/sa_customization/css/sa_customization.css"
# web_include_js = "/assets/sa_customization/js/sa_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sa_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
    # "methods": "sa_customization.utils.jinja_methods",
    "methods": "sa_customization.utils.money_in_arabic_words"
}

# Installation
# ------------

# before_install = "sa_customization.install.before_install"
# after_install = "sa_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sa_customization.uninstall.before_uninstall"
# after_uninstall = "sa_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sa_customization.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sa_customization.tasks.all"
# 	],
# 	"daily": [
# 		"sa_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"sa_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sa_customization.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sa_customization.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sa_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sa_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sa_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sa_customization.utils.before_request"]
# after_request = ["sa_customization.utils.after_request"]

# Job Events
# ----------
# before_job = ["sa_customization.utils.before_job"]
# after_job = ["sa_customization.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sa_customization.auth.validate"
# ]

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["is_system_generated", "=", 0],
            ["module", "=", "sa_customization"],
        ],
    },
    {"dt": "Client Script", "filters": [["module", "=", "sa_customization"]]},
    {"dt": "Print Format", "filters": [["module", "=", "sa_customization"]]},
]
