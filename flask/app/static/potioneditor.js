function CharCount() {

    var inp = document.getElementById('description').value;

    charcount = inp.length;

    var percentage = charcount / 500 * 100;

    if (charcount < 500){
        $("#word-count").html(charcount);
        $('#word-count').css('width', percentage+'%').attr('aria-valuenow', percentage);
    }   else {
        $("#word-count").html("Over the character limit!");
        $('#word-count').css('width', 100+'%').attr('aria-valuenow', 100);
    }
}

$(function() {
    CharCount();

    $("#description").on('input',function(){
        CharCount();
    });

    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })
});

