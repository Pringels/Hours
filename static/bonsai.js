var global_percentage = 0;
var global_history = [];
var global_last_updated = 0;
var global_last_updated_date = 0;

$(document).ready(function(){
    runAllGauges();
    initWater();
    initHistogram();
});

setInterval(function(){
    $.ajax({
      type: "GET",
      url: "/bonsai/fetch/",
    }).done(function(data) {
        global_percentage = ((4000 - data) / 4000 ) * 100;
        $('.gauge-cont').data('percentage', global_percentage);
        runAllGauges();
        $.ajax({
          type: "GET",
          url: "/bonsai/fetch_more/",
        }).done(function(data) {
            parsed_data = JSON.parse(data);
            global_history = parsed_data.data;
            global_last_updated = parsed_data.delta;
            global_last_updated_date = parsed_data.date;
            update_histogram();
        });

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

$("#liquid").on("mouseover", function(){
    $('.stats').addClass('active');
});

$("#liquid").on("mouseout", function(){
    $('.stats').removeClass('active');
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


    var box3 = s.rect(center_x - 155, 250, 310, 310);

    var image = s.image("/static/images/soil.jpg", center_x - 150, 250, 300, 300);
    var image2 = s.image("/static/images/tree.png", center_x - 205, -350, 475, 600);

    var path = "M"+center_x+",20";
    path += "L"+(center_x+100)+",20";
    path += "L"+(center_x+100)+",200";
    path += "C300,400,150,100,10,200";
    path += "L10,20";

    var box = s.path(path);

    // 955 x 1207 = 1.264


    var m_circle1 = s.circle(center_x, 400, 150);
    m_circle1.attr({
        fill: "#fff"
    });

    var m_box1 = s.rect(center_x - 150, 250, 300, 150);
    m_box1.attr({
        fill: "#fff"
    });

    var m_circle2 = s.circle(center_x, 400, 150);
    m_circle2.attr({
        fill: "#fff"
    });

    var m_box2 = s.rect(center_x - 150, 250, 300, 150);
    m_box2.attr({
        fill: "#fff"
    })

    var m_circle3 = s.circle(center_x, 400, 150);
    m_circle3.attr({
        fill: "#fff"
    });

    var m_box3 = s.rect(center_x - 160, 250, 320, 150);
    m_box3.attr({
        fill: "#fff"
    })

    var mask = s.group(m_circle1, m_box1);
    var mask2 = s.group(m_circle2, m_box2);
    var mask3 = s.group(m_circle3, m_box3);


    mask3.attr({
        fill: "#FFF",
        stroke: "#FFF",
        strokeWidth: 10
    })

    box3.attr({
        mask: mask3,
        fill: "#FFF",
        strokeWidth: 10
    });

    image.attr({
        mask: mask2
    })

    box.attr({
        mask: mask,
        fill: "rgb(80, 80, 255)"
    });

    box.addClass('water');


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

function initHistogram() {
    var s = Snap("#histogram");

    var center_x = 500;

    var svg = document.getElementById("histogram");

    var path = "M"+center_x+",20";
    path += "L"+(center_x+100)+",20";
    path += "L"+(center_x+100)+",200";
    //path += "C300,400,150,100,10,200";
    //path += "L10,400";

    var box = s.path(path);
    box.addClass('histogram');

    window.update_histogram = function(){
        var new_path = "M00,20";

        for (var i = global_history.length - 1; i >= 0; i--){
            var coord = global_history[i] / 100
            new_path += "L" + ((global_history.length - i)*20) +"," + (global_history[i] / 100);
        }
        //new_path += "L" + (global_history.length * 20) + ",50";
        //new_path += "L0,50";

        box.attr(
            {path: new_path}
        );

        $('.last_updated h1 b').html(global_last_updated);
        $('.last_updated h2').html(global_last_updated_date);
    }

};
