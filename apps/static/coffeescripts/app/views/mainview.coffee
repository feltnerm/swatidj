define ['jquery', 'underscore', 'backbone',
        'app/views/currenttrack'],
($, _, Backbone, CurrentTrackView) ->

  class MainView extends Backbone.View 
  
      views:
        currentTrack: new CurrentTrackView()

      constructor: ()->
        console.log "MainView init'd"
        @$header = $ '#header'
        @$main = $ '#main'
        @$footer = $ '#footer'

        @render
        return @

      render: ()->
        console.log 'MainView Rendered'

        for view of @views
          @views[view].render()
        return @

  return MainView