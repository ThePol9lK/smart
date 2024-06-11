// РАБОТА С МОДАЛЬНЫМ ОКНОМ
let module = document.querySelector(".modal"); // Находим все обертки для модального окна
let moduleBox = document.querySelector(".modal__box"); // Находим сами модальные окна
let moduleOpenBtn = document.querySelectorAll(".modal__btn"); // Находим все кнопки для вызова модлаьного окна
console.log(moduleOpenBtn)
if(moduleOpenBtn.length == 0){
    let moduleOpenBtn = document.querySelectorAll(".educate__link");
    console.log(moduleOpenBtn)
}
let moduleCloseBtn = document.querySelector(".modal__btn-wrapper"); // Находим Кнопку закрытия модального окна

// ОТКРЫТИЕ МОДАЛЬНОГО ОКНА
moduleOpenBtn.forEach(function(element, index){
  element.addEventListener("click", function(){
    moduleBox.classList.remove("animate__fadeOutDown");
    module.classList.add("open");
    moduleBox.classList.add("animate__backInDown");
    moduleCloseBtn.classList.add("animate__bounceInDown");
    document.body.classList.add("stop-scroll");
  });
});

// ЗАКРЫТИЕМОДАЛЬНОГО ОКНА
moduleCloseBtn.addEventListener("click", function(){
    moduleBox.classList.remove("animate__fadeInDown");
    moduleCloseBtn.classList.remove("animate__bounceInDown");
    moduleBox.classList.add("animate__fadeOutDown");
    setTimeout(function() {
      module.classList.remove("open");
      document.body.classList.remove("stop-scroll");
    }, 900);
});

// ЗАКРЫТИЕ ОКНА ПРИ ПРОЖАТИИ КНОПКИ Esc
window.addEventListener('keydown', (e) => {
  if (e.key === "Escape") {
    moduleBox.classList.remove("animate__fadeInDown");
    moduleCloseBtn.classList.remove("animate__bounceInDown");
    moduleBox.classList.add("animate__fadeOutDown");
    setTimeout(function() {
      module.classList.remove("open");
      document.body.classList.remove("stop-scroll");
    }, 900);
  }
});

// Закрыть модальное окно при клике вне его
moduleBox.addEventListener('click', event => {
  event._isClickWithInModal = true;
});
module.addEventListener('click', event => {
  if (event._isClickWithInModal) return;
  moduleBox.classList.remove("animate__fadeInDown");
    moduleCloseBtn.classList.remove("animate__bounceInDown");
    moduleBox.classList.add("animate__fadeOutDown");
    setTimeout(function() {
      module.classList.remove("open");
      document.body.classList.remove("stop-scroll");
    }, 900);
});
