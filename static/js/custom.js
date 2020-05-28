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
    quantityInputElement = this
    newItemQuantity = this.value;
    itemId = this.dataset.itemId;
    const fetchInputData = {
        itemId: itemId,
        newItemQuantity: newItemQuantity 
    };
    identifyingHeader = "quantityValidationFetch";
    fetch(".", fetchParameterSetup(fetchInputData, identifyingHeader))
        .then(response => {
            response.json()
            .then(responseJson => {
                if(responseJson.updatedQuantity == true){
                    $(quantityInputElement).siblings(".btn").removeClass("invisible");
                }
                else {
                    $(quantityInputElement).siblings(".btn").addClass("invisible");
                }
            })
        })
})

$(".remove-cart-item-button").click(function(){
    itemId = this.dataset.removeItemId;
    fetchInputData = {"itemId" : itemId}
    swal.fire({"timer":"20000",
    "title":"Remove product",
    "text":"Are you sure you wish to remove this item from your cart?",
    "icon":"warning",
    "showConfirmButton":"true",
    "showCancelButton":"true",
    "confirmButtonText":"Remove"})
    .then((userConfirmation) => {
        if (userConfirmation.value) {
            identifyingHeader = "removeCartItemFetch"
            fetch(".", fetchParameterSetup(fetchInputData, identifyingHeader))
            .then(function(){
                location.reload()
            })
            
        }
    })
})

function fetchParameterSetup(fetchInputData, identifyingHeader){
	const fetchParameters = {
		method: "POST",
		cors: "*same-origin",
		headers: new Headers({
            "Identifying-Header" : identifyingHeader,
            "Content-Type": "application/json",
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