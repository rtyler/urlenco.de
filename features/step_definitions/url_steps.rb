#!/usr/bin/env ruby

Given /^a record where "([^"]*)" maps to "([^"]*)"$/ do |token, url|
  @url = Urlencode::Url.new(:token => token, :url => url)
  @redis = mock('redis', :get => url)
end

When /^I expand "([^"]*)"$/ do |token|
  @expanded = Urlencode::Url.lookup(@redis, token)
end

Then /^I should see "([^"]*)"$/ do |url|
  @expanded.should == url
end
