define ['jquery', 'underscore', 'backbone', 'mustache',
  'app/models/currenttrack', 
  'app/views/coverart',
  'app/views/metadata'],
($, _, Backbone, Mustache, CurrentTrackModel, CoverartView, MetadataView) ->
	
  class CurrentTrackView extends Backbone.View 
    el: "#current-track"

    # Instantiate models and views
    initialize: ->
      @model = new CurrentTrackModel()
      @model.on 'change', =>
        console.log "CHANGE"
        @render()
        
      @views = {
        coverartView: new CoverartView(@model)
        metadataView: new MetadataView(@model)
      }
      return @

    render: =>
      for view of @views
        @views[view].render()
      return @

    remove: =>
      for view of @views
        @views[view].remove()

  return CurrentTrackView