$("table tr button").on('click', function(e){
   var voterid = $(this).attr('id');
   $.ajax({
     type : 'POST',
     url : "{{url_for('voterpincard')}}",
     contentType: 'application/json;charset=UTF-8',
     data : voterid
    });
});
