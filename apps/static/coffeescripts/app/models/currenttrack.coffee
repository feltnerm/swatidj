define ['jquery', 'underscore', 'backbone'],
($, _, Backbone) ->
	
  class CurrentTrackModel extends Backbone.Model 
    urlRoot: '/api/0.1/stats/currentsong/'
    url: '/api/0.1/stats/currentsong/'

    defaults:
      album: 'Unknown'
      artist: 'Unknown'
      title: 'Unknown'
      track: 'Unknown'
      pos: 'Unknown'
      time: 'Unknown'
      genre: 'Unknown'
      composer: 'Unknown'
      date: 'Unknown'

    initialize: ->
      @fetch()
      @poller()

    poller: =>
      @fetch()
      setTimeout(@poller, 1000)

  return CurrentTrackModel