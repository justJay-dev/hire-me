var inactivityTime = function () {
    var time;
    window.onload = resetTimer;
    // DOM Events
    document.onmousemove = resetTimer;
    document.onkeypress = resetTimer;
    var desktop = document.getElementById('desktop')
    var canvas = document.getElementById('c')
    function showDesktop(){
        if (desktop.style.display ==='none'){
            desktop.style.display = 'block';
            canvas.style.display = 'none';
        }
    }
    function showScreenSaver() {
        if (canvas.style.display === 'none') {
            desktop.style.display = 'none';
            canvas.style.display = 'block';
        } else {
            canvas.style.display = 'none';
            desktop.style.display = 'block';
        }
    }

    function resetTimer() {
        clearTimeout(time);
        showDesktop()
        time = setTimeout(showScreenSaver, 30000)
        // 1000 milliseconds = 1 second
    }
};
window.onload = function() {
  inactivityTime(); 
}
function timerIncrement() {
    idleTime = idleTime + 1;
    if (idleTime > 1) { 
        alert('timer')
    }
}
var c = document.getElementById('c'),
    ctx = c.getContext('2d'),
    shapes = [],
    speed = 7

c.width = window.innerWidth;
c.height = window.innerHeight;

function Point(){
    this.x = parseInt(Math.random()*c.width);
    this.y = parseInt(Math.random()*c.height);
    this.xVel = parseInt(Math.random()*2) == 1 ? 1 : -1;
    this.yVel = parseInt(Math.random()*2) == 1 ? 1 : -1;
}

function Shape(){
    this.color = '#'+Math.floor(Math.random()*16777215).toString(16);
    this.points = [];

    for(var i=0;i<4;i++){
        this.points.push(new Point());
    }

    this.draw = function(){
        ctx.strokeStyle = this.color;
        ctx.beginPath();
        ctx.moveTo(this.points[0].x, this.points[0].y);

        for(var i=1;i<this.points.length;i++){
            var p = this.points[i];

            ctx.lineTo(p.x, p.y);
        }

        ctx.lineTo(this.points[0].x, this.points[0].y);
        ctx.closePath();
        ctx.stroke();
    }

    this.update = function(){
        for(var i=0;i<this.points.length;i++){
            var p = this.points[i];

            p.x += p.xVel * speed;
            p.y += p.yVel * speed;

            if(p.x > c.width) p.xVel = Math.abs(p.xVel) * -1;
            if(p.x < 0) p.xVel = Math.abs(p.xVel);

            if(p.y > c.height) p.yVel = Math.abs(p.yVel) * -1;
            if(p.y < 0) p.yVel = Math.abs(p.yVel);
        }
    }
}

var s = new Shape();
var s2 = new Shape();

function render(){
    ctx.fillStyle = 'rgba(0,0,0,0.1)';
    ctx.fillRect(0, 0, c.width, c.height);

    s.update();
    s.draw();

    s2.update();
    s2.draw();
}

window.requestAnimFrame = (function(){
    return  window.requestAnimationFrame   ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame    ||
        function(callback){
            window.setTimeout(callback, 1000 / 60);
        };
})();

(function animloop(){
    requestAnimFrame(animloop);
    render();
})();
