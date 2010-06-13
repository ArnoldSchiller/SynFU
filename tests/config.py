# encoding: utf-8
#
#  config.py 
#
# Copyright (c) 2010 René Köcher <shirk@bitspin.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modifica-
# tion, are permitted provided that the following conditions are met:
# 
#   1.  Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
# 
#   2.  Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MER-
# CHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPE-
# CIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTH-
# ERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Created by René Köcher on 2010-04-03.
#

import sys, os, unittest
import synfu.config

class ConfigSuite(unittest.TestCase):
    def setUp(self):
        self._data_path     = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
        
        self._cfg = [
            ('postfilter', os.path.join(self._data_path, 'config_00_mandatory_00_synfu.conf')),
            ('reactor'   , os.path.join(self._data_path, 'config_00_mandatory_01_synfu.conf'))
        ]
    
    def test_00_mandatory(self):
        for (what, path) in self._cfg:
            sys.stderr.write('\n    {0}..'.format(what))
            
            self.assertRaises(RuntimeError, synfu.config.Config, path, {})
            
        sys.stderr.write('\n -- ')
