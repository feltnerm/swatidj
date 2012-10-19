// Generated by CoffeeScript 1.3.3
var __hasProp = {}.hasOwnProperty,
  __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

define(['jquery', 'underscore', 'backbone', 'app/views/currenttrack'], function($, _, Backbone, CurrentTrackView) {
  var Router;
  Router = (function(_super) {

    __extends(Router, _super);

    Router.prototype.routes = {
      '': 'index',
      '*actions': 'defaultAction'
    };

    Router.prototype.views = {
      'currentTrackView': new CurrentTrackView
    };

    function Router(options) {
      var view;
      this.options = options;
      this.$header = $('#header');
      this.$main = $('#main');
      this.$footer = $('#footer');
      for (view in this.views) {
        this.views[view].render();
      }
    }

    Router.prototype.defaultAction = function(actions) {
      return console.log("USER ACTION: ", actions);
    };

    return Router;

  })(Backbone.Router);
  return Router;
});