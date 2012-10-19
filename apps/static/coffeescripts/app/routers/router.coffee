define ['jquery', 'underscore', 'backbone',
        'app/views/currenttrack'],
($, _, Backbone, CurrentTrackView) ->
  class Router extends Backbone.Router

      routes:
        '': 'index'
        '*actions': 'defaultAction'
      
      views:
        'currentTrackView': new CurrentTrackView
        #'navigationView': new NavigationView
        #'browserView': new BrowserView

      constructor: (@options) ->
        # Cache main page sections as jquery objects
        @$header = $ '#header'
        @$main = $ '#main'
        @$footer = $ '#footer'

        # Render the initial views
        for view of @views
          @views[view].render()

      defaultAction: (actions) ->
        # no matching routes, log it!
        console.log "USER ACTION: ", actions

  return Router