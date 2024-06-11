document.addEventListener('DOMContentLoaded', () => {
	const accordions = document.querySelectorAll('.accordion');

	accordions.forEach(el => {
		el.addEventListener('click', (e) => {
			const self = e.currentTarget;
			const control = self.querySelector('.accordion__control');
			const content = self.querySelector('.accordion__content');

			// Закрываем все остальные аккордеоны
			accordions.forEach(otherEl => {
				if (otherEl !== self) {
					const otherControl = otherEl.querySelector('.accordion__control');
					const otherContent = otherEl.querySelector('.accordion__content');

					otherEl.classList.remove('open');
					otherControl.setAttribute('aria-expanded', false);
					otherContent.setAttribute('aria-hidden', true);
					otherContent.style.maxHeight = null;
				}
			});

			// Открываем или закрываем текущий аккордеон
			self.classList.toggle('open');

			if (self.classList.contains('open')) {
				control.setAttribute('aria-expanded', true);
				content.setAttribute('aria-hidden', false);
				content.style.maxHeight = content.scrollHeight + 'px';
			} else {
				control.setAttribute('aria-expanded', false);
				content.setAttribute('aria-hidden', true);
				content.style.maxHeight = null;
			}
		});
	});
});