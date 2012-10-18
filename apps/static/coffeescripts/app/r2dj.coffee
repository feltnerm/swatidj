define ['jquery', 'underscore', 'backbone']
($, _, Backbone) ->

  App =
    init: () ->
      @root = '/'
      @router = new Router

  _.extends App, Backbone.Events

  class Router extends Backbone.Router

    defaults:
      routes:
        '': 'index'
      view: new MainView

    initialize: () ->
      @routes =
        "": "index"
      @view = new R2DJView()
      console.log @view

    index: () ->
      @view.render
      console.log "Index Visited"
      
    browse: () ->

      console.log "Browse visited"

    defaultAction: (actions) ->

      # no matching routes, log it!
      console.log "USER ACTION: ", actions


  class View extends Backbone.View 
    
    # #events: 
    #   'keypress #new-todo': 'createOnEnter',
    #   'click #clear-completed': 'clearCompleted',
    #   'click #toggle-all': 'toggleAllComplete'
    defaults:
      id: '#main'
      views:
        currentTrack: new CurrentTrack

    initialize: ()->
      console.log 'Main App Rendered'

    render: ()->
      $(@el).append '<p>Hello, world!</p>'
      for view of @get 'views'
        view.render()


  class CurrentTrackView extends Backbone.View 
      id: "#current-track-view"
      tag: "div"

      # #events: 
      #   'keypress #new-todo': 'createOnEnter',
      #   'click #clear-completed': 'clearCompleted',
      #   'click #toggle-all': 'toggleAllComplete'
      
      render: ()->
        console.log "CurrentTrackView rendered"