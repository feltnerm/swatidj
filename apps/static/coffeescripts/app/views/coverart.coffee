define ['jquery', 'underscore', 'backbone', 'mustache',
  'app/models/currenttrack', 
  'text!templates/coverart.html'],
($, _, Backbone, Mustache, CurrentTrackModel, template) ->
	
  class CoverartView extends Backbone.View 
    el: "#coverart"

    constructor: (model)->
      @model = model
      return @

    render: =>
      $(@el).html( Mustache.render( template, @model.toJSON() ) )
      return @

  return CoverartView