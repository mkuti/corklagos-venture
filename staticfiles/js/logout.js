const logoutbtn = document.getElementById("logoutbtn");
const logouturl = `${window.origin}/accounts/logout/`

logoutbtn.addEventListener("click", function(){
    fetch(logouturl, {
        headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
        method: 'POST',
        mode: 'same-origin',
    }).then(function(response){
    }).then(() => {
        location.reload();
    }).catch((err) => {
        console.log(err);
    });
});

