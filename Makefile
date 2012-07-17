.PHONY: all less coffee

all: 	less coffee

less:
	lessc apps/static/less/style.less apps/static/css/style.css

coffee:
	coffee -b -l --compile --output apps/static/js/ apps/static/coffee/*.coffee

watch:
	coffee -wlbc -o apps/static/js/ apps/static/coffee/*.coffee
