

## 2.99 - 3.0.X

- Experimantal versions supporing python 3.9 and later only
- Include latest pydal, rocket3, yatl

## 2.27

- python 3.11 support
- linted and formatted code

## 2.26

- fixed invalid headers and header serialization bug
- fixed circular imports
- fixed a header injection vulnerability

## 2.25

(never released)

## 2.24

- fixed vulnerability JVN#80476432
- fixed issue #2468
- fixed issue #2457
- fixed issue #2457
- initialize env with abspath
- fixed application packaging
- fixed hmac.new digestmod
- fixed cache corruption issue

## 2.23

- fixed internal error in map_static() on self.args=None
- fixed corner cases in prevent_open_redirect
- fixed #2451, invalid chars in german translation
- prevent admin app from accessing files outside the applications folder
- fixed migration and virtual fields
- callable auth.settings.auth_two_factor_enabled
- added DKIM support to emails

## 2.22

- pydal upgrade
- yatl upgrade
- improved open redirect prevention
- fixed problem with gmail attachments
- fixed #2432
- made simplejsonrpc compatible with python3.8+
- fixed reload from _compat so it works in py3
- fixed bug with filenames and = in the url
- fixed #2425
- fixed copyreg import for python2
- fixed #2330
- fixed oauth2.0 to work with python 3
- added Ubuntu 20.04+Apache+Python3 installation script
- fixed #2400, in rocket fixed SSL DoS issue in accept loop
- added python 3.9 support

## 2.21	

- fixed exception handling for packed file creation
- fixed handling of filenames with non-ascii characters in attachments	
- fixed issue #2312
- added hash_extension functionality to URL
- fixed order keyword value in Grid column sort
- cleanup in strings and regex
- fixed handling of smtplib.SMTPException
- fixed SCRIPT(ASSIGNJS(foo=bar))
- fixed issue #2326
- fixed issue #2315
- removed Python 3.5 support

## 2.20.1

new makefile to update binaries from Nico Zanferrari

## 2.19.0
- new command line options (Thanks Paolo Pastori)

OLD NAME                   NEW NAME
==================         ==================
--debug                     --log_level
--nogui                     --no_gui
--ssl_private_key           --server_key
--ssl_certificate           --server_cert
--minthreads                --min_threads
--maxthreads                --max_threads
--profiler                  --profiler_dir
--run-cron                  --with_cron
--softcron                  --soft_cron
--cron                      --cron_run
--cronjob *                 --cron_job *
--test                      --run_doctests
                            --add_options
                            --interface
                            --crontab

## 2.18.1-2.18.5
- pydal 19.04
- made template its own module (Yet Another Template Language)
- improved python 3.4-3.7 support
- better regular expressions
- bug fixes

## 2.17.1-2
- pydal 18.08
- many small bug fixes

## 2.16.1
- pydal 17.11
- bootstrap 4 
- better welcome examples
- many bug fixes

