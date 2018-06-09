.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
Department.schedules
==============================================================================

A tool for proposing schedules. Note: Any changes made after 2018-06-08 will have been done blindly. Until Further notice, I don't have enough disk space for a VM with Plone. 

Let the open source flow through you.

Project status/phase: Development
Completion: 40%

Features
--------

- View courses currently offered
- Specify which courses you would like to modify, remove or add to the master schedule.
- For Executives: Approve or deny requests to change the master schedules.
- For IT Admins: Add or remove courses from course vocubularies.

Permissions / Workflow
----------------------

- Any logged in user -> View the schedules
- Department level -> Edit the schedule, send to registrar (if same as previous year), send it to the Deans / Provost
- Dean Level -> Edit schedule, send to department, send it to Provost
- Provost level -> Edit schedule, send back to department, send it to Registrar
- Registrar level -> view only(?), departments can change state

Todo list:
----------

- Add named vocabulary items to datagrid fields
- Write update / upgrade steps
- Style Datagrid fields so they look a little more pleasant
- Create validators: Class time conflicts, day of week conflicts, limit on number of new classes offered
- test faculty vocabulary, and decide if it needs to be cached or not.
- if functions need caching, create new cache keys.
- Create action (button) to write datagrid data to csv.
- Fix workflows


Recommendation:
---------------

- Add new user property for staff: ``'workloadHours'`` . If this is done, a Workload report could be implemented as a view, using data from the datagrid fields.

Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar

- Full documentation due after UAT


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install Department.schedules by adding it to your buildout::

    [sources]
    Department.schedules = git https://github.com/jameltravis/Department.schedules.git

    ...

    [buildout]

    ...

    eggs =
        Department.schedules


and then running ``bin/buildout`` from your zinstance or zeocluster directory 
Note: if ``[sources]`` isn't included in your buildout, include it. Feel free to copy and paste
the following code above the ``[buildout]`` header ::
    [sources]
    Department.schedules = git https://github.com/jameltravis/Department.schedules.git




Contribute
----------

- Source Code: git https://github.com/jameltravis/Department.schedules.git
- Documentation: git https://github.com/jameltravis/Department.schedules.git


Support
-------

email me at: j.travis07@hotmail.com


License
-------

The project is licensed under the GPLv2.
