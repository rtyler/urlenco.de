Feature: redirect a user with a token
  In order to expand the token into a full, long form URL
  As a user
  I want to be given the URL to redirect to

  Scenario: Expand a token
    Given a record where "foobar" maps to "http://urlenco.de"
    When I expand "foobar"
    Then I should see "http://urlenco.de"


  Scenario: Expand an invalid token
    Given a record where "foobar" maps to ""
    When I expand "foobar"
    Then I should see ""

# vim: shiftwidth=2 tabstop=2 expandtab
