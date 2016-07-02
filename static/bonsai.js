var global_percentage = 0;

$(document).ready(function(){
    runAllGauges();
    initWater();
});

setInterval(function(){
    $.ajax({
      type: "GET",
      url: "/bonsai/fetch/",
    }).done(function(data) {
        data = Math.round(((4096 - data) / 4096) * 100);
        $('.gauge-cont').data('percentage', data);
        runAllGauges();
    });
}, 500);

$('.reset').on('click', function(e){
  e.preventDefault();
  $(this).toggleClass('active');
  if ( $(this).hasClass('active') ){
    $(this).text('Run');
    resetAllGauges();
  } else {
    $(this).text('Reset');
    runAllGauges();
  }
});


function runAllGauges()
{
  var gauges = $('.gauge-cont');
  $.each(gauges, function(i, v){
    var self = this;
        setTimeout(function(){
        setGauge(self);
    },i * 700);
  });
}

function resetAllGauges()
{
  var gauges = $('.gauge-cont').get().reverse();
  $.each(gauges, function(i, v){
    var self = this;
        setTimeout(function(){
        resetGauge(self);
    },i * 700);
  });
}

function resetGauge(gauge)
{
  var spinner = $(gauge).find('.spinner');
  var pointer = $(gauge).find('.pointer');
  $(spinner).attr({
    style: 'transform: rotate(0deg)'
  });
  $(pointer).attr({
    style: 'transform: rotate(-90deg)'
  });
}

function setGauge(gauge)
{
  var percentage = $(gauge).data('percentage') / 100;
  global_percentage = percentage * 100;
  var degrees = 180 * percentage;
  var pointerDegrees = degrees - 90;
  var spinner = $(gauge).find('.spinner');
  var pointer = $(gauge).find('.pointer');
  $(spinner).attr({
    style: 'transform: rotate(' + degrees + 'deg)'
  });
  $(pointer).attr({
    style: 'transform: rotate(' + pointerDegrees + 'deg)'
  });
}

function initWater() {

    var s = Snap("#liquid");

    var svg = document.getElementById("liquid");

    var center_x = 300;
    var testActive = true;

    var delay = 0.05;


    var path = "M"+center_x+",20";
    path += "L"+(center_x+100)+",20";
    path += "L"+(center_x+100)+",200";
    path += "C300,400,150,100,10,200";
    path += "L10,20";

    var box = s.path(path);

    var m_circle1 = s.circle(center_x, 400, 150);
    m_circle1.attr({
        fill: "#fff"
    });
    var mask = s.group(m_circle1);

    box.attr({
        mask: mask,
        fill: "rgb(80, 80, 255)"
    });

    var ticker = 0;

    var speed = 0.05;
    var amplitude = 30;

    var activeColor = "none";

    var colorDuration = 500;

    var mouseY = 400;

    var offset = 600;

    function render() {

        // temp testing input
        speed = 0.05;
        amplitude = 20;
        delay = 0.1;
        colorDuration = 2;

        // end temp testing input

        ticker += speed;

        if (ticker >= 2 * Math.PI) {
            ticker = 0;
        }

        var y1 = Math.round(Math.sin(ticker + Math.PI*0.5)*amplitude*2 + offset);
        var y2 = Math.round(Math.sin(ticker + Math.PI)*amplitude + offset);
        var y3 = Math.round(Math.sin(ticker + Math.PI*1.5)*amplitude*2 + offset);
        var y4 = Math.round(Math.sin(ticker + Math.PI*2)*amplitude + offset);


        new_path = "M"+(center_x-200)+","+(offset + 700);
        new_path += "L"+(center_x+200)+","+(offset + 700);
        new_path += "L"+(center_x+200)+","+ y2;
        new_path += "C"+(center_x)+","+y1+","+(center_x)+","+y3+","+(center_x-200)+","+y2;
        new_path += "L"+(center_x-200)+","+(offset + 700);

        box.attr(
            {path: new_path}
        );

        var target = ((100 - global_percentage) * 2.8) + 260

        offset += (target - offset) * delay;
        offset = Math.round(offset);
    }

    function changeColor(evt) {

        if (offset > 350){
            if (activeColor !== "red"){
                activeColor = "red";

                box.stop().animate(
                    {fill: "rgb(255, 80, 80)"},
                    colorDuration,
                    mina.easein
                );
            }
        }else if (offset > 200){
            if (activeColor !== "yellow"){
                activeColor = "yellow";
                box.stop().animate(
                    {fill: "rgb(255, 200, 80)"},
                    colorDuration,
                    mina.easein
                );
            }
        }else if (activeColor !== "green") {
            if (activeColor !== "green"){

                activeColor = "green";
                box.stop().animate(
                    {fill: "rgb(80, 220, 80)"},
                    colorDuration,
                    mina.easein
                );
            }
        }
    }

    // returns an animation frame along with a setTimeout fallback
    window.requestAnimFrame = (function(){
      return  window.requestAnimationFrame       ||
              window.webkitRequestAnimationFrame ||
              window.mozRequestAnimationFrame    ||
              function( callback ){
                window.setTimeout(callback, 1000 / 60);
              };
    })();

    //document.addEventListener("mousemove", changeColor);

    function animloop(){
      requestAnimFrame(animloop);
      render();
    };

    animloop();


}
