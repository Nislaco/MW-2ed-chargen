cted option is found, set it as checked
    if (selectedOption !== null) {
        radios[selectedOption].checked = true;
    }

    // Listen for form submission
    unitForm.addEventListener('submit', function() {
        const selectedValue = document.querySelector('input[name="option"]:checked').value;
        
        // Save the selected option to local storage
        localStorage.setItem('selectedOption', selectedValue);
    });
});
