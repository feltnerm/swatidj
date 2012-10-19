// Generated by CoffeeScript 1.3.3

define(['underscore', 'backbone', 'app/routers/router'], function(_, Backbone, Router) {
  return _.extend({
    root: '/',
    initialize: function() {
      this.router = new Router({
        root: this.root
      });
      return this.trigger('initialize');
    }
  }, Backbone.Events);
});