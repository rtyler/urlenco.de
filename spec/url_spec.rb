#!/usr/bin/env ruby

$LOAD_PATH << File.expand_path('/../lib')
require 'urlencode'

describe Urlencode::Url do
  it "should store the token and url" do
    url = Urlencode::Url.new(:token => "foo", :url => "bar")

    url.token.should == "foo"
    url.url.should == "bar"
  end

  it "should be able to look up by token" do
    token = "foo"
    url = "bar"
    redis = mock('redis', :get => url)

    result = Urlencode::Url.lookup(redis, token)
    result.should == url
  end
end
