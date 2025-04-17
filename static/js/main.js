document.addEventListener('DOMContentLoaded', function() {
    // слайдерок
    const newsSlider = document.querySelector('.news-slider');
    if (newsSlider) {
        let isDown = false;
        let startX;
        let scrollLeft;

        newsSlider.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.pageX - newsSlider.offsetLeft;
            scrollLeft = newsSlider.scrollLeft;
        });

        newsSlider.addEventListener('mouseleave', () => {
            isDown = false;
        });

        newsSlider.addEventListener('mouseup', () => {
            isDown = false;
        });

        newsSlider.addEventListener('mousemove', (e) => {
            if(!isDown) return;
            e.preventDefault();
            const x = e.pageX - newsSlider.offsetLeft;
            const walk = (x - startX) * 2;
            newsSlider.scrollLeft = scrollLeft - walk;
        });
    }

    // валидка
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            let valid = true;
            const inputs = this.querySelectorAll('input[required], textarea[required]');

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.borderColor = 'red';
                    valid = false;
                } else {
                    input.style.borderColor = '';
                }
            });

            if (!valid) {
                e.preventDefault();
                alert('Пожалуйста, заполните все обязательные поля');
            }
        });
    });
});




