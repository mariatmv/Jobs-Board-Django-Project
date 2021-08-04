window.onload = function() {
    let contactsButton = document.querySelector('#contacts-button');
    contactsButton.addEventListener('click', showContactDetails);


    function showContactDetails(event) {
        contactsButton.parentNode.removeChild(contactsButton);
        let contactDetails = document.querySelector('#contact-details');
        contactDetails.removeAttribute('hidden');
    }
};