document.addEventListener('DOMContentLoaded', () => {
    // Slider Logic
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    let currentSlide = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.remove('active');
            if (i === index) {
                slide.classList.add('active');
            }
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
    }

    if (prevBtn && nextBtn) {
        nextBtn.addEventListener('click', nextSlide);
        prevBtn.addEventListener('click', prevSlide);

        // Auto play
        setInterval(nextSlide, 5000);
    }

    // Gallery "Read" functionality (Simple alert for academic demo)
    const readIcons = document.querySelectorAll('.read-icon');
    readIcons.forEach(icon => {
        icon.addEventListener('click', (e) => {
            const item = e.target.closest('.gallery-item');
            const title = item.querySelector('h4').innerText;
            alert(`Explanation for ${title}:\n\nThis value is computed in real-time by the Python backend. It represents a key metric in the face tracking pipeline.`);
        });
    });
});
