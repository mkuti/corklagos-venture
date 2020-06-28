const logoutbtn = document.getElementById("logoutbtn");
const logouturl = `${window.origin}/accounts/logout/`

/**
 * Add event listener to logout user when logout is clicked
 * @event click on logout navitem
 */
logoutbtn.addEventListener("click", function(){
    fetch(logouturl, {
        headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
        method: 'POST',
        mode: 'same-origin',
    }).then(function(response){
    }).then(() => {
        Swal.fire({
            title: "You've been logged out!",
            icon: "success",
            timer: 500,
            allowEscapeKey: false,
            allowOutsideClick: false,
            showConfirmButton: false,
        }).then((result) => {
            location.reload();
        })
    }).catch((err) => {
        console.log(err);
    });
});

