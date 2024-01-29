// animations.js

document.addEventListener('DOMContentLoaded', function () {
    // Header animations
    anime.timeline({ easing: 'easeOutExpo' })
        .add({
            targets: '.animated-header',
            translateY: [-50, 0],
            opacity: [0, 1],
            duration: 1200,
            delay: 500
        })
        .add({
            targets: '.animated-subtitle',
            translateY: [50, 0],
            opacity: [0, 1],
            duration: 1200,
            offset: '-=1000'
        });

    // Section title animations
    anime.timeline({ easing: 'easeOutExpo' })
        .add({
            targets: '.animated-title',
            translateY: [50, 0],
            opacity: [0, 1],
            duration: 1200,
            delay: anime.stagger(200)
        });

    // Portfolio item animations
    anime({
        targets: '.animated-item',
        translateY: [50, 0],
        opacity: [0, 1],
        duration: 1200,
        delay: anime.stagger(200, { start: 1000 })
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const menuBtn = document.getElementById('menu-btn');
    const menuContent = document.getElementById('menu-content');

    menuBtn.addEventListener('click', function () {
        menuContent.classList.toggle('show');
    });

    window.addEventListener('resize', function () {
        if (window.innerWidth > 768) {
            menuContent.classList.remove('show');
        }
    });
});