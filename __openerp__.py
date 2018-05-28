# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'HR Extend',
    'version': '1.0',
    'category': 'ARO HR',
    'sequence': 1,
    'summary': 'Ajout de champs',
    'description': """
                Ajout de champs dans la table hr_department
                   """,
    'author': 'Solofo',
    'website': 'http://www.aro.mg',
    'depends': ['base', 'hr', 'aro_hr', 'report'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_department_inherit.xml',
        'views/hr_job_inherit.xml',
        'views/common_menu.xml',
        'reports.xml',
        'views/hr_employee_career.xml',
        'views/hr_employee_formation_module_view.xml',
        'views/hr_employee_branche.xml',
        'views/hr_formation_instructor.xml',
        'views/sanction_type_view.xml',
        'views/hr_employee_sanction_view.xml',
        'views/qual_type_view.xml',
        'views/hr_employee_module_specificite_view.xml',
        #'views/hr_session_formation_version_2_view.xml',
        'views/hr_plan_formation_view.xml',
        'views/hr_session_plan_view.xml',
        'views/hr_souhait_formation.xml',
        'views/hr_session_elearning.xml',
        'views/hr_plan_elearning.xml',
        'views/hr_employee_diplome_view.xml',
        'views/hr_employee_decoration_type_view.xml',
        'views/hr_employee_decoration.xml',
        'views/hr_employee_note_view.xml',
        'views/hr_employee_last_job_view.xml',
        'views/hr_niveau_etudes.xml',
        'views/hr_employee.xml',
        'views/hr_employee_career_history.xml',
        'data/hr_employee_category_data.xml',
        'data/sanction_type_data.xml',
        'data/hr_department_data.xml',
        'data/hr_job_data.xml',
        'data/hr_employee_decoration_type_data.xml',
        'data/hr_holidays_status_data.xml',
        'employee_contract_report.xml',
        'employee_qualification_report.xml',
        'employee_formation_report.xml',
        'employee_distinction_report.xml',
        'employee_sanction_report.xml',
        'employee_notation_report.xml',
        'employee_last_job_report.xml',
        'employee_job_history_report.xml',
        'employee_grade_history_report.xml',
        'employee_department_history_report.xml',
    ],

    "qweb": [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
