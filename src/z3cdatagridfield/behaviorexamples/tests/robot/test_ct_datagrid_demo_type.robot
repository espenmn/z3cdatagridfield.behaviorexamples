# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s z3cdatagridfield.behaviorexamples -t test_datagrid_demo_type.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src z3cdatagridfield.behaviorexamples.testing.Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/z3cdatagridfield/behaviorexamples/tests/robot/test_datagrid_demo_type.robot
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

Scenario: As a site administrator I can add a DatagridDemoType
  Given a logged-in site administrator
    and an add DatagridDemoType form
   When I type 'My DatagridDemoType' into the title field
    and I submit the form
   Then a DatagridDemoType with the title 'My DatagridDemoType' has been created

Scenario: As a site administrator I can view a DatagridDemoType
  Given a logged-in site administrator
    and a DatagridDemoType 'My DatagridDemoType'
   When I go to the DatagridDemoType view
   Then I can see the DatagridDemoType title 'My DatagridDemoType'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add DatagridDemoType form
  Go To  ${PLONE_URL}/++add++DatagridDemoType

a DatagridDemoType 'My DatagridDemoType'
  Create content  type=DatagridDemoType  id=my-datagrid_demo_type  title=My DatagridDemoType

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the DatagridDemoType view
  Go To  ${PLONE_URL}/my-datagrid_demo_type
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a DatagridDemoType with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the DatagridDemoType title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
