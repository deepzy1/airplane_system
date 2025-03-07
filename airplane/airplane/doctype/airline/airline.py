# Copyright (c) 2025, deepak' and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Airline(WebsiteGenerator):
	
	def before_save(self):
		self.route="https://www.goindigo.in/"
		pass
