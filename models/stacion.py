# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stacion(models.Model):
    _name = 'nitro.gas.stacion'
    _description = 'Bomba'

    ticket_id = fields.Char(copy=False, default='New', readonly=True, string='No de Ticket')
    car_model = fields.Char(string='Modelo:')  # required="True"
    number_plate = fields.Char(string='Placa:')
    cv = fields.Float(string='CV:')
    color = fields.Char(string='Color:')
    fuel_litres = fields.Float()
    marca = fields.Selection([('T', 'Toyota'), ('N', 'Nissan'), ('M', 'Mitsubishi')], string='Marca de Fabricante')
    empty = fields.Boolean(string='Tanque Vacio')
    full = fields.Boolean(string='Tanque Lleno')
    customer = fields.Many2one(comodel_name='res.partner', string='Nombre del Cliente', required="True")

    @api.model
    def create(self, vals):
        if vals.get('ticket_id', 'New') == 'New':
            vals['ticket_id'] = self.env['ir.sequence'].next_by_code('task.lfpv') or 'New'
        result = super(Stacion, self).create(vals)
        return result


    # Método para imprimir el ticket
    def print_ticket(self):
        return self.env.ref('nitro_gas.report_ticket').report_action(self)
