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

  it "should generate a token for a URL" do
    token = Urlencode::Url.encode("http://foobar")
    token.should_not == nil
    token.length.should >= 4
    token.length.should <= 8
    token.ascii_only?.should be true
  end
end
