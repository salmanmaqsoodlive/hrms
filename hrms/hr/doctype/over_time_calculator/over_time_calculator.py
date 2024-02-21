# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OverTimeCalculator(Document):
	#pass
    def validate(self):
        if self.overtime_hours < 2:
            
            self.validate_overtime_hours()
    
    def validate_overtime_hours(self):
        frappe.throw(f'Over Time Hours Must Be Greater Than or equal to 2')


