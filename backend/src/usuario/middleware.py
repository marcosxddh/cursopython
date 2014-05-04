# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl


def execute(next_process, handler, dependencies, **kwargs):
    user = users.get_current_user()
    if user:
        pass
    else:
        dependencies['_usuario_logado'] = None

    next_process(dependencies, **kwargs)
