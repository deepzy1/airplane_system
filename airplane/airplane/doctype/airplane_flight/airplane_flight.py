# Copyright (c) 2025, deepak' and contributors
# For license information, please see license.txt
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document



class AirplaneFlight(WebsiteGenerator):

	def before_submit(self):
		self.status ="Completed"
	
