/**
 * Upon DOM creation completion the containing functions are called if conditions met.
 */
$(function () {
    containerHeightHandling();
    if (window.location.pathname == "/"){
        homepageProductSelection(bootstrapDetectBreakpoint());
        homepageJumbotronMobileBackground(bootstrapDetectBreakpoint());
    };
}
);

/**
 * Sets the height of two main components used on PrintCrate: the main page content
 * container and the jumbotron container.
 * The heights of the header and footer are subtracted from the height of the viewport
 * and the minimum height of the main content is set to the result.
 * Jumbotron height disregards the footer as is intended for better layout.
 */
function containerHeightHandling(){
    const viewportHeight = window.innerHeight;
    const headerHeight = $("nav").outerHeight();
    const footerHeight = $("footer").outerHeight();
    $(".main-container").first().css("min-height", viewportHeight - headerHeight - footerHeight);
    $(".jumbotron").css("margin-bottom", 0);
    $(".jumbotron").outerHeight(viewportHeight - headerHeight);
}

/**
 * PrintCrate site URL is copied to the user's clipboard, a success modal is displayed.
 * Action triggered upon selecting the hyperlink image located in the footer.
 */
$("#clipboard-url").click(function(){
    new ClipboardJS("#clipboard-url");
    swal.fire({
        icon: "success",
        text:"Site URL copied to clipboard.",
        timer: 3000,
    });
})

/**
 * Hides the third showcase product on smaller displays for better site flow / layout.
 * @param {object} breakpoint Details the active breakpoint: name and "index".
 */
function homepageProductSelection(breakpoint){
    if (breakpoint.index < 3) {
        $(".product-container").eq(2).hide();
    }
}

/**
 * Displays "amend" button on quantity field change if new quantity is different from the
 * original quantity requested.
 */
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

/**
 * Button to remove item from cart triggers a confirmation modal on activation.
 * If user then activates confirmation button the item is removed from cart.
 */
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

/**
 * A template used for constructing a fetch request to the backend.
 * @param {object} fetchInputData Data to be passed in the fetch to be handled by backend.
 * @param {string} identifyingHeader Header for backend to easily recognise the handling to be done.
 * @returns {object} Returns data required for the fetch request in a standardised method.
 */
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

if(window.location.href.match("products/search")){
    $("#empty-items-list-declaration").append(" that match your search criteria.")
    const searchAddition = $("#search-query").text();
    const formattedSearchAddition = searchAddition.replace(/ /g,"+");
    ($(".pagination-control")).map(function () {
        const defaultPaginator = $(this).attr("href");
        const formattedPaginator = defaultPaginator.substring(1, defaultPaginator.length);
        $(this).attr("href", `search?search_query=${formattedSearchAddition}&${formattedPaginator}`);
    });
}