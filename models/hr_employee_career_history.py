# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrEmployeeJobHistory(models.Model):
    _name = 'hr.employee.job.history'
    _description = 'Suivi des changements de fonction'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    date = fields.Date(string='Date')
    job_id = fields.Many2one('hr.job', string='Fonction')
    commentaires = fields.Char(string='Commentaires')

class HrEmployeeDepartmentHistory(models.Model):
    _name = 'hr.employee.department.history'
    _description = 'Suivi des changements de service'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    date = fields.Date(string='Date')
    department_id = fields.Many2one('hr.department', string='Service')
    commentaires = fields.Char(string='Commentaires')

    #_order = 'field1_name desc,field2_name asc'

class HrEmployeeGradeHistory(models.Model):
    _name = 'hr.employee.grade.history'
    _description = 'Suivi des changements de grade'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    date = fields.Date(string='Date')
    category_ids = fields.Many2one('hr.employee.category', string='Grade')
    commentaires = fields.Char(string='Commentaires')