# -*- coding: utf-8 -*-
# © 2015 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import base64
import cStringIO
from xlwt import Workbook

from openerp import exceptions
from openerp.tests.common import TransactionCase


class TestImportLots(TransactionCase):

    def setUp(self):
        super(TestImportLots, self).setUp()
        self.product = self.env['product.product'].create({
            'name': 'My Test Product 1',
            'type': 'product',
            'default_code': 'SKU_2',
        })

    def test_import_wrong_file(self):
        with self.assertRaises(exceptions.Warning):
            content = 'Dummy,file'
            importer = self.env['stock.lot.supplier_importer'].create({
                'xls_file': base64.b64encode(content),
            })
            importer.import_lots()

    def test_import_xls_file(self):
        wb = Workbook()
        ws = wb.add_sheet('0')
        xls_content = [
            ('sku_no', 'serial_no'),
            ('123', 'serial123'),
            ('SKU_2', 'serial_product_1'),
            ('SKU_2', 'serial_product_1')
        ]
        for row in xrange(len(xls_content)):
            for col in xrange(len(xls_content[row])):
                ws.write(row, col, xls_content[row][col])
        f = cStringIO.StringIO()
        wb.save(f)
        importer = self.env['stock.lot.supplier_importer'].create({
            'xls_file': base64.b64encode(f.getvalue()),
        })
        importer.import_lots()

        # Check the lot is created correctly
        lots = self.env['stock.production.lot'].search([
            ('name', '=', 'serial_product_1'),
        ])
        self.assertEqual(self.product.id, lots[0].product_id.id)

        # Check does not creates duplicates
        self.assertTrue(
            "number with number 'serial_product_1'" in importer.error_lines)

        # Check does not creates lots with not existing SKUs.
        self.assertTrue(
            "not found any product with '123' as sku" in importer.error_lines)
