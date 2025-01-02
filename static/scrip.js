document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        // Отменяем стандартное поведение формы
        event.preventDefault();

        // Здесь можно добавить код для отправки данных в БД
        // Например, с помощью fetch или XMLHttpRequest

        // После успешной отправки данных показываем alert
        alert('Данные успешно отправлены!');

        // Если нужно, можно сбросить форму после отправки
        form.reset();
    });
});