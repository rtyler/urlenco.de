#!/usr/bin/env ruby

module Urlencode
  class Url
    attr_accessor :token, :url

    def initialize(opts={})
      @token = opts[:token]
      @url = opts[:url]
      super
    end

    def self.lookup(redis, token)
      return redis.get(token)
    end
  end
end
