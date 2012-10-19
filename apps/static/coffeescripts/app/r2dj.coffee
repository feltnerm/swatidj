define ['underscore', 'backbone', 
        'app/routers/router'], 
(_, Backbone, Router) ->

  return _.extend {
    root: '/'
    initialize: ->
      @router = new Router
        root: @root
      @trigger('initialize')

  }, Backbone.Events