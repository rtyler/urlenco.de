Feature: Generate a token for a URL
  In order to use a more compact URL for sharing, etc
  As a user
  I want to pass in a URL and receive a shortened Urlencode token

  Scenario: Encoding a simple URL
    Given the url "http://urlenco.de"
    When I encode it
    Then I should receive a token
# vim: shiftwidth=2 tabstop=2 expandtab
