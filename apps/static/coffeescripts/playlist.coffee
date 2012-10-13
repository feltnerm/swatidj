
define (require, exports, module) ->
    Backbone = require 'backbone'

    
    class PlaylistTrack extends Backbone.Model
        defaults:
            played: false
            selected: false


    class Playlist extends Backbone.Collection
        model: PlaylistTrack
        url: '/api/0.1/playlist/'

        getPlayed = (track) ->
            return track.get("played");

        played: ->
            return @filter(getPlayed);

        remaining: ->
            return @without.apply(this, @played())

        comparator: (track) ->
            return parseInt(track.get('pos'))

        
        class PlaylistTrackView extends Backbone.View
            tagName: 'tr'

            initialize: ->
                _.bindAll @

            render: ->
                $(@el).html "<tr>#{@model.get pos}</tr>
                <tr>#{@model.get 'title'}</tr>
                <tr>#{@model.get 'artist'}</tr>"
                    
                @

        class PlaylistView extends Backbone.View
            tagName: "tbody"
            class: "playlistTable"
            el: "playlist"

            initialize: ->
                _.bindAll @

                @collection = new Playlist
                @collection.bind 'add', @appendItem

                @counter = 0
                @render()

            render:  ->
                $(@el).html(this)   

                @

            appendTrack: (track) ->
                playlist_track_view = new PlaylistTrackView model: track
                $(@el+'tbody').append playlist_track_view.render().el