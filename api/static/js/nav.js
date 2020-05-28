$(document).ready(function () {
    $(".hoverli").hover(function () {
     $(this).find('ul').slideToggle('medium');
    });
});
