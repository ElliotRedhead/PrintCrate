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

$(".quantity-input").change(function(){
    newItemQuantity = this.value;
    itemId = this.itemId;
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
            "Custom-Fetch": true,
            "X-CSRFToken": csrftoken,
            "X-Requested-With": "XMLHttpRequest"
        }),
		body: JSON.stringify(fetchInputData)
	};
	return fetchParameters;
}