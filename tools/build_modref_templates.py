#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""Script to auto-generate our API docs.
"""
# stdlib imports
import os

# local imports
from apigen import ApiDocWriter

#*****************************************************************************
if __name__ == '__main__':
    package = 'formula'
    outdir = os.path.join('api','generated')
    docwriter = ApiDocWriter(package)
    docwriter.package_skip_patterns += [r'\.fixes$',
                                        r'\.externals$',
                                        #r'\.neurospin\.viz',
                                        ]
    docwriter.write_api_docs(outdir)
    docwriter.write_index(outdir, 'gen', relative_to='api')
    print '%d files written' % len(docwriter.written_modules)
