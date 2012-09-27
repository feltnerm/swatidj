$ = jQuery


initController = ->
    for control in ['prev','next','play','pause']
        $('#'+control).bind 'click', (event) ->
            $.ajax(
                type: 'POST'
                url: '/api/0.1/c/?cmd='+control
                success: (data) ->
                    console.log(data)
            )

$ ()->
    
    initController()