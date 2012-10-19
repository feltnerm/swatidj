require.config({

	deps: ["main"],

	'paths': {
		// Javascript Directories
		contrib : './contrib/',

		// Libraries
		jquery: 'contrib/jquery-min',
		underscore: 'contrib/underscore-min',
		backbone: 'contrib/backbone-min',

		//views: './views/',
		//models: './models/',
		//collections: './collections/'
		app: 'app/',
		r2dj: 'app/r2dj'
	
	},

	shim: {
		'backbone': {
			deps: ['underscore', 'jquery'],
			exports: 'Backbone',
			init: function(_, $) {
				return this.Backbone.noConflict();
			}
		},
		'underscore': {
			exports: '_',
			init: function () {
				return this._.noConflict();
			}
		},
		'jquery': {
			exports: '$',
			init: function () {
				return this.$.noConflict();
			}
		}
	}

});

require(['r2dj'],
	function(App) {
		console.log(App);
		App.initialize();
	//	Backbone.history.start({
	//		pushState: true,
	//		root: app.root
	//	});

	//$(document).ready( function() {
	//		console.log("Shit's ready, yo.");
	//});

});
