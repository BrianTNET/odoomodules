from odoo import fields, models


class Employee(models.Model):
    _name = "smcn.employee"
    _description = "Employee of SMC"

    name = fields.Char('Name', required=True)
    last_name = fields.Char('Last name', required=True)
    dni = fields.Integer(required=True, string='DNI')
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    #number_of_months = fields.Integer('# Months', required=True)
    #active = fields.Boolean('Active', default=True)

    #_sql_constraints = [
        #('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
        #(name, sql_definition, message) 
    #]