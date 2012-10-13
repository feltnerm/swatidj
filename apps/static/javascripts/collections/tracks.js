// Generated by CoffeeScript 1.3.3
(function() {

  define(['Underscore', 'Backbone', './models/track'], function(_, Backbone, trackModel) {
    var trackCollection;
    trackCollection = Backbone.Collection.extend({
      model: trackModel,
      url: function() {
        return "/api/0.1/songs/";
      }
    });
    return trackCollection;
  });

}).call(this);
