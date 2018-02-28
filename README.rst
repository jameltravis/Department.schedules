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

Examples
--------

This add-on can be seen in action at the following sites:
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

    [buildout]

    ...

    eggs =
        Department.schedules


and then running ``bin/buildout`` from your zinstanc or zeocluster directory 
Note: if ``[sources]`` isn't included in your buildout, include it. Feel free to copy and paste
the following above ``[buildout]`` ::

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
