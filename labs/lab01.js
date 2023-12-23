document.addEventListener('DOMContentLoaded', function () {
    const posterLinks = document.querySelectorAll('.poster-link');
    const popup = document.getElementById('popup');
    const popupPoster = document.getElementById('popupPoster');
    const closeBtn = document.getElementById('closeBtn');

    posterLinks.forEach(function (link) {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const posterUrl = link.getAttribute('data-poster-url');
            popupPoster.src = posterUrl;
            popup.style.display = 'flex';
        });
    });

    closeBtn.addEventListener('click', function () {
        popup.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });
});
