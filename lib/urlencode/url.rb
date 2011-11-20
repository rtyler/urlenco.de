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

    def self.encode(url)
      token = []
      r = Random.new(Time.now.to_i)
      length = r.rand(4 .. 8)

      length.times do |i|
        token << r.rand(97 .. 122).chr
      end

      return token.join
    end
  end
end
