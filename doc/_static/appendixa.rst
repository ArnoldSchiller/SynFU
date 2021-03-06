.. _appendix-a:

Appendix A: Synfu example config
=================================

The following synfu.conf was taken from a test system
and represents a working sample.

.. code-block:: yaml

        --- !<tag:news.bgepartei.de,2009:synfu/reactor>
        settings:
              outlook_hacks  : yes
              complex_footer : yes
              strip_notes    : no
              verbose        : yes
              verbosity      : 2

        --- !<tag:news.bgepartei.de,2009:synfu/postfilter>
        settings:
              inn_sm         : /usr/lib/news/bin/sm
              inn_host       : news.bgepartei.de
              verbose        : yes
              verbosity      : 2
              default_sender : mail2news@bgepartei.de
              mail2news_cmd  : |
                /usr/local/bin/synfu-reactor |
                /usr/lib/news/bin/mailpost -b /tmp -x In-Reply-To:User-Agent -d bgepartei {0[NNTP_ID]}
              news2mail_cmd  : |
                /usr/sbin/sendmail -oi -oem -ee -odq -f "{0[FROM]}" -p "NNTP:{0[HOST]}" {1}

        filters:

            - nntp : bgepartei.de.region.hh.misc
              smtp : .*list.hh.aktive
              from : aktive@bgepartei-hamburg.de
              sender: mail2news@nordbge.de
              force_tag: PPD-HH
              
            - nntp : bgepartei.de.region.hh.test
              smtp : .*test.lists.bgepartei-hamburg.de
              from : test@bgepartei-hamburg.de
              sender: mail2news@nordbge.de

            - nntp : bgepartei.de.test
              smtp : .*test.lists.bgepartei.de
              from : test@lists.bgepartei.de
              force_tag: PPD-HH
              description : Fixed description for GroomNewsgroups

            - nntp : bgepartei.de.talk.politik.etc.pflege
              smtp : .*ag-pflege.lists.bgepartei.de
              from : ag-pflege@lists.bgepartei.de

            - nntp : bgepartei.de.region.nw.ak.gesundheit
              smtp : .*nrw-ak-gesundheit.lists.bgepartei.de
              from : nrw-ak-gesundheit@lists.bgepartei.de

            - nntp : bgepartei.de.talk.politik.etc.pflege
              smtp : .*ag-pflege.lists.bgepartei.de
              from : ag-pflege@lists.bgepartei.de

            - nntp : bgepartei.de.talk.politik.etc.gesundheit
              smtp : .*ag-gesundheitswesen.lists.bgepartei.de
              from : ag-gesundheitswesen@lists.bgepartei.de

            - nntp : bgepartei.de.region.sn
              smtp : .*sachsen.lists.bgepartei.de
              from : sachsen@lists.bgepartei.de

            - nntp : bgepartei.de.region.he.darmstadt
              smtp : .*darmstadt.bgepartei-hessen.de
              from : darmstadt@bgepartei-hessen.de

            - nntp : bgepartei.de.region.ni.misc
              smtp : .*aktive-nds.lists.bgeserver.de
              from : aktive-nds@lists.bgeserver.de

            - nntp : bgepartei.de.region.ni.braunschweig
              smtp : .*braunschweig.lists.bgepartei-niedersachsen.de
              from : bs-bge@gomex.de

            - nntp : bgepartei.de.region.rp.neustadt
              smtp : .*rlp-neustadt@lists.bgepartei.de
              from : rlp-neustadt@lists.bgepartei.dee

            - nntp : bgepartei.de.region.sh.misc
              smtp : .*diskurs.lists.bgepartei-sh.de
              from : diskurs@lists.bgepartei-sh.de
              sender: mail2news@nordbge.de

            - nntp : bgepartei.de.region.sh.announce
              smtp : .*ankuendigungen.lists.bgepartei-sh.de
              from : ankuendigungen@lists.bgepartei-sh.de
              sender: mail2news@nordbge.de

    --- !<tag:news.bgepartei.de,2010:synfu/imp>
        settings:
            verbose    : yes
            verbosity  : 3
            jobs:
                groom_newsgroups:
                    newsgroups : tests/data/misc/newsgroups
    #                http_proxy : http://host:port
    #                https_proxy: http://host:port

                    listinfo:
                        - host: lists.bgepartei.de
                          info: https://service.bgepartei.de/mailman/listinfo

...
