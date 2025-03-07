# Copyright (c) 2025, deepak' and contributors
# For license information, please see license.txt

import frappe
import random,string
from frappe.model.document import Document


class AirplaneTicket(Document):

	def before_save(self):
		self.get_total_price()
		# self.seat= self.assign_seat()

	def before_submit(self):
		check_status=self.validate()
		if check_status:
			frappe.throw("Passenger Still Not yet Boarded the flight")

	

		

	def assign_seat(self):
		random_seat=str(random.randint(1,100)) + random.choice(string.ascii_uppercase)
		return random_seat

	def get_total_price(self):
		total_add_ons_amount=0
		for amount in self.item:
			if amount.amount:
				total_add_ons_amount+= amount.amount
			

		self.total_price = self.flight_price + total_add_ons_amount

	def validate(self):
		if self.status != "Boarded":
			return True
		
		pass
