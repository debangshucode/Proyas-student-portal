// Ensure all variables are declared
var loader = document.getElementById('preeloader');
var contactLink = document.getElementById('contact-link');
var contactPopup = document.getElementById('contact-popup');
var overlay = document.getElementById('overlay');
var filter = document.getElementById('filter');
var allNotes = document.querySelectorAll('.sub_notes');
var slideIndex = 1;

// Event listener for window load
window.addEventListener('load', function() {
    loader.style.display = 'none';
});

// Event listener for contact link
if (contactLink) {
    contactLink.addEventListener('click', function(e) {
        e.preventDefault();
        showPopup();
    });
}

// Event listener for close button
var closeButton = document.getElementById('close-popup');
if (closeButton) {
    closeButton.addEventListener('click', function() {
        hidePopup();
    });
}

// Event listener for overlay click
if (overlay) {
    overlay.addEventListener('click', function() {
        hidePopup();
    });
}

// Show popup function
function showPopup() {
    if (contactPopup && overlay) {
        contactPopup.style.display = 'block';
        overlay.style.display = 'block';
    }
}

// Hide popup function
function hidePopup() {
    if (contactPopup && overlay) {
        contactPopup.style.display = 'none';
        overlay.style.display = 'none';
    }
}

// Show more notes function
function showMoreNotes() {
    var hiddenNotes = document.querySelectorAll('.sub_notes[style="display: none;"]');
    var visibleCount = 0;
    for (var i = 0; i < hiddenNotes.length && visibleCount < 5; i++) {
        var note = hiddenNotes[i];
        var semesterMatch = filter.value === 'none' || note.dataset.semester === filter.value;
        if (semesterMatch) {
            note.style.display = 'flex';
            visibleCount++;
        }
    }
}

// Show less notes function
function showLessNotes() {
    var visibleNotes = document.querySelectorAll('.sub_notes[style="display: flex;"]');
    var hiddenCount = 0;
    for (var i = visibleNotes.length - 1; i >= 0 && hiddenCount < 5; i--) {
        var note = visibleNotes[i];
        var semesterMatch = filter.value === 'none' || note.dataset.semester === filter.value;
        if (semesterMatch) {
            note.style.display = 'none';
            hiddenCount++;
        }
    }
    noteCounter -= hiddenCount;
}
if (filter) {
    filter.addEventListener('change', filterNotes);
}

// Filter notes function
function filterNotes() {
    const selectedSemester = filter.value;
    let visibleCount = 0;
    for (let i = 0; i < allNotes.length; i++) {
        const note = allNotes[i];
        const semesterMatch = selectedSemester === 'none' || note.dataset.semester === selectedSemester;
        if (semesterMatch) {
            if (visibleCount < 5) {
                note.style.display = 'flex';
                visibleCount++;
            } else {
                note.style.display = 'none';
            }
        } else {
            note.style.display = 'none';
        }
    }
}
document.addEventListener('DOMContentLoaded', function() {
    var initialNotes = document.querySelectorAll('.sub_notes');
    for (var i = 5; i < initialNotes.length; i++) {
        initialNotes[i].style.display = 'none';
    }
});

// Show slides function
function showSlides(n) {
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (var i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    captionText.innerHTML = dots[slideIndex-1].alt;
}

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

// Initially show slides
showSlides(slideIndex);

// Attach event listener for filter change
if (filter) {
    filter.addEventListener('change', filterNotes);
}
