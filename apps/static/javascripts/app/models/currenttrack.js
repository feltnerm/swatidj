// Generated by CoffeeScript 1.3.3
var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; },
  __hasProp = {}.hasOwnProperty,
  __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

define(['jquery', 'underscore', 'backbone'], function($, _, Backbone) {
  var CurrentTrackModel;
  CurrentTrackModel = (function(_super) {

    __extends(CurrentTrackModel, _super);

    function CurrentTrackModel() {
      this.poller = __bind(this.poller, this);
      return CurrentTrackModel.__super__.constructor.apply(this, arguments);
    }

    CurrentTrackModel.prototype.urlRoot = '/api/0.1/stats/currentsong/';

    CurrentTrackModel.prototype.url = '/api/0.1/stats/currentsong/';

    CurrentTrackModel.prototype.defaults = {
      album: 'Unknown',
      artist: 'Unknown',
      title: 'Unknown',
      track: 'Unknown',
      pos: 'Unknown',
      time: 'Unknown',
      genre: 'Unknown',
      composer: 'Unknown',
      date: 'Unknown'
    };

    CurrentTrackModel.prototype.initialize = function() {
      this.fetch();
      return this.poller();
    };

    CurrentTrackModel.prototype.poller = function() {
      this.fetch();
      return setTimeout(this.poller, 1000);
    };

    return CurrentTrackModel;

  })(Backbone.Model);
  return CurrentTrackModel;
});