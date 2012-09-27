$ -> 
	
	# Track Model
    PlaylistTrack = Backbone.Model.extend(
        defaults:
            played: false
            selected: false

        initialize: ->
            if !@get("selected")
                @set({ "selected":@defaults.content})
            if !@get("played")
                @set({  "played":@defaults.played})

    )       

    Playlist = Backbone.Collection.extend(
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
            )

    PlaylistView = Backbone.View.extend(
        tagName: "tr"
        className: "playlistRow"

        events: 
            "click":    "select"
            "dblclick": "play"

        render: () ->
            $(this.el).html(this)   
        )