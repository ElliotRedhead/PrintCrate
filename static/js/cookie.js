/**
 * Retrieves the target cookie from user.
 * credit: https://stackoverflow.com/questions/19333098/403-forbidden-error-when-making-an-ajax-post-request-in-django-framework/26100613#26100613
 * @param {string} name The name of the cookie to access.
 * @returns {string} The value of the cookie.
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrftoken = getCookie("csrftoken");