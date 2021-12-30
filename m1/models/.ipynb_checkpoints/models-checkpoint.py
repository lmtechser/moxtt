#-*- coding: utf-8 -*-

from odoo import models, fields, api


class m1(models.Model):
    _name = 'm1.m1'
    _description = 'm1.m1'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
#
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
