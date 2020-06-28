const contactForm = document.getElementById('contact-form')
console.log(contactForm)

contactForm.addEventListener('submit', function(event) {
                event.preventDefault();
                // generate the contact number value
                this.contact_number.value = Math.random() * 100000 | 0;
                emailjs.sendForm('contact_service', 'contact_form', this);
                alert("Your mail is sent!");
                location.reload()
            });
    