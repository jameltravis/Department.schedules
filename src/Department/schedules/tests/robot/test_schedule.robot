# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s Department.schedules -t test_schedule.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src Department.schedules.testing.DEPARTMENT_SCHEDULES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_schedule.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Schedule
  Given a logged-in site administrator
    and an add schedule form
   When I type 'My Schedule' into the title field
    and I submit the form
   Then a schedule with the title 'My Schedule' has been created

Scenario: As a site administrator I can view a Schedule
  Given a logged-in site administrator
    and a schedule 'My Schedule'
   When I go to the schedule view
   Then I can see the schedule title 'My Schedule'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add schedule form
  Go To  ${PLONE_URL}/++add++Schedule

a schedule 'My Schedule'
  Create content  type=Schedule  id=my-schedule  title=My Schedule


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the schedule view
  Go To  ${PLONE_URL}/my-schedule
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a schedule with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the schedule title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
