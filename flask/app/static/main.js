$(function() {

     var options = {
      valueNames: [ 'name', 'cost' ],
      page: 5,
      pagination: {
        innerWindow: 1,
        left: 0,
        right: 0,
        paginationClass: "pagination",
      },
      // Since there are no elements in the list, this will be used as template.
      item: '<tr><th><h3 class="name"></h3></th><th><p class="cost"></p></th></tr>'
    };

    var values = [
      {
        name: 'Elixir of Conflicts',
        cost: 820
      },
      {
        name: 'Philter of Dream Inducement',
        cost: 120
      },
      {
        name: 'Elixir of Enhanced Sleep',
        cost: 510
      },
      {
        name: 'Elixir of Enhanced Sleep',
        cost: 20
      },
      {
        name: 'Flask of the Oracle',
        cost: 1337
      },
      {
        name: 'Phial of Pain',
        cost: 30
      },
      {
        name: 'Brew of Hysteria',
        cost: 50
      },
      {
        name: 'Flask of Endless Time',
        cost: 10
      }
    ];

    var potionList = new List('potions', options, values);

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

    potionList.on('updated', function (list) {
        $('tr').addClass('animated fadeInRight');
    });

});

