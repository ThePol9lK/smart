AOS.init({
  once:true
});

let burger = document.querySelector(".burger");
let menu = document.querySelector(".header-nav");
let mainMenuItems = document.querySelectorAll(".header-nav__list > .header-nav__item"); // Получаем все элементы основного меню

// Клонируем элементы "Вход" и "Регистрация" из основного меню
let loginItem = mainMenuItems[mainMenuItems.length - 2].cloneNode(true); // Клонируем предпоследний элемент
let registerItem = mainMenuItems[mainMenuItems.length - 1].cloneNode(true); // Клонируем последний элемент

burger.addEventListener("click", function(){
  burger.classList.toggle("burger_active");
  menu.classList.toggle("header__nav_brg-anim");
  document.body.classList.toggle("stop-scroll");
});

// Добавляем клонированные элементы в бургер-меню
menu.querySelector(".header-nav__list").appendChild(loginItem);
menu.querySelector(".header-nav__list").appendChild(registerItem);

loginItem.classList.add("header-nav__item--burger");
registerItem.classList.add("header-nav__item--burger");