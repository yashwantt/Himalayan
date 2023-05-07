document.addEventListener("DOMContentLoaded", function(){ 
  //  DOM is ready
  var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    // slidesPerGroup: 3,
    loop: false,
    // loopFillGroupWithBlank: true,
    centerSlide:'true',
    fade:'true',
    grabCursor:'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets:true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints:{
        0:{
            slidesPerView: 1,
        },
        750:{
            slidesPerView: 2,
        },
        950:{
            slidesPerView: 3,
        },
    },
  });
});

