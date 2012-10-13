require.config({

	'paths': {
		jQuery: 'contrib/jquery/jquery-min',
		Underscore: 'contrib/underscore/underscore-min',
		Backbone: 'contrib/backbone/backbone-min'
	},

	shim: {
		'Backbone': {
			deps: ['Underscore', 'jQuery'],
			exports: 'Backbone'
		},
		'Underscore': {
			exports: '_'
		},
		'jQuery': {
			exports: '$'
		}
	}

});

require([

	'app',

	'jQuery',
	'Underscore',
	'Backbone'

], function(App){
	App.initialize();
});