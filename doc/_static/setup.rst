Setup
======

Installation
-------------

SynFU is distributed as a platform independent `python-egg`_.
You can either download the egg from `PyPi <http://pypi.python.org>`_ the Python package index, unpack it and run :command:`setup.py` like this:

	~/> curl -O http://pypi.python.org/packages/source/s/synfu/SynFu-|version|.tar.gz
	
	~/> tar -xzf SynFu-|version|.tar.gz
	
	~/> cd SynFU-|version|
	
	~/> sudo python ./setup.py install

Or simply issue the command :command:`sudo easy_install SynFU`.

Either way will install SynFU in your python site-packages directory
and create a set of wrapper scripts in /usr/bin [#]_.

Configuration
--------------

Configuration is done in the file :download:`synfu.conf`.
This file contains three YAML_ streams defining the settings
for :ref:`synfu-reactor` as well as :ref:`synfu-news2mail`/:ref:`synfu-mail2news` and :ref:`synfu-imp`.

Each configuration section starts with a tag in the form:

.. code-block:: yaml

	--- !<tag:news.bgepartei.de,YEAR:synfu/MODULE>

With *YEAR* marking the initial release of a module and *MODULE* identifying
the specific module:

	- reactor: :ref:`synfu-reactor` (year: 2009)
	- postfilter: :ref:`synfu-mail2news` and :ref:`synfu-news2mail` (year: 2009)
	- imp: :ref:`synfu-imp` (year: 2010)

Detailed information about the supported options and their possible values can be found in the :ref:`tools` section and a complete example is available in :ref:`appendix-a` .

If you don't provide the absolute config path SynFU will search the following places in order:

	- ./synfu.config
	- /etc/synfu.config
	- /usr/local/etc/synfu.config

	- user specifed paths


Integration with INN
_____________________

Since :ref:`synfu-news2mail` works as a drop-in replacement the only
changes needed to the INN configuration is the removal of the old
news2mail line and the addition of the following line to */etc/news/newsfeeds*:

.. code-block:: bash

	# Replace the default news2mail line with this one
	synfu:*/!bgepartei:Tc,Ac,WnN:/usr/local/bin/synfu-news2mail


Integration with Mailman (via Procmail)
---------------------------------------

To feed mailing lists through :ref:`synfu-mail2news` you need a working `procmail`_ setup [#]_.
Once things are in place just add the following line to filter and distribute all messages as needed:

.. code-block:: bash

	# -------------------------------
	# distribute messages using SynFU
	# -------------------------------
	:0 H:mailpost.lock
	| synfu-mail2news



.. [#] The binary directory may vary depending on your OS,
	  	your distribution and your system configuration.

.. [#] The setup and configuration of procmail is beyond the
	    scope of this document.

.. _`python-egg`: http://pypi.python.org/pypi/setuptools
.. _`yaml`: http://www.yaml.org/
.. _`procmail`: www.procmail.org/

Task scheduling (via cron)
-------------------------------

To setup :ref:`synfu-imp` for periodic task execution just add a line like the following to your favorite cron system:

.. code-block:: bash

	# cleanup newsgroups file each day at 11:50pm - cron format
	50 11 * * * news /usr/bin/synfu-imp --jobs=GroomNewsgroups -- >/dev/null

