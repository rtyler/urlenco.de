#!/usr/bin/env ruby

Given /^a record where "([^"]*)" maps to "([^"]*)"$/ do |token, url|
  @url = Urlencode::Url.new(:token => token, :url => url)
  @redis = mock('redis', :get => url)
end

Given /^the url "([^"]*)"$/ do |url|
  @url = url
end



When /^I expand "([^"]*)"$/ do |token|
  @expanded = Urlencode::Url.lookup(@redis, token)
end

When /^I encode it$/ do
  @url.should_not == nil
  @encoded = Urlencode::Url.encode(@url)
end



Then /^I should see "([^"]*)"$/ do |url|
  @expanded.should == url
end

Then /^I should receive a token$/ do
  @encoded.should_not == nil
  # These checks are duplicated in the rspecs as well
  @encoded.length.should >= 4
  @encoded.length.should <= 8
end
