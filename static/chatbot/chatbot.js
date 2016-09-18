/**
 * Created by peter on 2016/09/18.
 */

var global_counter = 0;

$('button').on('click', function(){
  addMessage();
});

$(document).on('click', '.response-button', function(){

  var data = $(this).data('hook');
  addMessage(data);
});

$(document).on('keydown', function(evt){
  if (evt.keyCode == 13) {
      addMessage();
  }
})

function createMessage(val, side, responses, image) {
  responses = responses || false;
  image = image || false;
  var chatMsg = '<li class="chats-' + side + ' pre">';
  chatMsg += val;

  if (image){
      chatMsg += '<img src="'+image+'" class="response-image"/>';
  }

  if (responses){
    for (var i = 0; i < responses.length; i++){
        chatMsg += '<button class="response-button" data-hook="'+responses[i]+'">'+responses[i]+'</button>';
    }
  }

  chatMsg += '</li>';
  return chatMsg;
}

function clearPre() {
  setTimeout(function(){
    $('.pre').removeClass('pre');
  }, 0);
}

function scroll() {
  clearPre();
  $('.chats').stop().animate({
  scrollTop: $('.chats')[0].scrollHeight
}, 500, function(){

  });
}

function addMessage(data) {
  data = data || false;
  var delay = 100;
  var val = $('input').val();
  if (!data){
    $('.chats').append(createMessage(val, 'right'));
    scroll();
    delay = 1000;
    get_response(val, function(response){
      setTimeout(function(){
        $('.chats').append(
          createMessage(
            response.message,
            'left',
            response.links,
            response.image
          )
        );
        scroll();
      }, delay);

      $('input').val('');
    });
  } else {
    get_response(data, function(response){
      setTimeout(function(){
        $('.chats').append(
          createMessage(
            response.message,
            'left',
            response.links,
            response.image
          )
        );
        scroll();
      }, delay);

      $('input').val('');
    });
  }

}

scroll();

// Get response from server
function get_response(message, callback) {
  var request = $.ajax({
      method: "POST",
      url: "/chatbot/get_response/",
      data: { message: message, counter: global_counter }
    });
  request.done(function( res ) {
    res = JSON.parse(res);
    if (res.increment) {
      global_counter += 1;
    }

    if (res.reset) {
      global_counter = 1;
    }
    callback(res);
  });
  request.fail(function( msg ) {
    callback('Server error :(');
  });
}