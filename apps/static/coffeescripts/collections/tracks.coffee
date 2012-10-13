define [
	'Underscore',
	'Backbone',
	'./models/track'
	], 
(_, Backbone, trackModel) ->
	trackCollection = Backbone.Collection.extend
		model: trackModel
		url: () ->
			"/api/0.1/songs/"

	return trackCollection