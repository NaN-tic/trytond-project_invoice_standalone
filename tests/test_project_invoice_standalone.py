# This file is part of the project_invoice_standalone module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
from trytond.tests.test_tryton import suite as test_suite
from trytond.tests.test_tryton import ModuleTestCase


class ProjectInvoiceStandaloneTestCase(ModuleTestCase):
    'Test Project Invoice Standalone module'
    module = 'project_invoice_standalone'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProjectInvoiceStandaloneTestCase))
    return suite
