console.log("hhhhhh")

/* ------------------ toggle navbar ------------------*/

const navtoggler = document.querySelector(".nav-toggler");
navtoggler.addEventListener("click", togglenav);

function togglenav() {
    navtoggler.classList.toggle("active")
    document.querySelector(".nav").classList.toggle("open");
}

/*----- close navbar when clicking on an item --------*/
document.addEventListener("click", function(e) {
    if (e.target.closest(".nav-item")) {
        togglenav();
    }
})

/* ------------------- sticky header -------------------*/
// window.addEventListener("scroll", function() {
//     if (this.pageXOffset > 60) {
//         document.querySelector(".header").classList.add("sticky");
//     } else {
//         document.querySelector(".header").classList.remove("sticky");
//     }
// });
// console.log(pageYOffset)



// slide function

function first() {
    document.getElementById("slide").src = "/static/imgs/3.jpg"
}

function second() {
    document.getElementById("slide").src = "/static/imgs/6.jpg"
}

function third() {
    document.getElementById("slide").src = "/static/imgs/7.jpg"
}


function fourth() {
    document.getElementById("slide").src = "/static/imgs/10.jpg"
}
setInterval(first, 3000);
setInterval(second, 6000);
setInterval(third, 9000);
setInterval(fourth, 12000);


// menu start
const menutabs = document.querySelector(".menu-tabs");
menutabs.addEventListener("click", function(e) {
    if (e.target.classList.contains("menu-tab-item") && !e.target.classList.contains("active")) {
        const target = e.target.getAttribute("data-target");
        menutabs.querySelector(".active").classList.remove("active");
        console.log(target)
        e.target.classList.add("active");
        const menusection = document.querySelector(".menu-section");
        menusection.querySelector(".menu-tab-content.active").classList.remove("active");
        menusection.querySelector(target).classList.add("active");
    }
})



//   all ------------------
function initParadoxWay() {
    "use strict";

    if ($(".testimonials-carousel").length > 0) {
        var j2 = new Swiper(".testimonials-carousel .swiper-container", {
            preloadImages: false,
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            grabCursor: true,
            mousewheel: false,
            centeredSlides: true,
            pagination: {
                el: '.tc-pagination',
                clickable: true,
                dynamicBullets: true,
            },
            navigation: {
                nextEl: '.listing-carousel-button-next',
                prevEl: '.listing-carousel-button-prev',
            },
            breakpoints: {
                1024: {
                    slidesPerView: 3,
                },

            }
        });
    }

    // bubbles -----------------


    setInterval(function() {
        var size = randomValue(sArray);
        $('.bubbles').append('<div class="individual-bubble" style="left: ' + randomValue(bArray) + 'px; width: ' + size + 'px; height:' + size + 'px;"></div>');
        $('.individual-bubble').animate({
            'bottom': '100%',
            'opacity': '-=0.7'
        }, 4000, function() {
            $(this).remove()
        });
    }, 350);

}

//   Init All ------------------
$(document).ready(function() {
    initParadoxWay();
});

// review form
const open = document.getElementById('open');
const modal_container = document.getElementById('modal-container');
const close = document.getElementById('close');

open.addEventListener('click', () => {
    modal_container.classList.add('show')
})
close.addEventListener('click', () => {
    modal_container.classList.remove('show')
})










// var swiper = new Swiper(".review-slider", {
//     spaceBetween: 20,
//     centeredSlides: true,
//     autoplay: {
//         delay: 7500,
//         disableOnInteraction: false,
//     },
//     loop: true,
//     breakpoints: {
//         0: {
//             slidesPerView: 1,
//         },
//         640: {
//             slidesPerView: 2,
//         },
//         768: {
//             slidesPerView: 2,
//         },
//         1024: {
//             slidesPerView: 3,
//         },
//     },
// });





















// // var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
// var now = new Date();
// y = now.getFullYear();
// d = now.getDate();

// var m = now.getMonth(); // getMonth method returns the month of the date (0-January :: 11-December)
// m = m + 1;
// var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

// function convertDate(date_str) {
//     temp_date = date_str.split("-");
//     return temp_date[2] + " " + months[Number(temp_date[1]) - 1] + " " + temp_date[0];
// }
// sp = convertDate(y + " - " + m + " - " + d);
// document.getElementById("date").innerHTML = sp;
// // var output = document.getElementById('output');

// // console.log(thisMonth);

// // if (output.textContent !== undefined) {
// //     output.textContent = m + " /" + d + " /" + y;
// // } else {
// //     output.innerText = m + " /" + d + " /" + y;
// // }
// // document.getElementById("date").innerHTML = d + "/" + y;



// // console.log(m)
// // console.log(convertDate(y + " - " + m + " - " + d));