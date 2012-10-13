define [
  'jQuery',
  'Underscore',
  'Backbone',
  # views
  ],
($, _, Backbone) ->
  AppRouter = Backbone.Router.extend
    routes:
      '*actions': 'defaultAction'

    defaultAction: (actions) ->
      # no matching routes, log it!
      console.log "No route: ", actions

  initialize = ->
    app_router = new AppRouter
    Backbone.history.start()

  return { initialize: initialize }