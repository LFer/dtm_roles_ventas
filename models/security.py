# -*- coding: utf_8 -*-
from openerp import models, fields, _, api, exceptions
from openerp.tools.misc import DEFAULT_SERVER_DATE_FORMAT
import locale
import time
import logging
import ipdb as pdb
from openerp.exceptions import Warning
_logger = logging.getLogger(__name__)


class security(models.Model):
    _name = 'security'

security()


