# -*- coding: utf-8 -*-
# © 2015 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import base64
import tempfile
import xlrd
from xlrd import XLRDError

from openerp import api, exceptions, fields, models, _


class StockLotSupplierImporter(models.TransientModel):
    _name = "stock.lot.supplier_importer"

    xls_file = fields.Binary('XLS File', required=True)
    error_lines = fields.Text('Not Loaded Lines', readonly=True)

    @api.model
    def read_excel_row(self, sh, rownum):
        row = {}
        for col in xrange(sh.ncols):
            row[sh.cell(0, col).value.lower().strip()] = \
                sh.cell(rownum, col).value
        return row

    @api.multi
    def _import_lots(self):
        product_product_model = self.env['product.product']
        lot_model = self.env['stock.production.lot']
        error_lines = ''
        tf = tempfile.NamedTemporaryFile(delete=False)
        tf.write(base64.b64decode(self.xls_file))
        tf.close()
        try:
            wb = xlrd.open_workbook(tf.name)
            sh = wb.sheet_by_index(0)
        except XLRDError:
            raise exceptions.Warning(
                _("The selected file has not the correct csv format, "
                  "please select a correct one."))
        for rownum in xrange(sh.nrows):
            if rownum > 0:
                row = self.read_excel_row(sh, rownum)
                serial_no = row.get('serial_no', False)
                if type(serial_no) == float:
                    serial_no = format(serial_no, '.0f')
                if not row:
                    continue
                if row.get('sku_no', False) and serial_no:
                    lots = lot_model.search([
                        ('name', '=', serial_no)
                    ])
                    if lots:
                        error_lines += _(
                            "- Already exists a serial number with number "
                            "'%s', skipped. (File line: %s)\n") % (
                                serial_no,
                                rownum + 1)
                        continue
                    products = product_product_model.search([
                        ('default_code', '=', row['sku_no'])
                    ])
                    if not products:
                        error_lines += _(
                            "- We have not found any product with '%s' as "
                            "sku number, skipped. (File line: %s)\n") % (
                                row['sku_no'],
                                rownum + 1)
                        continue
                    lot_model.create({
                        'name': serial_no,
                        'product_id': products[0].product_tmpl_id.
                        product_variant_ids[0].id
                    })
        return error_lines

    @api.multi
    def import_lots(self):
        self.ensure_one()
        self.error_lines = self._import_lots()
        if self.error_lines:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'stock.lot.supplier_importer',
                'name': _('Lots Supplier Importer'),
                'res_id': self.id,
                'view_type': 'form',
                'view_mode': 'form',
                'view_id': False,
                'target': 'new',
                'nodestroy': True,
            }
        return {'type': 'ir.actions.act_window_close'}
