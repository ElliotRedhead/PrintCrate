$(function () {
    containerHeightHandling()
}
);

function containerHeightHandling(){
    const viewportHeight = window.innerHeight;
    const headerHeight = $("nav").outerHeight();
    const footerHeight = $("footer").outerHeight();
    $(".main-container").first().css("min-height", viewportHeight - headerHeight - footerHeight);
    $(".jumbotron").css("margin-bottom", 0);
    $(".jumbotron").outerHeight(viewportHeight - headerHeight);
}