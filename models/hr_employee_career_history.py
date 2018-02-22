# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrEmployeeJobHistory(models.Model):
    _name = 'hr.employee.job.history'
    _description = 'Suivi des changements de fonction'
    _order = "date asc"

    matricule = fields.Char(related="employee_id.matricule",string='Matricule',readonly=True,size=50)
    employee_id = fields.Many2one('hr.employee', string='Employee')
    date = fields.Date(string='Date')
    job_id = fields.Many2one('hr.job', string='Fonction')
    commentaires = fields.Char(string='Commentaires')

class HrEmployeeDepartmentHistory(models.Model):
    _name = 'hr.employee.department.history'
    _description = 'Suivi des changements de service'
    _order = "date asc"

    employee_id = fields.Many2one('hr.employee', string='Employee')
    matricule = fields.Char(related="employee_id.matricule",string='Matricule',readonly=True,size=50)
    date = fields.Date(string='Date')
    department_id = fields.Many2one('hr.department', string='Service')
    commentaires = fields.Char(string='Commentaires')


class HrEmployeeGradeHistory(models.Model):
    _name = 'hr.employee.grade.history'
    _description = 'Suivi des changements de grade'
    _order = 'employee_id desc,date asc'
    
    employee_id = fields.Many2one('hr.employee', string='Employee')
    matricule = fields.Char(related="employee_id.matricule",string='Matricule',readonly=True,size=50)
    date = fields.Date(string='Date')
    category_ids = fields.Many2one('hr.employee.category', string='Grade')
    commentaires = fields.Char(string='Commentaires')

    #_sql_constraints = [('name_grade_uniq', 'unique(employee_id,category_ids )', _(u'Vous avez déja saisi les avantages de cet employé !'))]