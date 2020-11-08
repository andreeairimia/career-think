// Select persona

$('.radio-group .radio').click(function() {
        $('.selected .btn-block').css("visibility", "hidden");
        $('.selected .fa').removeClass('fa-check');
        $('.selected .fa').addClass('fa-circle');
        $('.radio').removeClass('selected');
        $(this).addClass('selected');
        $('.selected .fa').removeClass('fa-circle');
        $('.selected .fa').addClass('fa-check');
        $('.selected .btn-block').css("visibility", "visible");
});

// Wizard

function show_next(id, nextid, bar) {
    document.getElementById("sat").style.display="none";
    document.getElementById("wlb").style.display="none";
    document.getElementById("opp").style.display="none";
    document.getElementById("ski").style.display="none";
    document.getElementById("fin").style.display="none";
    document.getElementById("imp").style.display="none";

    $("#" + nextid).fadeIn();
}

function show_prev(previd, bar) {
    document.getElementById("sat").style.display="none";
    document.getElementById("wlb").style.display="none";
    document.getElementById("opp").style.display="none";
    document.getElementById("ski").style.display="none";
    document.getElementById("fin").style.display="none";
    document.getElementById("imp").style.display="none";
    $("#" + previd).fadeIn();
}


// Score slider

var slider = new Slider("#persona_slider", {
    precision: 1,
	tooltip: 'always',
});

var slider = new Slider("#user_slider", {
    precision: 1,
	tooltip: 'always',
});
