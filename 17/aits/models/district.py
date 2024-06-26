# -*- coding: utf-8 -*-
from odoo import fields, models


class NepalDairyIndexDistrict(models.Model):
    _name = "nepal.dairy.index.district"
    _description = "District"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "district_name"

    province_id = fields.Many2one(comodel_name='nepal.dairy.index.province', string='Province', required=True,
                                  tracking=True)
    district_code = fields.Char('District Code', required=True, tracking=True)
    district_name = fields.Char('District Name', required=True, tracking=True)
    municipality_count = fields.Integer('Municipality Count', compute='_compute_municipality_count')
    ward_count = fields.Integer('Word Count', compute='_compute_ward_count')



