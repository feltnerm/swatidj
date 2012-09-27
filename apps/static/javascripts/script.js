// Generated by CoffeeScript 1.3.3
(function() {
  var $, initController;

  $ = jQuery;

  initController = function() {
    var control, _i, _len, _ref, _results;
    _ref = ['prev', 'next', 'play', 'pause'];
    _results = [];
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      control = _ref[_i];
      _results.push($('#' + control).bind('click', function(event) {
        return $.ajax({
          type: 'POST',
          url: '/api/0.1/c/?cmd=' + control,
          success: function(data) {
            return console.log(data);
          }
        });
      }));
    }
    return _results;
  };

  $(function() {
    var Playlist, PlaylistTrack;
    initController();
    PlaylistTrack = Backbone.Model.extend({
      defaults: {
        selected: false
      },
      initialize: function() {
        if (!this.get("selected")) {
          return this.set({
            "selected": this.defaults.content
          });
        }
      }
    });
    return Playlist = Backbone.Collection.extend({
      model: PlaylistTrack,
      url: '/api/0.1/playlist/',
      comparator: function(track) {
        return parseInt(track.get('pos'));
      }
    });
  });

}).call(this);
