$(function () {
    const viewportRemaining = window.innerHeight - $("nav").outerHeight();
    console.log($(".jumbotron").outerHeight(true))
    $(".jumbotron").css("margin-bottom", 0);
    $(".jumbotron").outerHeight(viewportRemaining);
}
);