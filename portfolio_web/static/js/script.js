const slides = document.querySelectorAll('.hero .slide');
let currentSlide = 0;

function showSlide(slideIndex) {
    slides.forEach((slide, index) => {
        if (index === slideIndex) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });
}

var swiper = new Swiper('.swiper-container', {
    loop: false, // Disable infinite loop
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

setInterval(nextSlide, 5000); // Change slide every 5 seconds
