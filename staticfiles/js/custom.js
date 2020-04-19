$(function () {
    const viewportRemaining = window.innerHeight - $("nav").outerHeight();
    $(".jumbotron").css("margin-bottom", 0);
    $(".jumbotron").outerHeight(viewportRemaining);
}
);