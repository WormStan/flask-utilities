// Log sidebar video event
function videoEvent() {
    var video = document.getElementById('log_video');

    log_tr = $('.log_tr');

    log_tr.click(function () {
        video.currentTime = $(this).attr("id");
    });

    var rate_slider = $("#rate_slider").bootstrapSlider({min: 1,max: 5,step: 1,value: 1,tooltip: 'show'});

    video.addEventListener('timeupdate', function () {
        log_tr.each(function () {
            if (parseInt($(this).attr("id")) == parseInt(video.currentTime)) {
                $('#timepoint').remove();
                $(this).find("td:first").append("<i id='timepoint' class='fa fa-arrow-circle-right fa-lg' style='color:green;''></i>")
            }
        });
        var rate = rate_slider.bootstrapSlider('getValue');
        video.playbackRate = rate;

    });
}
videoEvent();