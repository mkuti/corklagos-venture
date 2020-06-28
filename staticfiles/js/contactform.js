const contactForm = document.getElementById('contact-form')
console.log(contactForm)
const message = document.getElementById('jsmessage')

/**
 * Add event listener to send email via emailjs when contactform is submitted
 * @event submit on input with type submit of the form
 */
contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                emailjs.sendForm('contact_service', 'contact_form', this);
                alert("Your email has been sent")
                location.reload()
            });
    