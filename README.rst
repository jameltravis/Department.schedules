.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
Department.schedules
==============================================================================

Used for proposing course schedules at York College. 

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
--------

- Need to ``assert isinstance()`` to function args for pseudo type checking
- Need to create vocabularies that are context specific, or filter results based on department the current logged in user belongs to. Use ``startswith()`` in vocab definition.
- Style Datagrid fields so they look a little more pleasant
- Create validators: Class time conflicts, day of week conflicts, limit on number of new classes offered
- Coming soon!


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar
- Full documentation is coming soon!


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install Department.schedules by adding it to your buildout::

    [sources]
    Department.schedules = git https://git.york.cuny.edu/jtravis1/Department.schedules.git

    ...

    [buildout]

    ...

    eggs =
        Department.schedules


and then running ``bin/buildout`` from your zinstance or zeocluster directory 
Note: if ``[sources]`` isn't included in your buildout, include it. Feel free to copy and paste
the following code above the ``[buildout]`` header ::
    [sources]
    Department.schedules = git https://git.york.cuny.edu/jtravis1/Department.schedules.git




Contribute
----------

- Source Code: https://git.york.cuny.edu/jtravis1/Department.schedules
- Documentation: https://git.york.cuny.edu/jtravis1/Department.schedules


Support
-------

If you are having issues, please call/email someone who will call/email someone else, who will then call/email me.
Just kidding, email me at: jtravis1@york.cuny.edu


License
-------

The project is licensed under the GPLv2.