## 2.15.1-4
- pydal 17.08
- dropped support for python 2.6
- dropped web shell
- experimental python 3 support
- experimental authapi for service login
- allow ajax file uploads
- more tests
- more pep8 compliance
- d3.js model visulization
- improved scheduler
- is_email support for internationalized Domain Names
- improved used of cookies with CookieJar
- SQLFORM.grid(showblobs=True)
- import JS events (added w2p.componentBegin event)
- added support for CASv3
- allow first_name and last_name placeholders in verify_email message
- added three-quote support in markmin
- updated pg8000 driver (but we still recommend psycopg2)
- compiled views use . separator not _ separator (must recompile code)
- better serbian, french, and catalan translations
- speed improvements (refactor of compileapp and pyc caching)
- removed web shell (never worked as intended)
- allow Expose(..., follow_symlink_out=False).
- Updated fpdf to latest version
- JWT support
- import fabfile for remote deployment
- scheduler new feature: you can now specify intervals with cron
- gluon/* removed from sys.path. Applications relying on statements like e.g.
  "from storage import Storage"
  will need to be rewritten with
  "from gluon.storage import Storage"
- tests can only be run with the usual web2py.py --run_system_tests OR with
  python -m unittest -v gluon.tests on the root dir
- jQuery 3.2.1
- PyDAL 17.07 including:
  allow jsonb support for postgres
  correctly configure adapters that need connection for configuration
  better caching
  updated IMAP adapter methods to new API
  experimental suport for joinable subselects
  improved Teradata support
  improved mongodb support
  overall refactoring
  experimental support for Google Cloud SQL v2
  new pymysql driver

## 2.14.6

- Increased test coverage (thanks Richard)
- Fixed some newly discovered security issues in admin:
  CSRF vulnerability in admin that allows disabling apps
  Brute force password attack vulnerability in admin
  (thanks Narendra and Leonel)

## 2.14.1-5

- fixed two major security issues that caused the examples app to leak information
- new Auth(…,host_names=[…]) to prevent host header injection
- improved scheduler
- pep8 enhancements
- many bug fixes
- restored GAE support that was broken in 2.13.*
- improved fabfile for deployment
- refactored examples with stupid.css
- new JWT implementation (experimental)
- new gluon.contrib.redis_scheduler
- myconf.get
- LDAP groups (experimental)
- .flash -> .w2p_flash
- Updated feedparser.py 5.2.1
- Updated jQuery 1.12.2
- welcome app now checks for version number
- Redis improvements. New syntax:

    BEFORE:
    from gluon.contrib.redis_cache import RedisCache
    cache.redis = RedisCache('localhost:6379',db=None, debug=True)

    NOW:
    from gluon.contrib.redis_utils import RConn
    from gluon.contrib.redis_cache import RedisCache
    rconn = RConn()
    # or RConn(host='localhost', port=6379,
    # db=0, password=None, socket_timeout=None,
    # socket_connect_timeout=None, .....)
    # exactly as a redis.StrictRedis instance
    cache.redis = RedisCache(redis_conn=rconn, debug=True)

    BEFORE:
    from gluon.contrib.redis_session import RedisSession
    sessiondb = RedisSession('localhost:6379',db=0, session_expiry=False)
    session.connect(request, response, db = sessiondb)

    NOW:
    from gluon.contrib.redis_utils import RConn
    from gluon.contrib.redis_session import RedisSession
    rconn = RConn()
    sessiondb = RedisSession(redis_conn=rconn, session_expiry=False)
    session.connect(request, response, db = sessiondb)

Many thanks to Richard and Simone for their work and dedication.

## 2.13.*

- fixed a security issue in request_reset_password
- added fabfile.py
- fixed oauth2 renew token, thanks dokime7
- fixed add_membership, del_membership, add_membership IntegrityError (when auth.enable_record_versioning)
- allow passing unicode to template render
- allow IS_NOT_IN_DB to work with custom primarykey, thanks timmyborg
- allow HttpOnly cookies
- french pluralizaiton rules, thanks Mathieu Clabaut
- fixed bug in redirect to cas service, thanks Fernando González
- allow deploying to pythonanywhere from the web2py admin that you're running locally, thanks Leonel
- better tests
- many more bug fixes

## 2.12.1-3

- security fix: Validate for open redirect everywhere, not just in login()
- allow to pack invidual apps and selected files as packed exe files
- allow bulk user registration with default bulk_register_enabled=False
- allow unsorted multiword query in grid search
- better MongoDB support with newer pyDAL
- enable <app>/appadmin/manage/auth by default for user admin
- allow mail.settings.server='logging:filename' to log emails to a file
- better caching logic
- fixed order of confirm-password field
- TLS support in ldap
- prettydate can do UTC
- jquery 1.11.3
- bootstrap 3.3.5
- moved to codecov and enabled appveyor
- many bug fixes

## 2.11.1

- Many small but significative improvements and bug fixes

## 2.10.1-2.10.2

- welcome app defaults to Bootstrap 3
- DAL -> pyDAL (thanks Giovanni, Niphlod, Paolo)
  - new modular dal
  - fixed problems with GAE support
  - moved to full NDB support
  - improved connection pooling logic
- optional cache.ram.max_ram_utilization = 90 (experimental)
- improved cache.disk logic (thanks Niphlod and Leonel)
- lots of pep8 improvements, thanks Richard
- added support for email attchments when auth.settings.server='gae'
- fixed app.yaml.example for GAE
- fixed many small issues
- many many more tests (thanks Giovanni, Niphlod, Paolo)
- upgrading static libraries (bootstrap, codemirror, jquery, etc)

## 2.9.12

- Tornado HTTPS support, thanks Diego
- Modular DAL, thanks Giovanni
- Added coverage support, thanks Niphlod
- More tests, thanks Niphlod and Paolo Valleri
- Added support for show_if in readonly sqlform, thanks Paolo
- Improved scheduler, thanks Niphlod
- Email timeout support
- Made web2py's custom_import work with circular imports, thanks Jack Kuan
- Added Portuguese, Catalan, and Burmese translations
- Allow map_hyphen to work for application names, thanks Tim Nyborg
- New module appconfig.py, thanks Niphlod
- Added geospatial support to Teradata adaptor, thanks Andrew Willimott
- Many bug fixes



## 2.9.6 - 2.9.10

- fixed support of GAE + SQL
- fixed a typo in the license of some login_methods code. It is now LGPL consistently with the rest of the web2py code. This change applied to all previous web2py versions.
- support for SAML2 (with pysaml2)
- Sphinx documentation (thanks Niphlod)
- improved scheduler (thanks Niphlod)
- increased security
- better cache.disk (thanks Leonel)
- sessions are stored in subfolders for speed
- postgres support for "INSERT ... RETURING ..."
- ldap support for Certificate Authority (thanks Maggs and Shane)
- improved support for S/Mime X.509 (thanks Gyuris)
- better welcome app
- support for Collection+JSON Hypermedia API (RESTful self documenting API)
- jQuery 1.11
- codemirror 4.0.3
- markdown2 2.2.3
- memcache 1.53
- support for the new janrain API
- new "web2py.py -G config" to make GAE configuration easier
- many small bug fixes

## 2.9.1 - 2.9.5

- many small but important bug fixes
- jquery 1.11
- codemirror 3.21, thanks Paolo Valleri
- fixed security issue with sessions in database, thanks Nathan Humphreys
- fixed security issue with persistant data in session, thanks Kiran
- fixed security issue with redirect after expired login, thanks André Kablu
- cleaner DAL and rname integration, thanks niphlod and Michele
- added mongodb and imap tests for dal, thanks Alan
- NoSQL dal tests, thanks Alan
- better docstrings, thanks Niphlod
- allow URL(...,language=...) with parametric router, thanks Jonathan
- allow non-expiration of gae-memcache, thanks crimsoncantab
- MARKMIN(...,_class='...'), thanks Luca
- better transliteration in building slugs
- autolink emails
- new Janrain API, thanks PeterQ2
- enable admin app for GAE (experimental), thanks Alan
- many bug fixes
- invalidate function in web2py.js, thanks Paolo
- DAL(...,adapter_args=dict(engine='MyISAM'))
- todolist panel in admin editor, thanks Paolo Valleri

## 2.8.1

- no more winservice (use nssm instead)
- better imap support in DAL
- db().select().as_tree()
- bootstrap 2.3.2
- codemirror 3.19
- improved  mongoDB support, thanks Alan
- support for wiki custom render function
- Wiki(...groups=['x','y']) allows bypassing default permissions
- fixed websocket_messaging.py to support newer Tornado
- NDB support for GAE, thanks Quint
- fixed major concurrecy issue with MEMDB
- blocked generic.jsonp for security reasons
- many bug fixes, thanks Niphlod, Michele, Anthony, Tim, and many others.

## 2.7.1 - 2.7.4

- jQuery 1.10.2
- codemirror 3.18, thanks Paolo
- namespaces in T("Welcome", ns="namespace"), thanks jamarcer (experimental)
- more Auth options, thanks Charles
- more admin configuration, thanks Roberto
- new gluon.contrib.strip.StripeForm for PCI compliant payments
- webclient can hendle lists, thanks Yair
- allows SQLFORM.grid(...,ignore_common_filters=True)
- more translations, thanks Vladyslav
- better session2trash.py, works with scheduler, thanks niphlod
- fixed problem with ENABLED/DISABLED
- many bug fixes, thanks niphlod, michele, anthony, roberto, tim, and others

## 2.6.1 - 2.6.4

Attention all users: For pre 2.6 applications to work with web2py >=2.6, you must copy static/js/web2py.js, controllers/appadmin.py, and views/appadmin.html from the welcome app to your own apps (all of them).

Attention production users: The updated handlers and examples are in handlers/ and examples/. The updated ones will not override the existing ones. To use the new ones it is not sufficient to upgrade web2py, you also need to copy the desired handler/example in the root web2py/ folder.

Attention MySQL users: The length of string fields changed from 255 to 512 bytes. If you have migrations enabled this will trigger a large migration. To prevent it, first set migrate_enabled=False, upgrade, check everything is ok, then add length=255 to your string Fields, then re-enable migrations with migrate_enabled=True if needed.

- better directory structure: handlers/ extras/ examples/
- better MongoDb support, thanks Alan
- better Admin editor interface, thanks Paolo, Roberto (codemirror 3), and Lightdot
- better layout.html and web2py_bootstrap.css, thanks Paolo
- refactored web2py.js makes code more readable, thanks Niphlod
- compute fields can depend on other compute(d) fields
- more functions in appadmin (/manage/auth), thanks Anthony
- support for CAST in SQL generation
- new API jQuery('#component').reload()
- new API rows.render()
- new API table.field.referent, table._references
- new API db(...).validate_and_update(...)
- new API Wiki(..., force_render=True) renders the page source again instead of using cached
- Wiki now automatically parses named component arguments @{f:a=1,b='twp',c=variable}
- auth.get_or_create_user(login=False)
- auth = Auth(crsf_protection = False) prevents creating sessions in login/register forms.
- enable multiple renderers in wiki, thanks Alan
- log messages from Auth are no longer translated (for speed and readability)
- update jQuery mobile to 1.3.1
- reduced memory footprint by conditionally loading Tk
- faster pbkdf2 uses OpenSSL, thanks Michele
- many speed improvements, thanks Michele
- better session logic, prevents false positive when detecting session changes.
- scripts/import_static.py converts a static site to a web2py app (experimental)
- support for new http error code 451
- profiler saves dump in dir, thanks Niphlod
- upgraded pyfpdf, thanks Mariano
- gluon/contrib/pdfinvoice.py for generating PDF invoices (assumes reportlab)
- no more double submission of forms (even without crsf protection), thanks Niphlod
- speedup for define_table, thanks Michele
- settings.cfg to admin, thanks Paolo
- many bugs fixed, thanks Niphlod, Michele, Roberto, Jonathan, and many others
- 2.6,3 specifically fixed a possible DoS vulnerability
- 2.6.4 specifically fixes major problem introduced in 2.6.1 with session logic

## 2.5.2

- Web editor with tabs, thanks ilvalle

## 2.5.1

- New style virtual fields in grid
- Conditional fields (experimental) ``db.table.field.show_if = db.table.otherfield==True`` or ``db.table.field.show_if = db.table.otherfiel.contains(values)``
- auth.settings.manager_group_role="manager" enables http://.../app/appadmin/auth_manage and http://.../app/appadmin/manage for members of the "manager" group. (also experimental)
- support for POST variables in DELETE
- Fixed memory leak when using the TAG helper


## 2.4.7

- pypy support, thanks Niphlod
- more bug fixes
- ...

## 2.4.6

- better tests
- new ANY_OF and IS_IPV6 validators
- new custom save option
- many small bug fixes

## 2.4.5

- travis.ci integration (thanks Marc Abramowitz and Niphlod). Passes all tests (thanks Niplod).
- IS_DATE and IS_DATETIME can specify timezone

## 2.4.1- 2.4.3

- 2D GEO API: geoPoint, getLine, geoPolygon
- support for 'json' field type in DAL
- schema export with db.as_json/as_xml, thanks Alan
- graph representation of models
- support for semantic versioning
- new bootstrap based admin, thanks Paolo
- improved scheduler (and change in scheduler field names), thanks Niphlod
- graphviz support added to adm, thanks Jose
- on_failure in grid
- db.table.field.abs()
- better wiki
- geoPoint, getLine, geoPolygon
- better reporting of 500 ajax errors
- better grid
- improved/fixed mongodb support
- improved parse_as_rest(patterns=...), thanks Denes
- improved IMAP DAL support, thanks Alan
- improved security when cookies in sessions
- Row.as_xml, as_json, as_dict, as_yaml thanks Alan
- smarter custom_import
- setup-ubuntu-12-04-redmine-unicorn-web2py-uwsgi-nginx.sh
- added support for motor and pulsar servers, thanks Niphlod
- added json-rpc2 support
- added pypyodbc.py driver
- allow auth.settings.ondelete='CASCADE'
- new syntax IS_EXPR(lambda value: ...
- using google for QR codes (although Graph API will be deprecated in 2015)
- upgraded fpdf to 1.7.1
- bug fixes (including issues with calendar.js and archive tables)

## 2.3.1 - 2.3.2

- new virtual fields syntax:
  ``db.define_table('person',Field('name'),Field.Virtual('namey',lambda row: row.person.name+'y'))``
- db.thing(name='Cohen',_orderby=db.thing.name), thanks Yair
- made many modules Python 3.3 friendly (compile but not tested)
- better welcome css, thanks Paolo
- jQuery 1.8.3
- Bootstrap 2.2.2
- Modernizr 2.6.2 (custom full options)
- integration with analyitics.js (0.2.0)
- better scheduler, thanks Niphlod
- page and media preview in wiki, thanks Niphlod
- create new auth.wiki page from slug model, thanks Nico
- conditional menus with auth.wiki(menugroups=['wiki_editor'])
- better security in grid/smartgrid
- allow LOADing multiple grids, thanks Niphlod
- auth.settings.login_onfail, thanks Yair
- better handling of session files for speed
- added heroku support (experimental)
- added rocket support for IPV6, thanks Chirs Winebrinner
- more customizable menus with MENU(li_first, li_last..)
- added support for paymentech (gluon/contrib/paymentech.py)
- fixed broken cron
- fixed possible xss with share.js
- many bug fixes. Closed more than 50 tickets since 2.2.1

## 2.2.1

- session.connect(cookie_key='secret', compression_level=9) stores sessions in cookies
- T.is_writable = False prevents T from dynamically updating langauge files
- all code is more PEP8 compliant
- better custom_importer behaviour (now works per app, is smalled and faster)
- fixed some bugs
- upgraded feedparser.py and rss2.py
- codemirror has autoresize

## 2.1.0

- overall faster web2py
- when apps are deleted, a w2p copy is left in deposit folder
- change in cron (it is now disabled by default). removed -N option and introduced -Y.
- faster web2py_uuid() and request initialization logic, thanks Michele
- static asset management, thanks Niphlod
- improved mobile admin
- request.requires_https and Auth(secure=True), thanks Yarin and Niphlod
- better custom_import (works per app and is faster), thanks Michele
- redis_sesssion.py, thanks Niphlod
- allow entropy computation in IS_STRONG and web2py.js, thanks Jonathan and Niphlod
- fixed many aith.wiki problems
- support for auth.wiki(render='html')
- better welcome layout, thanks Paolo
- db.define_table(...,redefine=True)
- DAL, Row, and Rows object can now be pickled/unpickled, thanks to zombie DAL.
- admin uses codemirror
- allow syntax auth = Auth(db).define_tables()
- better auth.wiki with preview, thanks Alan
- better auth.impersonate, thanks Alan
- upgraded jQuery 1.8
- upgraded Bootstrap 2.1
- fixed problem with dropbox_account.py
- many fixes to cache.ram, cache.disk, memcache and gae_memcache
- cache.with_prefix(cache.ram,'prefix')
- db.table.field.epoch() counts seconds from epoch
- DAL support for SQL CASE, example: db().select(...query.case('true','false))
- DAL(...,do_connect=False) allows faking connections
- DAL(...,auto_import=True) now retieves some fiel attributes
- mail can specify a sender: mail.send(...,sender='Mr X <%(sender)s>')
- renamed gluon/contrib/comet_messaging.py -> gluon/contrib/websocket_messaging.py

## 2.0.1-11

### DAL Improvements

- Support for DAL(lazy_tables=True) and db.define_table(on_define=lambda table:), thanks Jonathan
- db(...).select(cacheable=True) make select 30% faster
- db(...).select(cache=(cache.ram,3600)) now caches parsed data 100x faster
- db(...).count(cache=(cache.ram,3600)) now supported
- MongoDB support in DAL (experimental), thanks Mark Breedveld
- geodal and spatialite, thanks Denes and Fran (experimental)
- db.mytable._before_insert, _after_insert, _before_update, _after_update, _before_delete. _after_delete (list of callbacks)
- db(...).update_naive(...) same as update but ignores table._before_update and table._after_update
- DAL BIGINT support and DAL(...,bigint_id=True)
- IS_IN_DB(..., distinct=True)
- new syntax: db.mytable.insert(myuploadfield=open(....)), thank you Iceberg
- db(...).select(db.mytable.myfield.count(distinct=True))
- db(db.a)._update(name=db(db.b.a==db.a.id).nested_select(db.b.id))
- db.mytable.myfield.filter_in, filter_out
- db.mytable._enable_record_versioning(db) adds versioning to this table
- teradata adapter, thanks Andrew Willimott
- experimental Sybase Adapter
- added db.table.field.avg()
- Support for Google App Engine projections, thanks Christian
- Field(... 'upload', default=path) now accepts a path to a local file as default value, if user does not upload a file. Relative path looks inside current application folder, thanks Marin
- executesql(...,fields=,columns=) allows parsing of results in Rows, thanks Anthony
- Rows.find(lambda row: bool(), limitby=(0,1))

### Auth improvements

- auth.enable_record_versioning(db)  adds full versioning to all tables
- @auth.requires_login(otherwise=URL(...))
- auth supports salt and compatible with third party data, thanks Dave Stoll
- CRYPT now defaults to pbkdf2(1000,20,sha1)
- Built-in wiki with menu, tags, search, media, permissions. def index: return auth.wiki()
- auth.settings.everybody_group_id
- allow storage of uploads on any PyFileSystem (including amazon)

### Form improvements

- FORM.confirm('Are you sure?',{'Back':URL(...)})
- SQLFORM.smartdictform(dict)
- form.add_button(value,link)
- SQLFORM.grid(groupby='...')
- fixed security issue with SQLFORM.grid and SQLFORM.smartgrid
- more export options in SQLFORM.grid and SQLFORM.smartgrid (html, xml, csv, ...)

### Admin improvements

- new admin pages: manage_students, bulk_regsiter, and progress reports
- increased security in admin against CSRF
- experimental Git integration
- experimental OpenShift deployment
- multi-language pluralization engine
- ace text web editor in admin
- Ukrainian translations, thanks Vladyslav Kozlovskyy
- Romanian translation for welcome, thanks ionel
- support for mercurial 2.6, thanks Vlad

### Scheduler Improvements (thanks to niphlod, ykessler, dhx, toomim)

- web2py.py -K myapp -X starts the myapp scheduler alongside the webserver
- tasks are marked EXPIRED (if stop_time passed)
- functions with no result don't end up in scheduler_run
- more options: web2py.py -E -b -L
- scheduler can now handle 10k tasks with 20 concurrent workers and with no issues
- new params:
    tasks can be found in the environment (no need to define the tasks parameter)
    max_empty_runs kills the workers automatically if no new tasks are found in queue (nice for "spikes" of processing power)
    discard_results to completely discard the results (if you don't need the output of the task)
    utc_time enables datetime calculations with UTC time
- scheduler_task changes:
    task_name is no longer required (filled automatically with function_name if found empty)
    uuid makes easy to coordinate scheduler_task maintenance (filled automatically if not provided)
    stop_time has no default (previously was today+1)
    retry_failed to requeue automatically failed tasks
    sync_output refreshes automatically the output (nice to report percentages)
- workers can be:
    DISABLED (put to sleep and do nothing if not sending the heartbeat every 30 seconds)
    TERMINATE (complete the current task and then die)
    KILL (kill ASAP)

### Other Improvements

- gluon/contrib/webclient.py makes it easy to create functional tests for app
- DIV(..).elements(...replace=...), thanks Anthony
- new layout based on Twitter Bootstrap
- New generic views: generic.ics (Mac Mail Calendar) and generic.map (Google Maps)
- request.args(0,default=0, cast=int, otherwise=URL(...)), thanks Anthony
- redirect(...,type='auto') will be handled properly in ajax responses
- routes in can redirect outside with routes_in=[('/path','303->http://..')]
- better memcache support
- improved spreadsheet, thanks Alan
- new internationalization engine, thanks Vladyslav
- pluralization engine, thanks Vladyslav
- new markmin with support for nested lists, <i>, <em>, autolinks, thanks Vladyslav
- new syntax: {{=BR()*5}}
- gluon.cache.lazy_cache decorator allows caching functions in modules
- .coffee and .less support in response.files, thanks Sam Sheftel
- ldap certificate support
- pg8000 postgresql driver support (experimental)
- @cache('%(name)s%(args)s%(vars)s',5) and cache.autokey
- added tox.ini, thanks Marc
- web2py.py --run_system_tests, thanks Marc Abramowitz
- html.py (and web2py helpers) can be used without web2py dependencies
- new fpdf, thanks Mariano


## 1.99.5-1.99.7
- admin in Russian (Bulat), Japanese (Omi) and Slovenian (Robert Valentak)
- included web-based debugger (experimental, thanks Mariano)
- def index(): return dict(a=gluon.tools.Expose(folder))
- db.table.field.like(...,case_sensitive=False) (thanks Floyd)
- db.table.field.regexp(...) for sqlite and postgres
- db(...,ignore_common_filters=True)
- db(db.dog_id.belongs(db.dogs.owner=='james')).select()
- db(...).select().group_by_value(db.table.field) (thanks Yair)
- db = DAL('imap://user:password@server:port') support (thanks Alan Etkin)
- db = DAL('teradata://DSN=dsn;UID=user;PWD=pass; DATABASE=database') (thanks Adrew Willmott)
- db = DAL('mongodb://127.0.0.1:5984/db') (experimental, thanks Mark Breedveld)
- db = DAL('cubrid')  (experimental)
- db = DAL('postgres:pg8000:...') and DAL('postgres:psycopg2:...')
- pg8000 now ships with web2py (thanks Mariano)
- reponse.delimiters = ('\\[','\\]') (thanks Denes)
- auth.user_groups stores user groups
- auth.is_impersonating()
- populate can now deal with computed fields (thanks Tsvi Mostovicz)
- new rediscache (thanks niphold)
- sync languages capability (thanks Yair)
- improved markmin auto-links
- improved ldap support (thanks Omi)
- added TimeCollector (thanks Caleb)
- better cpdb.py (thanks pasxidis)
- conditional menu items (reponse.menu=[(title,bool,link,[],condition)]
- scripts/services/service.py (thanks Ross)
- gluon/contrib/login_methods/browserid_account.py (thanks Pai)
- gluon/contrib/htmlmin.py for html minimization (thanks kerncece)
- web2py_component has timeout parameter, thanks Alan
- 100's of small bug fixes and small improvements

## 1.99.4
Improved mobile admin, thanks Angelo
Improved examples page, thanks Anthony
fixed a SQLCustomField bug

## 1.99.3
This is a major revision in peparation for web2py 2.0
- moved to GitHub and abandoned Lanchpad
- new web site layout, thanks Anthony
- new welcome app using skeleton, thanks Anthony
- jQuery 1.7.1
- modernizr 2.0.6 (customized)
- ``define_table('thing', singluar='thing',plural='things')``
- CAS 1.0 and 2.0 compliant, thanks Olivier
- fixed validate_and_insert and validate_and_update, thanks Anthony
- ``request.user_agent().is_mobile`` etc., thanks Ross and Angelo
- better router, thanks Jonathan
- app on/off buttons
- support for dropbox_login
- improved markmin recognizes qr code, supports auto audio/video/embed
- ``response.optimize_css = 'concat,minify,inline'``, thanks Ross
- ``response.optimize_js = 'concat,minify,inline'`` thanks Ross
- ``db.define_table(...,common_filter=query)``, thanks Yair
- ``db(...,ignore_common_filter=True)``
- support for stripe payments
- support for DowCommerce payments, thanks Dave
- experimental PyPy support
- experimental mongodb support, thanks Mark
- tickets in db now accessible from admin, thanks Niphlod




## 1.99.1-1.99.2
- gluon/contrib/simplejsonrpc.py
- gluon/contrib/redis_cache.py
- support for A(name,callback=url,target='id',delete='tr')
- support for A(name,component=url,target='id',delete='tr')
- new pip installer, thanks Chris Steel
- isapiwsgihandler.py
- dal expression.coalesce(*options)
- gluon/contrib/simplejsonrpc.py, thanks Mariano
- expire_sessions.py respects expiration time, thanks iceberg
- addressed this issue: http://fuelyourcoding.com/jquery-events-stop-misusing-return-false/
- x509 support (thanks Michele)
- form.process() and for.validate()
- rocket upgrade (1.2.4)
- jQuery upgrade (1.6.3)
- new syntax rows[i]('tablename.fieldname')
- new query syntax field.contains(list,all=True or False)
- new SQLFORM.grid and SQLFORM.smartgrid (should replace crud.search and crud.select)
- support for natural language queries (english only) in SQLFORM.grid
- support for computed columns and additional links in SQLFORM.grid
- new style virtual fields (experimental): db.table.field=Field.Lazy(...)
- request.utcnow
- cleaner/simpler welcome/models/db.py and welcome layout.html
- response.include_meta() and response.include_files(), thanks Denes
- dal auto-reconnect on time-out connections
- COL and COLGROUP helpers
- addresed OWASP #10, thanks Anthony and Eric
- auth.settings.login_after_registration=True
- detection of mobile devices and @mobilize helper (view.mobile.html), thanks Angelo
- experimental gluon/scheduler.py
- scripts/make_min_web2py.py
- crud.search has more options, thanks Denes
- many bug fixes (thanks Jonathan, Michele, Fran and others)

## 1.98.1-1.98.2
- fixed some problems with LOAD(ajax=False), thanks Anthony
- jquery 1.6.2
- gevent.pywsgi adds ssl support, thanks Vasile
- import/export of blobs are base64 encoded
- max number of login attemts in admin, thanks Ross
- fixed joins with alias tables
- new field.custom_delete attribute
- removed resctions on large 'text fields, thanks Martin
- field.represent = lambda value,record: .... (record is optional)
- FORM.validate() and FORM.process(), thanks Bruno
- faster visrtualfields, thanks Howsec
- mail has ssl support separate from tls, thanks Eric
- TAG objects are now pickable
- new CAT tag for no tags
- request.user_agent(), thanks Ross
- fixed fawps support
- SQLFORM(...,separator=': ') now customizable
- many small bug fixes

## 1.97.1
- validate_and_update, thanks Bruno
- fixed problem with new custom import, thanks Mart
- fixed pyamf 0.6, thanks Alexei and Nickd
- fixed "+ =" bug in wizard
- fixed problem with allowed_patterns
- fixed problems with LOAD and vars and ajax
- closed lots of google code tickets
- checkboxes should now work with list:string
- web2py works on Android, thanks Corne Dickens
- new cpdb.py, thanks Mart
- improved translation (frech in particuler), thanks Pierre
- improved cas_auth.py, thanks Sergio
- IS_DATE and IS_DATETIME validators now work with native types
- better description of --shell, thanks Anthony
- extra SQLTABLE columns, thanks Martin
- fixed toolbar conflics, thanks Simon
- GAE password shows with ****

## 1.96.2-1.96.4
- bug fixes

## 1.96.1

- "from gluon import *" imports in every python module a web2py environment (A, DIV,..SQLFORM, DAL, Field,...) including current.request, current.response, current.session, current.T, current.cache, thanks Jonathan.
- conditional models in
  models/<controller>/a.py and models/<controller>/<function>/a.py
- from mymodule import *, looks for mymodule in applications/thisapp/modules first and then in sys.path. No more need for local_import. Thanks Pierre.
- usage of generic.* views is - by default - restricted to localhost for security. This can be changed in a granular way with: response.generic_patterns=['*']. This is a slight change of behavior for new app but a major security fix.

- all applications have cas 2.0 provider at http://.../user/cas/login
- all applications can delegate to login to external provider Auth(...,cas_provider='http://.../other_app/default/user/cas')
- A(...,callback=URL(...),larget='id') does Ajax
- URL(...,user_signature=True), LOAD(...,user_signature=True) can sign urls and @auth.requires_signature() will check the signature for any decorated action.

- DAL(...,migrate_enabled=False) to disable all migrations
- DAL(...,fake_migrate_all=True) to rebuild all corrupted metadata
- new DAL metadata format (databases/*.table)
- DAL(...,adapter_arg={}) allows support for alternate drivers
- DAL now allows circular table defintions
- DAL(..,auto_import=True) automatically imports tables from metadata without need to db.define_table(...)s.
- new alterante syntax for inner joins: db(...).select(join=...)
- experimental cubrid database support
- DAL 'request_tenant' fields are special, the altomatically filer all records based on their default value.
- db._common_fields.append(Field('owner')) allows to add fields to ALL tables
- DAL ignores repeated fields with same names

- web2py_ajax.html is more modular, thanks Anthony
- request.is_local
- request.is_http
- new sessions2trash.py thanks Jim Karsten
- corrupted cache files are automatically deleted
- new simpler API gluon.contrib.AuthorizeNet.procss(...)
- fixed recaptcha (as they released new API)
- messages in validators have default internationalization
- No more Auth(globals(),db), just Auth(db). Same for Crud and Service.
- scripts/access.wsgi allows apache+mod_wsgi to delegate authentication of any URL to any web2py app
- json now supports T(...)
- scripts/setup-web2py-nginx-uwsgi-ubuntu.sh
- web2py HTTP responses now set: "X-Powered-By: web2py", thanks Bruno
- mostly fixed generic.pdf. You can view any page in PDF if you have pdflatex installed or if your html follows the pyfpdf convention.
- auth.settings.extra_fields['auth_user'].append(Field('country')) allows to extend auth_* tables without need of definiting a custom auth_* table. Must be placed before auth.define_tables()
- {{=response.toolbar()}} to help you debug applications
- web based shell now supports object modifications (but no redefinitions of non-serializable types)
- jQuery 1.6.1
- Lots of bug fixes


## 1.95.1
- Google MySQL support (experimental)
- pip support, thanks lifeeth
- better setup_exe.py, thanks meredyk
- importved pyfpdf
- domain check in email_auth.py, thanks Gyuris
- added change_password_onvalidation and change_password_onaccept
- DAL(...,migrate_enabled=True)
- login_methods/loginza.py, thanks Vladimir
- bpython shell support, thanks Arun
- request.uuid and response.uuid (for a future toolbar)
- db._timings contains database query timing info
- efficient db(...).isempty()
- setup-web2py-nginx-uwsgi-ubuntu.sh
- Many bug fixes, thanks Jonathan

## 1.94.6
- fixed a number of minor bugs including adding some missing files
- better session handling on session._unlock(..), thanks Jonathan
- added experimental pip support, thanks Lifeeth
- added experimental SAP DB support

## 1.94.5
- fixed a major bug with session introdued in 1.94.1

## 1.94.4
- removed debug print statement that caused problems on GAE and mod_wsgi

## 1.94.3
- fixed major bug in auth redirection

## 1.94.2
- reverted wrong behavior of auth.requires(condition) in 1.94.1

## 1.94.1
- moderniz 1.17
- web2py no longer saves session if no change, this makes it up up to 10x faster for simple actions
- experimental REST API
- better support for MSSQL NOT NULL
- small bug fixes

## 1.93.1-2
- support for multiple interfaces, thanks Jonathan
- jquery 1.5.1
- simplejson 2.1.3
- customizable simplejson
- leaner app.yaml
- css3 buttons in welcome
- android support (experimental)
- Field(':hidden'), Field('.readonly'), Field('name=value')
- combined expressions print db.data.body.len().sum()
- wizard can download plugins
- better json serilization (object.custom_json)
- better xml serialization (object.custom_xml)
- better formstyle support
- better comet_messaging.py (needs more testing)
- many bug fixes

## 1.92.1
- much improved routing (thanks Jonathan)
- Expression.__mod__ (thanks Denes)
- admin has MULTI_USER_MODE (admin/models/0.py)
- support for count(distinct=...)
- has_permissions(...,group_id)
- IS_MATCH(...,strict=True)
- URL(...,scheme=,host=,port=), thanks Jonathan
- admin in Afrikaans, thanks Caleb
- auth.signature (experimental)
- many other bug fixes

## 1.91.6
- web2py comet via gluon/contrib/comet_messaging.py (html5 websockets) experimental
- fixed problem with services (broken in 1.91.5), thanks Vollrath
- customizable uploadwidget, thanks Fran
- fixed problem with mail unicode support, thanks Richard
- fixed problem with linkto=None and references fields in SQLTABLE, thanks villas
- no more upgrade button on windows since does not work
- better remember-me login, thanks Martin Weissenboeck
- support for recatcha options
- support for GAE namespaces via DAL('gae://namespace')
- new rocket (1.2.2), thanks Tim
- many other bug fixes and improvements (thanks Jonathan)

## 1.91.2-1.91.5
- fixed a problem with deplyment on GAE
- other new dal bug fixes

## 1.91.1
- LICENSE CHANGE FROM GPLv2 to LGPLv3
- URL(...,hash_vars=...) allows to specify which vars need to be signed
- fixed bug with aliasing in new DAL

## 1.90.6
- fix issue with pickling new dal Row and Rows.

## 1.90.5
- set poll = False in rocket because of poll python thread bug often unfixed, thanks Jonathan
- fixes issue with crud and reCaptcha

## 1.90.2-4
- pymysql no longer requires ssl (if not used)
- fixed bug with virtualfields
- fixed bug in truncate (new dal)
- fixed bug in select with alternate primary key (new dal)
- fixed bug with IS_IN_DB and self refences (also new dal)

## 1.90.1
- new DAL (complete rewrite of the web2py DAL is more modular)
- rewrite has fail safe reload, thanks Jonathan
- better CAS with v2 support, thanks Olivier ROCH VILATO
- better markmin2latex
- session.connect(separate=True) to handle many session files, thanks huaiyu wang
- changed bahvior of impersonate (more secure, can generate form or used as API)
- new rocket, thanks Tim
- new pyfpdf
- no more old style classes
- experimental couchdb support in new dal (only insert, select, update by id)
- mysql support out of the box via pymysql
- SQLITABLE(...,headers='labels') thanks Bruno
- optional: digitally signed URLs, thanks Brian Meredyk
- minor bug fixes

## 1.89.1-.5
- new admin layout (thanks Branko Vukelic)
- new admin search
- new admin language selector (thanks Yair)
- new Welcome app (thanks Martin Mulone)
- better wizard
- admin support for DEMO_MODE=True
- admin exposes GAE deployment button (always)
- MENU support None links (thanks Michael Wolfe)
- web2py.py -J for running cron (thanks Jonathan Lundell)
- fixed ~db.table.id on GAE (thanks MicLee)
- service.jsonrpc supports service.JsonRpcException (thanks Matt)
- bug fixes

## 1.88.1-2
- better list: string support, thanks Bob
- jquery 1.4.3
- scripts/autoroutes.py
- new admin wizard
- added retrieve_username to navbar (if username)
- internal rewrite for arbitrary paths (abspath), thanks Jonathan
- populate support for list: and decimal, thanks Chirstian
- markmin2latex has extra attribute
- better mercual admin allows list of files, versions and retrieve
- new error report system, thanks Thadeus and Selecta
- SQLFORM.accepts(detect_record_change).record_changed
- fixed cron for bytecode compiled apps, thanks Álvaro J. Iradier Muro
- other bugs fixes and pep8 compliant fixes

## 1.87.3
- fixed a major bug introduced in 1.87.1 that prevents appadmin from working for new apps created with 1.87.1-2.
- upgraded to clockpick 1.28, thanks villas

## 1.87.1-2
- new layout for examples, thanks Bruno and Martin
- admin allow ``DEMO_MODE=True`` and ``FILTER_APPS=['welcome']``
- fixed a possible problem with CRON and paths


## 1.86.3
- Error reporting on save, thanks Mariano
recalled

## 1.86.1-1.86.3
- markmin2latex
- markmin2pdf
- fixed some bugs
- Storage getfirst, getlast, getall by Kevin and Nathan
- db(db.table), db(db.table.id) both suported and equivalent to db(db.table.id>0)
- postresql ssl support
- less un-necessary logging and warnings on GAE
- IS_DECIMAL_IN_RANGE and IS_FLOAT_IN_RANGE support dot="," (dot="." is default)
- on_failed_authorization can be a function, thanks Niphold
- gluon/contrib/login_methods/cas_auth.py for integration between CAS and Auth.

## 1.85.1-3
- fixed some bugs
- added pyfpdf, thank Mariano

## 1.84.1-4
- flash now stays put in the top right corner
- improved behavior for URL and T objects
- new app level logging with logging.conf (thanks Jonathan)
- improved OpenID (thanks Michele)
- web2py_ajax handles prepend, append, hide (thanks Juris)
- web2py_ajax also handels pre-validation of decimal fields
- ru-ru translation (thanks Michele)
- sk-sk translation (thanks Julius)
- migrations save .table only if changed and after each ALTER TABLE (no more mysql inconsistencies)
- fixed bugs in SQLCustomField, Field(default=...), IS_IMAGE, IS_DECIMAL_IN_RANGE and a few more.
- Better validators (IS_DECIMAL_IN_RANGE, IS_INT_IN_RANGE, etc) thanks Jonatham
- Polymmodel support on GAE
- Experimental ListWidget
- moved DAL and routes to thread.local (thanks Jonathan, again)
- scripts/extract_mysql_models.py, thanks Falko Krause and Ron McOuat
- scripts/dbsessions2trash.py, thanks Scott

## 1.83.2
- mostly cleanup

## 1.83.1
- New error reporting mechanism (thanks Mariano)
- New routing system with app level routing (thanks Jonathan)
- Integrated GAE appstat and GAE precompilation (thanks Scott)
- New Field types "list:string", "list:integer", "list:reference"
- request.cid, request.ajax, A(cid=request.cid), response.js

## 1.82.1
- request.ajax to detect if action is called via ajax, tahnks Jonathan and David Mako
- more captcha options, thanks Vidul
- openid and oauth2 thanks Michele and Keith
- better PluginManager and load components
- new template system, thanks Thadeus
- new db.table(id,[field=value]) and db.table(query) syntax
- URL('index') (no more r=request), thanks Thadeus
- mail.send(message='<html>...</html>', ....)
- DAL([....]) for load balancing
- @service.soap(...) with mysimplesoap, thanks Mariano
- hideerror

## 1.81.5
- Fixed a few bugs. The most important bugs we fixed are in memcache (thanks Scott) and in a process starvation issue with Rocket (thanks Mike Ellis and Tim).

## 1.81.4
- Fixed gluon.tools to work work with load and base.css to nowrap labels

## 1.81.3
- fixed bug in label names in formstyle
- fixed id names in admin test.html page

## 1.81.2
- fixed bug in Auth

## 1.81.1
- rpx (janrain) support out of the box, allows login with Facebook, MySpace, etc. Thanks Mr Freeze
- Increased security (escape  single and double quotes, thanks Craig"
- Fixed a bug with db.table.field.uploadseparate=True and autodelete
- New welcome app with superfish and jQuery 1.4.2
- Deleted openwysiwyg from admin
- In XML and xmlescape quote defaults to True. Both ' and " are escaped. Thanks Craig Younkins

## 1.80.1
- MARKMIN helper (no backward compatibility promise yet)
- self._last_reference, thanks Dave (no backward compatibility promise yet)
- IS_EQUAL_TO
- zh-tw and better internationalization page, thanks Daniel Lin and Iceberg
- better crud.search, thanks MrFreeze
- Rocket interfaces, thanks Nik Klever
- db.table.field.uploadseparate=True, thanks Gyuris
- SCOPE_IDENITY for MSSQL, thanks Jose
- fixed email attachment issue, thanks Bob_in_Comox
- fixed problem with groupby and IS_IN_DB
- other bug fixes
- new implementation for local_import
- ajax(..,...,null)
- fixed Chrome bug in calendar.js, thanks Iceberg
- experimental scrips/web2py-setup-fedora.sh
- generic.load, thanks Iceberg

## 1.79.2
- solved simplejson imcompatibility problem

## 1.79.1
- x509 emails, thanks Gyuris
- attachment and html in Mail on GAE, thanks PanosJee
- fixed docstring in SQLTABLE, thanks aabelyakov
- TAG(html) parese html into helpers (experimental, still some problems with unicode, , thanks RobertVa for unicode help)
- DIV.elements(find=re.compile(....))
- DIV.flatten()
- DIV.elements('....') supports jQuery syntax in '....'
- better it-it.py and it.py, thanks Marcello Della Longa
- Many Bug fixes:
- improved support for DAL and joins in postgresql/oracle, thanks Nico de Groot
- bux fixex in html.py, thanks Ian
- fixed an issue with registration_key==None, thanks Jay Kelkar
- fixed bug in gql.py, thanks NoNoNo
- fixed problem with multiple and checkboxes, thanks MIchael Howden
- fixed bug in gae, thanks NoNoNo
- restored 2.4 compatibility, thanks Paolo Gasparello
- auth.update() when pictures in profile
- formstyle can be a function, thanks Howden
- escape in sanitizer, thanks Howes
- add missing settings, thanks Hamdy
- find and exclude return empty Rows instead of [], thanks iceberg
- simplejson 2.1.1 should fix compatibility problems
- added sms_utils and Authorize.net in contrib

## 1.78.3
- reverted temporarily to old template system because of backward compatibility issues

## 1.78.1
- new template system allows {{block name}}{{end}}, thanks Thadeus
- fixed mime headers in emails, included PGP in emails, thanks Gyuris
- automatic database retry connect when pooling and lost connections
- OPTGROUP helper, thanks Iceberg
- web2py_ajax_trap captures all form submissions, thank you Skiros
- multicolumn checkwidget and arbitrary chars in multiple is_in_set, thanks hy
- Québécois for welcome, thanks Chris
- crud.search(), thanks Mr Freeze
- DAL(...migrate,fake_migrate), thanks Thadeus

## 1.77.3
- some cleanup of code in compileapp

## 1.77.2
- fixed x-index in calendar
## 1.77.1
- Replaced CherryPy with Rocket web server, thanks Tim
- CacheOnDisk allows to specify a folder
- IS_DATE/DATETIME can handle any year since 0
- SQLTABLE(...,headers='fieldname:capitalize')
- Field().with_alias, thanks Nathan and Mengu
- has_membership(group=...,role=...), thank Jonathan
- db.define_table(username=True), thanks Jonathan
- gluon.tools.prettydate
- can specify hostname in routes_out (same syntax as routes in), thanks Martin
- db.table.bulk_insert([...records...]) now works on GAE, thanks Jon
- IS_EMAIL validates on 'localhost', thanks Jonathan
- welcome/views/layout.html uses ez.css, thanks Yarko
- mail attachments support utf8, thanks szimszon
- works with PyPy, thanks Joe
- better Firebird support, thanks Jose
- better Oracle support, thanks Gabriele
- cron supports days of week
- SQLFORM(...,formstyle="table3cols") or "table2cols" or "divs" or "ul"
- crud.settings.formstyle
- web2py.py -f folder allows to specify locations of applications, thanks Iceberg
- better/faster regex in template works in Jython
- fixed lots of small bugs

## 1.76.5
- Fixed a typo in auth that created some registration problems

## 1.76.4
- SQLTABLE(db(db.auth_user.id>0).select(),headers='fieldname:capitalize')
- Oracle limitby improved (thanks Sergey)
- fixed migrations in Firebird, thanks Jose Jachuf
- gluon/contrib/login_methods/linkedin_account.py (to be tested)

## 1.76.2-1.76.3
- major fix in cron (will I ever get this 100% right?)
- fix in delete for GAE
- auth.settings.login_captcha and auth.settings.register_captcha
- crud.settings.create_captcha and  crud.settings.update_captcha
- automatic update button in admin

## 1.76.1
- editarea 0.8.2 + zencoding
- new (better) cron locking meachnism
- no storing session cookies on session.forget(), thank you Alvaro
- routes_apps_raw allows disabling of request.args validation, thanks Jonathan and Denes
- fixed problem with edit_languages ad multiple tabs, thanks Iceberg
- crud captcha, thanks you Nathan
- softcron disabled by default in wsgihandler and fcgihandler

## 1.75.5
- fixed behaviour with languages.py, thanks Iceberg
- added chinese (thanks Iceberg) and Hungarian (thanks Gyuris)
- fixed problem with GAE deleted by id (thanks what_ho)
- fixed bug in LOAD with custom views, thanks vhang
- improved IS_IN_SET takes iterator, dict, list and list of tuples, thanks Iceberg
- Auth(...,controller='default')
- Fixed major bug in parsing repeated request.vars, thanks Ben
- IS_DATE and IS_DATETIME can now handle any 0<year
- allow to disable editarea onload, thanks Alex

## 1.75.4
- customizable BEAUTIFY, thanks John

## 1.75.3
- added support for PAM authentican for apps and for admin
- INTRODUCED MAJOR BUG IN BEAUTIFY (upgrade to 1.75.4) IMMEDIATELY

## 1.75.2
- fetch supports cache
- curd.update(....,onaccept=crud.archive) magic
- new UUID mechnism fixes session conflicts with cloned machine in cloud
- allow to upload app and overwrite existing old ones, thanks Jonathan
- print gluon.tools.prettydate(request.now,T), thanks Richard

## 1.75.1
- better cron
- better fetch
- logging of email failures
- new web2py.fedora.sh
- new setup-web2py-ubuntu.sh
- experimental autocomplete
- menus work on IE6

## 1.74.9
- IS_IN_SET(((0,'label0'),(1,'label1'))), thanks Falko Krause
- SQLFORM(...).accpets stores True or False in boolean types no None, thanks Frederik Wagner
- SQLFORM.factory(...,table_name='no_table'), thanks Thedeus
- jQuery 1.4.1
- Fixed major problem with internationalization of multiple languages.
- Fixed a serius security issue with login
- Possibly fixed some issues with cron

## 1.74.8
- IS_SLUG, thanks Gustavo and Jonathan
- web2py.py -nogui, thanks Jeff Bauer
- solved a problem with jython, thanks Tim Farrel
- login has "remember be option", thanks Piotr Banasziewicz
- fixed problem with keepvalue in update forms, thanks Miguel Lopez

## 1.74.7
- request_password_reset and password reset verification
- python web2py.py -S app -M -R script.py -A arg1 arg2 arg3
- T("%(a)s") % dict(a="hello")

## 1.74.6
- bug fixes
- IS_IN_DB(...,_and=IS_NOT_IN_DB)
- Smaller populate, thanks Piotr
- better slicing of fields, thanks Michael Fig
- Cache stats, thanks Thadeus
- Better gql.py
- IS_IN_DB and IS_IN_SET default to zero='', no longer zero=None

## 1.74.5
- bug fixes
- restored python 2.4 support,thanks ont.rif
- support for native types on Google App Engine
- cache.ram usage statictics, thanks Thadus
- no more auth manu in scaffolding
- no more spash screen with -Q
- fixed doctest in html.py, thanks Anand Vaidya
- export_to_csv_file has represent, thanks Thadeus

## 1.74.2-4
- Fix bugs including including unicode in emails and blobs on GAE

## 1.74.1
- Moved to mercurial
- Default validators use the new define_table(....,format='...')
- New get_vars and post_vars compatible in 2.5 and 2.6 (thanks Tim)
- Major rewrite of gql.py extends DAL syntax on GAE
- No more *.w2p, welcome.w2p is create automatically, base apps are always upgraded
- export_to_csv(delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL), thanks Thadeus

## 1.73.1
- Fixed problem with storage and comparison of Row objects
- Fixed problem with mail on GAE
- Fixed problem with T in IS_DATE(TIME) error_message and format
- Rows[i].delete_record()
- Even better support for legacy databases
- Experimantal support for non UTF8 encoding in DB
- Better IPV4 (thanks Thandeus)
- T.current_languages default to 'en' and new T.set_current_languages(...) (thanks Yarko)
- INPUT(...,hideerror=False) used to fix rare chechbox widget problem
- Admin allows change of admin password
- New gluon/contrib/populate.py
- Size of input/textarea set by CSS no more by jQuery  (thanks Iceberg)
- Customizable CSV  (thanks Thandeus)
- More bug fixed (thanks Thandeus)
- Better regex for template fixed Jython problem (thank Jonathan)

## 1.72.1 - 1.72.3
- Better support for legacy databases

## 1.71.1
- Complete rewrite of Rows
- renamed DALStorage->Rows, DALRef->Reference
- Experimental serializarion of Row and Rows (get serialized to dict and list of dict)
- DAL(...,folder) and template.render(content=, context=) make it more modular

## 1.70.1
- Fixed bug with Rows.as_list and DALRef
- Added Rows.as_dict (thanks Mr Freeze and Thedeus)
- Added request.wsgi (thanks hcvst) allows running wsgi apps under web2py and applying wegi middleware to regular web2py actions that return strings.
- Experimental distributed transactions between postgresql, mysql and firebird
- Finally local_import is here!

## 1.69.1
- Fixed a bug introduced in 1.68 about inserting unicode in DAL
- Fixed other small bugs
- Better support for legacy databases (thank Denes)
- response.meta replaces response.author, response.keywords, response.description
- response.files stets dependes in plugins
- better admin for packing/unpacking plugins
- reference fiels nor evaluate to DALRef with lazy evaluation (cool, thanks Mr Freeze)
- can insert a record in place of a reference
- record[e] instead of record._extra[e] (tentatively!)
- record.update_record() with no args
- rows.find()  (thanks Mr Freeze)
- rows.exclude()
- rows.sort()
- rows[:]

## 1.68.2
- Fixing bug with admin and missing crontab
- Fixing bug with rewrite.load on GAE (thanks Willian Wang)

## 1.68.1
- New official markdown with security fix
- rows.first()
- rows.last()
- New cron
- New hindi and spanish translation
- cached uploads allow for progress bars (thanks AndCycle)
- ingres support (thanks Chris)
- legacy database support for db2, mssql with non-int primary keys (thanks Denes)
- default setting of content-type (this may cause strange behavior in old apps when downloading images)
- IS_UPPER and IS_LOWER works with unicode
- CLENUP not takes regex of allowed/now allowed chartares
- New rewrite.py allows dynamic routes
- Better error messages for IS_INT_* and IS_FLOAT_*

## 1.67.2
- Security fix in markdown

## 1.67.1
- Bux fixed

## 1.67.0
- Python 2.4 support (again)
- New layout for welcome
- changed defauld field sizes to 512
- Field(uploadfolder="...")
- appadmin works on GAE (again, somehting got broken at some point)
- new wsgiserver 3.2.0 should fix recurrent broken download problems

## 1.66
- new doctypes
- form.vars.newfilename
- new HTML and XHTML helpers
- better IS_LENGTH

## 1.65.13
- request.url (thanks Jonathan)
- restored uploadfield_newfilename
- new examples layout nad logo (thanks Mateusz)

## 1.65.12
- lables in auth auto-translate (thanks Alvaro)
- better ldap_auth (thanks Fran)
- auth chacks locally for blocked accounts even for alternate login methods (thanks Fran)

## 1.65.11
- Fixed a sqlhtml bug with image upload

## 1.65.3-10
- Fixed some small bugs and typos in the docstrings
- Fixed AMF3 support

## 1.65.2
- Fixed some small auth bugs
- Field.store(...)

## 1.65.1
- spreadsheet
- shell history, thanks sherdim
- crontab editor, thanks Angelo
- gluon/contrib/login_methods/cas_auth.py (thanks Hans)
- DAL(...) instead of SQLDB(...)
- DAL('gae') instead of GQLDB()
- Field instead of SQLField
- (the old syntax still works)

## 1.65
- reST docstrings for Sphinx, thanks Hans
- gluon/conrtib/login_methods/gae_google_account.py for google CAS login on GAE, thanks Hans
- fixed problem with Auth and Firebird 'password' issue
- new auth.settings.create_user_groups
- tickets stored on datastore on GAE and also logged, thanks Hans
- imporved IS_LENGTH with max and min, thanks Mateusz
- improved IS_EMAIL with filters, thanks Mateusz
- new IS_IMAGE checks for format and size, thanks Mateusz
- new IS_IPV4, thanks Mateusz

## 1.64.4
- Som bug fixes
- Informix Support
- response.render(stream)
- SQLFORM.factory
- SQLFORM.widgets.radio and SQLFORM.widgets.checkboxes

## 1.64.3
- Some bug fixes

## 1.64.2
- New IS_COMPLEX validator, thank Mr. Freeze
- Experimental Informix support
- Autologin on registration

## 1.64
- Models 2-3 times faster (thanks Alexey)
- Better LDAP support
- Works with Jython (including sqlite and postgresql with zxJDBC):

-   download jython-2.5rc3.jar
-   download qlite-jdbc-3.6.14.2.jar
-   java -jar jython-xxx.jar
-   export CLASSPATH=$CLASSPATH:/Users/mdipierro/jython2.5rc3/sqlite-jdbc-3.6.14.2.jar
-   cd web2py
-   ../jython2.5rc3/jython web2py.py

## 1.63.5
- You can do jQuery.noConflict() without breaking web2py_ajax
- Wigets can have attributes (thanks Hans)
- Lots of internal cleanup and better code reusage (thanks Hans)

## 1.63-1.63.4
- no more import gluon.
- support for generic.xxx
- simplejson can handle datetime date and time

## 1.62
- SQLFORMS and crud now show readble fields
- Better WingIDE support
- Languages are automatically translated
- T.force and lazyT works better, optional T.lazy=False
- gluon.storage.Messages are now translated without T
- if routes.py then request.env.web2py_original_uri
- db.table.field.isattachment = True
- internationalizaiton of admin by Yair
- admin.py by Alvaro
- new MENU helper
- new w2p file format
- new welcome app with auth, service and crud turned on

## 1.61
- fixed some typos
- auth.add_permissions(0,....) 0 indicates group of current user
- crud.update has deletable=True or False
- fixed issue with GAE detection -> gluon.settings.web2py_runtime -> request

## 1.59-1.60
- fixed lots of small bugs
- routes_in can filter by http_host

## 1.58
- Fixed some CRON bugs
- Fixed a bug with new ajax edit
- Experimental DB2 support in DAL
- Customizable font size in admin edit page
- New welcome/models/db.py shows how to memcache sessions on GAE with MEMDB
- More expressive titles in admin
- DB2 support. Thanks Denes!

## 1.57
- New ajax edit with keepalive (no longer logged out when editing code)
- Fixed conflict resolution page.
- Removed /user/bin/python from models/controllers

## 1.56.1-1.56.4
- fixing lots of small bugs with tool and languages
- jquery.1.3.2

##

- One more feature in trunk....

-     db.define_table('image',SQLField('file','upload'))

-     db.image.file.authorize=lambda row: True or False

- then controller
-     def download(): return response.download(request,db)
- id' is now a hidden field sqlform
- gql references converted to long
- admin login has autofocus
- new notation proposed by Robin, db.table[id]
- new UploadWidget shows images
- new generic.html shows request, response, session
- new LEGEND helper (thanks Marcus)
- fixed doctests in sql (thanks Robin)
- new notation for DB

- record=db.table[id]
- db.table[id]=dict(...)
- del db.table[id]

- request.env.web2py_version
- new class gluon.storage.Settings has lock_keys, lock_values
- jquery 1.3.1
- PEP8 compliance
- new examples application
- runs on jython (no database drivers yet, thanks Phyo)
- fixed bugs in tests
- passes all unittest but test_rewite (not sure it should pass that one)

- Lots of patches from Fran Boone (about tools) and Dougla Soares de Andarde (Python 2.6 compliance, user use of hashlib instead of md5, new markdown2.py)
- db.define_table('mytable',db.Field('somefield'),timestamp)
Example:
``
timestamp=SQLTable(None,'timestamp',
             SQLField('created_on','datetime',
                          writable=False,
                          default=request.now),
             SQLField('modified_on','datetime',
                          writable=False,
                          default=request.now,update=request.now))
``
and use it in all your tables
- form=SQLFORM(db.circle,request.args[-1])
- and you get a create form if the URL ends in /0, you get an update
- form if the URL ends in /[valid_record_id]
make a display form in two possible ways:
- form=SQLFORM(db.circle,record,readonly=True)
- form=SQLFORM(db.circle,record_id,readonly=True)
make an update form in two possible ways:
- form=SQLFORM(db.circle,record)
- form=SQLFORM(db.circle,record_id)
make a create form in two possible ways:
- form=SQLFORM(db.circle)
- form=SQLFORM(db.circle,0)
make a form that automatically computes area
- pi=3.1415
- form=SQLFOM(db.circle)
- if form.accepts(request.vars,
- onvalidation=lambda form: form.vars.area=pi*form.vars.radius**2): ...
make the radius appear in bold in display and table
- db.circle.radius.represent=lambda value: B(value)
automatically timestamp when record is modified
- db.circle.modified_on.update=request.now
automatically timestamp when record cretaed
- db.circle.modified_on.default=request.now
do not show now in display forms
- db.circle.modified_on.readable=False
do not show area in create/edit forms
- db.circle.area.writable=False
add a comment in the forms
- db.circle.area.comment="(this is a comment)"

## 1.56
- Now you can do:
``
db.define_table('cirlce',
    db.Field('radius','double'),
    db.Field('area','double'),
    db.Field('modified_on','datetime'))
``

## 1.55
- rowcount
- fixed bug when IS_IN_DB involved multiple fields on GAE
- T.set_current_languages
- better unittests
- response.custom_commit and response.custom_rollback
- you can next cache calls (like cache a controller that caches a select). Thanks Iceberg
- db(....id==None).select() no longer returns an error but an empty SQLRows on GAE
- db(...).delete(delete_uploads=True) and SQLFORM.accepts(....delete_uploads=True) will delete all referenced uploaded files
- DIV.element and DIV.update
- sqlrows.json()
- SQLFORM.widgets
- URL(r=request,args=0)
- IS_IN_DB(...,multiple=True) for Many2Many (sort of)
- In URL(...,f) f is url encoded
- In routes_in=[['a/b/c/','a/b/c/?var=value']]
- simplejson 2.0.7


## 1.54
- fixed minor bugs

## 1.53
- On GAE upload data goes automatically in datastore (blob created automatically)
- New appadmin runs on GAE (most of it, not all)
- Martin Hufsky patch allow slicing of fields in DAL expressions

## 1.52
- Fixed a minor bug with _extra[key] and key not str.
- check for upgrade via ajax

## 1.51
- Fixed more bugs introduced in 1.49 (sql _extra and html select)
- support for sqlite:memory:

## 1.50
- Fixed some bugs introduced in 1.49

## 1.49
- fixed a bug with taskbar widget, thanks Mark
- fixed a bug with form.latest
- made many DIV methods private (_)


## 1.43-1.48
- html.py rewrite (better support for custom forms) (Bill Ferrett)
- new stickers in examples (thanks Mateusz)
- on windows can run in taskbar (Mark Larsen)
- in admin|edit page link to edit|controller (Nathan Freeze)
- better error codes and routes_onerror (Timothy Farrell)
- DAL support for groupy and having
- DAL support for expressions instead of values
- DAL has experimental Informix support
- fixed bug with non-printable chars in DAL
- 'text' fields limited to 2**16 (to avoid mysql problems)
- widget has -quiet and -debug (Attila Csipa)
- web2py_session uses BLOB instead of TEXT
- improved IS_URL
- Runs with python 2.6 (Tim)
- On GAE uses GAE for static files (Robin)


## 1.42
- fixed security issue by removing slash escape in mysql
- removed random everywhere
- use uuid for session and tickets
- use http_x_forward_for to figure out the client causing a ticket
- use longtext and longblob for mysql
- main now really catches all exceptions
- no more warnings on GAE

## web2py 1.31-1.41
- some bug fixes, mostly better appengine support
- mssql support
- firebird support
- widgets support
- connection pools

## web2py 1.30
- added flv to contenttype
- added support for appengine

## web2py 1.29
- Now selet mutliple works with get, so does is IS_LENGTH
- Added IS_LIST_OF
- fixed problem with admin from windows and localhost

## web2py 1.28
- fixed bug with belongs, faster sql.py
- included jquery.js
- minor aestetical fixes
- sortable.js is gone

## web2py 1.27
- IS_NULL_OR now works will all fields
- admin creates paths to static files
- wsgiserver options are passed to HttpServer
- faking limitby for oracle to make appadmin work
- all objects inherit from object
- fixed bug in app names with .
- fixed bug in created RestrictedError object on windows
- shell is now in gluon and accessible via web2py.py

## web2py 1.26
- added shell.py (thanks Limodou!)
- added memcache support

## web2py 1.22-1.25
- fixed minor bugs, added IS_NULL_OR

## web2py 1.21
- replaced paste.httpserver with cherrypy.wsgi server
- temporary sessions are no longer saved
- widget has [stop] button and graph
- logging is done by main by appfactory
- fixed a bug in sql belongs

## web2py 1.20
- new IFRAME, LABEL, FIELDSET validators
- P(..cr2br=True) option
- FORM and SQLFORM have hidden=dict(...) option for REST
- testing framework.
- improved examples pages

## web2py 1.19
- minor typos

## web2py v1.18
- removed vulnerability in accept_languages and session_id
- Minor bug fixes. Typos and cleanup cache. Textarea now clears.
- Support for PyAMF.
- T returns a class, not a string
- new template parser (faster?)
- got rid of sintaxhighlighter in favor of server side CODE
- fix problem with cacheondisk locking
- fix 'None' instead of NULL in IS_NOT_IN_DB (I think)
- gluon.contrib.markdown
- notnull and unique in SQLField now supported (tested on sqlite mysql and postgresql)
- Storage now has __getstate__ and __setstate__ needed for pickling.
- session files are now locked to make it work better with asynchronous requests
- cxoracle should work, apart for limitby
- .../examples is now mapped to .../examples/default/index etc.
- .../init is now mapped to .../welcome if init is not present

## web2py v1.17
- I posted v1.16 too soon. v1.17 was released after 1h to fix some bugs.

## web2py v1.16
- yes we changed the name! Turns out Gluon was trademarked by somebody else.
- Although we are not infringing the trademark since this is a non-commercial
- product we could have run into some issues. So we have been professional
- and changed the name to web2py.
- Now SQLFORMs and FORM can have a formname and multiple forms are allowed
- per page.
- A new examples/default/index page.
- web2py.py instead of runme.py
- mysql sets utf8 encoding.
- input integer field values are automatically converted int().

## Gluon v1.15
- New try:... except. in gluon/main.py for when sessions cannot be saved
- Now validator/formatter method allows IS_DATE('%d/%m/%Y')

## Gluon v1.14
- Fixed a bug fix in URLs

## Gluon v1.13
- (this is one of the biggest revisions ever)
- Improved sql.py has support MySQL, cxOracle (experimental), extract, like and better testing
- SQLDB.tables and SQLTable.fields are now SQLCalableList objects
- Fixed bug with editing integer fields storing zero
- Admin interface now says "insert new [tablename]" and display insert, select or update properly in the title.
- Added a cache mechamism. Works for data, controllers, views and SQLRows.
- main.py now uses a request.folder absolute path when not os.name in ['nt','posix']. Seems to work on windowsce devices, except no file locking has consequences.
- Now you can put modules in applications/[anyapp]/modules and import them with
- import applications.[anyapp].modules.[module] as [module]
- Fixed problem with init
- New applications/examples/controller/global.py controller for docs.

## Gluon v1.12
- in sql.py
- handles NULL values properly
- unicode support (data always stored in utf-8)
- 'date' -> datetime.date ,'time' -> datetime.time, 'datetime' -> datetime.datetime, 'boolean' -> True/False
- most types have default validators
- SQLField(...,required=True) option.
- SQLRows has __str__ that serializes in CSV and xml() that serializes in HTML
- SQLTable has import_from_csv_file(...)
- gluon.simplejson for AJAX
- in validators.py
- IS_IN_DB(db,..) -  db can be an SQLSet or an SQLDB
- better error messages
- in admin
- new import/export in csv, update and delete interface.
- in appadmin
- edit form allows to keep stored encrypted password
- in main.py
- http://host not defaults to http://host/init/default/index
- New third party modules
- gluon.simplejson(.dumps, .loads)
- gluon.pyrtf(.dumps)
- gluon.rss2(.dumps)

## Gluon v1.11
- appadmin allows to keep or delete uploaded files

## Gluon v1.10
- fixed concurrency problems with SQLDB._instances and SQLDB._folders, now use lock
- now, by default, edit SQLFORMs retain uploaded files

## Gluon v1.9
- allow "count(*)" in select
- db.execute()
- fixed problem with continue and return in template
- removed try: ... except in sql.py
- fixed '\t'

## Gluon v1.8
- no more chdir (thread unsafe)
- no more sys.stdout (thread unsafe)
- response.body is StringIO()
- admin/default/site informs about upgrade
- response.locker (optional)

## Gluon v1.5
- <form> -> <form method="post"> in errors.html
- replace('//','////') in sub in template.py

## Gluon v1.4
- fixed problem with IS_INT_IN_RANGE and IS_FLOAT_IN_RANGE. Now an error in a validator is reported as a ticket. Good validators should not raise Exceptions.
- IS_IN_DB displays "label (id)"
- it can upload files without extension
- migration is now optional (define_table has migrate=False option)

## Gluon v1.3
- added IS_IN_DB, IS_NOT_IN_DB and updated examples accordingly

## Gluon v1.1 -> v1.2
- fixed some typos in examples
- IS_IN_SET now supports labels
- cleanup in sql.py does not cleanup, just checks valid field and table names

## Gluon v1.0 -> v1.1
- bug in sqlhtml with JOINS queries

## EWF v1.7 -> Gluon v1.0
- Name change
- Improved layout.html

## EWF v1.6 -> v1.7
- in paths replace '\' with '/' to fix problem with windows paths
- using limitby in database administration
- replaced mime/miltupart with multipart/form-data to fix a windows problem

## EWF v1.5 -> v1.6  (2007)
- load and save .py in ascii, avoids problem with LF+CR on windows
- added path.join in compileapp, fixed problem with Windows compileapp
