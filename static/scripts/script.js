/* Validates the data entered in the contact form */
function validate() {
    let myform = document.forms['contactform']
    message = ''
    if (myform['nume'].value == '') {
        message += 'Numele nu poate fi nul\n'
    }
    if (myform['email'].value == '') {
        message += 'Email nu poate fi nul\n'
    }
    if (myform['mesaj'].value == '') {
        message += 'Mesajul nu poate fi nul\n'
    }
    if (message != '') {
        alert(message)
    } else {
        alert('Mesajul a fost trimis cu success.')
    }
}