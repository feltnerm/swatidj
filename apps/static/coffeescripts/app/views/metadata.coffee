define ['jquery', 'underscore', 'backbone', 'mustache',
  'app/models/currenttrack', 
  'text!templates/metadata.html'],
($, _, Backbone, Mustache, CurrentTrackModel, template) ->
	
  class MetadataView extends Backbone.View 
    el: "#metadata"

    constructor: (model)->
      @model = model
      return @

    render: =>
      output = Mustache.render template, @model.toJSON()
      $(@el).html output
      return @

  return MetadataView