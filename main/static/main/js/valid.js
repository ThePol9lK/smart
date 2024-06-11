let form = document.querySelector(".form");
let triggerForm = false;

// INPUTMASK -------------------------------

let selector = document.querySelector("input[type='tel']");
let im = new Inputmask("+7 (999)-999-99-99");
im.mask(selector);

// -----------------------------------------

// JUST VALIDATE ---------------------------
// Форма обратной связи
new JustValidate(".js-form-connection", {
    rules: {

        name: {
            required: true,
            minLength: 2,
            maxLength: 30,
        },

        tel: {
            required: true,
            function: (name, value) => {
                const phone = selector.inputmask.unmaskedvalue();
                console.log(phone);
                return Number(phone) && phone.length === 10;
            },
        },
    },

    messages: {
        name: {
            required: 'Поле обязательно к заполнению ',
            minLength: 'Необходимо ввести имя целиком',
            maxLength: 'Необходимо ввести только имя',
        },

        tel: {
            required: 'Поле обязательно к заполнению ',
            function: 'Некорректный ввод',
        },
    },

    tooltip: {
        fadeOutTime: 4000,
    },
    colorWrong: 'var(--pink)',

    // Если ввод верный, то - код ниже (Form)
    submitHandler: function (form, values, ajax) {
        triggerForm = true;

        // form.classList.remove("animate__delay-1s");
        form.classList.add("animate__fadeOutLeft");
        console.log("Верный ввод сработал")
        setTimeout(function () {
            form.classList.add("hide-block");
        }, 2500);
        setTimeout(function () {
            form.classList.remove("hide-block");
            form.classList.remove("animate__fadeOutLeft");animate__fadeInUp
            form.classList.remove("animate__fadeInUp");
        }, 2500);
    },
});

$(document).ready(function () {
// //E-mail Ajax Send
// $(".form").submit(function () { //Change
//     if(!triggerForm){
//         return false;
//     }
//     var th = $(this);
//     $.ajax({
//         type: "POST",
//         url: "http://cz34920.tw1.ru/mail-connect.php", //Change
//         data: th.serialize()
//     }).done(function (e) {
//         console.log(e);
//         setTimeout(function () {
//             // Done Functions
//             th.trigger("reset");
//         }, 1000);
//     }).fail(function (error) {
//         console.log(error);
//     });
//     return false;
// });


});