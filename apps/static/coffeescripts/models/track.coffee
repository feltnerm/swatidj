define [
	'Underscore', 
	'Backbone'
	], 
(_, Backbone) ->
	trackModel = Backbone.Model.extend
		idAttribute: "title"

	return trackModel