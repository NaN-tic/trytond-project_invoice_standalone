# This file is part project_invoice_standalone module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from . import work


def register():
    Pool.register(
        work.Work,
        module='project_invoice_standalone', type_='model')
