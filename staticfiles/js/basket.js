// basket.js

document.addEventListener('DOMContentLoaded', () => {
    const basket = [];
    const basketItemsEl = document.getElementById('basketItems');
    const basketTotalEl = document.getElementById('basketTotal');

    const addButtons = document.querySelectorAll('.add-to-basket-btn');

    addButtons.forEach(button => {
        button.addEventListener('click', () => {
            const name = button.dataset.name;
            const price = parseFloat(button.dataset.price);
            const id = button.dataset.id;

            basket.push({ id, name, price });

            basketItemsEl.innerHTML = '';

            let total = 0;
            basket.forEach(item => {
                const li = document.createElement('li');
                li.className = 'list-group-item d-flex justify-content-between align-items-center';
                li.textContent = item.name;
                const span = document.createElement('span');
                span.className = 'badge bg-secondary rounded-pill';
                span.textContent = `$${item.price.toFixed(2)}`;
                li.appendChild(span);
                basketItemsEl.appendChild(li);
                total += item.price;
            });

            basketTotalEl.textContent = total.toFixed(2);
        });
    });
});
