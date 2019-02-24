$(function() {

    /* ######################## POPULATING THE LIST  ###################### */

    function get_list_data(typeOfRequest) {
        $.ajax({
			url: '/_get_list_data',
			data: JSON.stringify({ "a" : typeOfRequest } ),
			contentType: "application/json; charset=utf-8",
            dataType: "json",
			type: 'POST',
			success: function(text){
				response = text;
				init_list(text);
			},
			error: function(error){
			}
		})
    }

     var options = {
      valueNames: [ 'name', 'cost' ],
      page: 5,
      pagination: {
        innerWindow: 1,
        left: 0,
        right: 0,
        paginationClass: "pagination",
      },
      item: '<tr><th><h3 class="name"></h3></th><th><p class="cost"></p></th></tr>'
    };

    /* ######################## Live exec  ###################### */

    get_list_data(1);

    var potionList;
    var listLoaded = 0;

    function init_list (values){
        potionList = new List('potions', options, values['result']);

        var listLoaded = 1;
    }


    /* ######################## PAGINATION FUNCTIONS  ###################### */

    $('.jPaginateNext').on('click', function(){

        var list = $('.pagination').find('li');

        $.each(list, function(position, element){
            if($(element).is('.active')){
                $(list[position+1]).trigger('click');
            }
        })
    });


    $('.jPaginateBack').on('click', function(){

        var list = $('.pagination').find('li');

        $.each(list, function(position, element){
            if($(element).is('.active')){
                $(list[position-1]).trigger('click');
            }
        })
    });

    /* ######################## ANIMATIONS  ###################### */

    if (listLoaded == 1){

        potionList.on('updated', function (list) {
            $('tr').addClass('animated fadeInRight');
        });
    }
});

