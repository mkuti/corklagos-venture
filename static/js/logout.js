const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const logoutbtn = document.getElementById("logoutbtn");

const request = new Request(
    `${window.origin}/accounts/logout/`,
    {headers: {'X-CSRFToken': csrftoken}}
);

logoutbtn.addEventListener("click", function(e){
    e.preventDefault();
    fetch(request, {
        method: 'POST',
        mode: 'same-origin'  
    }).then(function(response) {
        console.log(response)
});

});
