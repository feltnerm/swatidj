require.config
  deps: ['app']
  paths:
    
    # Javascript Directories
    lib: 'lib/'
    
    # Libraries
    jquery: 'lib/jquery-min'
    underscore: 'lib/underscore-min'
    backbone: 'lib/backbone-min'

    mustache: 'lib/mustache'
    
    r2dj: 'app/r2dj'


  shim:
    backbone:
      deps: ['underscore', 'jquery']
      exports: 'Backbone'
      init: (_, $) ->
        @Backbone.noConflict()

    underscore:
      exports: '_'
      init: ->
        @_.noConflict()

    jquery:
      exports: '$'
      init: ->
        @$.noConflict()

    mustache:
      exports: 'mustache'

require ['jquery', 'r2dj'], ($, App) ->

  App.initialize()

  $ ()->
    console.log "Shit's ready, yo."
#	Backbone.history.start({
#		pushState: true,
#		root: app.root
#	});