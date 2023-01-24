from odoo import fields, models


class Employees(models.Model):
    _name = "employees.model"
    _description = "Employee of SMC"
    _order = "sequence"

    name = fields.Char('Name', required=True, translate=True)
    #last_name = fields.Char('Last name', required=True, translate=True)
    #dni = fields.Integer(required=True, default=10)
    #number_of_months = fields.Integer('# Months', required=True)
    #active = fields.Boolean('Active', default=True)

    #_sql_constraints = [
        #('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
        #(name, sql_definition, message) 
    #]