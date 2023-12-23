document.addEventListener('DOMContentLoaded', function () {
    const filterInput = document.getElementById('filterMovie');
    const messageTable = document.getElementById('movieTable');
    const rows = messageTable.getElementsByTagName('tr');
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

    filterInput.addEventListener('input', function () {
        const filter = filterInput.value.toLowerCase();

        for (let i = 1; i < rows.length; i++) {
            const watchedDate = rows[i].getElementsByTagName('td')[0].textContent.toLowerCase();
            const rating = rows[i].getElementsByTagName('td')[1].textContent.toLowerCase();
            const movieName = rows[i].getElementsByTagName('td')[2].textContent.toLowerCase();
            const runtime = rows[i].getElementsByTagName('td')[3].textContent.toLowerCase();
            const tags = rows[i].getElementsByTagName('td')[4].textContent.toLowerCase();

            if (watchedDate.includes(filter)
                || rating.includes(filter)
                || movieName.includes(filter)
                || runtime.includes(filter)
                || tags.includes(filter)) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    });
});