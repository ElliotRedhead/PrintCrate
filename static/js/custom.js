$(function () {
    containerHeightHandling();
    if (window.location.pathname == "/")
    homepageProductSelection(bootstrapDetectBreakpoint());
    navigationBarItemBorders(bootstrapDetectBreakpoint());
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

$(".quantity-input").change(function(){
    newItemQuantity = this.value;
    itemId = this.dataset.itemId;
    const fetchInputData = {
        itemId: itemId,
        newItemQuantity: newItemQuantity 
    };
    fetch(".", fetchParameterSetup(fetchInputData))
        .then(response => {
            response.json()
            .then(responseJson => {
                console.log(responseJson)
            })
        })
})

function fetchParameterSetup(fetchInputData){
	const fetchParameters = {
		method: "POST",
		cors: "*same-origin",
		headers: new Headers({
            "Content-Type": "application/json",
            "Quantity-Validation-Fetch": true,
            "X-CSRFToken": csrftoken,
            "X-Requested-With": "XMLHttpRequest"
        }),
		body: JSON.stringify(fetchInputData)
	};
	return fetchParameters;
}

function navigationBarItemBorders(breakpoint){
    if(breakpoint.index > 2) {
        $(".nav-item").addClass("border")
    }
}

function homepageProductSelection(breakpoint){
    if (breakpoint.index < 3) {
        $(".product-container").eq(2).hide();
    }
}

$("#clipboard-url").click(function(){
    new ClipboardJS("#clipboard-url");
    swal.fire({
        icon: "success",
        text:"Site URL copied to clipboard.",
        timer: 3000,
    });
})