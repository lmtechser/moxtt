#-*- coding: utf-8 -*-
from odoo import http


class M1(http.Controller):
    @http.route('/m1/m1/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/m1/m1/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('m1.listing', {
            'root': '/m1/m1',
            'objects': http.request.env['m1.m1'].search([]),
        })

    @http.route('/m1/m1/objects/<model("m1.m1"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('m1.object', {
            'object': obj
        })
