const contactForm = document.getElementById('contact-form')

/**
 * Add event listener to send email via emailjs when contactform is submitted
 * @event submit on input with type submit of the form
 */
contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                emailjs.sendForm('contact_service', 'contact_form', this)
                .then(function(response) {
                    Swal.fire({
                    title: "Your email has been sent!",
                    icon: "success",
                    timer: 500,
                    allowEscapeKey: false,
                    allowOutsideClick: false,
                    showConfirmButton: false,
                }).then((result) => {
                    window.location.replace("/")
                })
                }, function(error) {
                    console.log('FAILED...', error);
                    Swal.fire({
                    title: "Something did not go right, please try again.",
                    icon: "error",
                    timer: 500,
                    allowEscapeKey: false,
                    allowOutsideClick: false,
                    showConfirmButton: false,
                })
                });
            });
    