let center = [55.736812,37.692159];

function init() {
	let map = new ymaps.Map('map', {
		center: center,
		zoom: 17,
	});

    let placemark = new ymaps.Placemark(center, {
		balloonContent: `
			<div class="balloon">
				<div class="balloon__address">Умней для детей</div>
				<div class="balloon__contacts">
					<a href="tel:+78002006101">8 800 200-61-01</a>
				</div>
			</div>
		`
	}, {
	});

	map.controls.remove('geolocationControl'); // удаляем геолокацию
  map.controls.remove('searchControl'); // удаляем поиск
  map.controls.remove('trafficControl'); // удаляем контроль трафика
  map.controls.remove('typeSelector'); // удаляем тип
  map.controls.remove('fullscreenControl'); // удаляем кнопку перехода в полноэкранный режим
  map.controls.remove('zoomControl'); // удаляем контрол зуммирования
  map.controls.remove('rulerControl'); // удаляем контрол правил
  map.behaviors.disable(['scrollZoom']); // отключаем скролл карты (опционально)

  map.geoObjects.add(placemark);
}

ymaps.ready(init);

// Обработчик события на изменение значения в select
let select = document.querySelector('#select-city');
select.addEventListener('change', function() {
  let city = this.value;
  let geocoder = ymaps.geocode(city);

  geocoder.then(function(res) {
    let coords = res.geoObjects.get(0).geometry.getCoordinates();
    setCenter(coords);
  });
});
