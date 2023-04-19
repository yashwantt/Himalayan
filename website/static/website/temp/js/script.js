$(document).ready(()=>{
    // DOM is Ready
    function closePopUp(){
        $('.headerUl').removeClass('active');
        $('#popUp').removeClass('blocker');
    }
// NAVIGATION --> HAMBURGER-BUTTON-EVENTS
    $('#hamburgerOpenBtn').click(()=>{
        $('.headerUl').addClass('active');
        $('#popUp').addClass('blocker');
    })
    $('#hamburgerCloseBtn').click(closePopUp);
    $('#popUp').click(closePopUp);
    
// NavBar
    $(".navListAnchor").click(closePopUp);
// STICKY AND NAV-Bar scroll 

    $(window).scroll(()=>{
        // Sticky 
        if(window.scrollY >= 300){
            $('.go-top').addClass('active');
        }else{
            $('.go-top').removeClass('active');
        }

        // navbar scroll 
        let headerHeight = $('.header').height();
        if(window.scrollY >=( headerHeight/3)){
            $('.headerNav').addClass('backgroundColor');
        }else{
            $('.headerNav').removeClass('backgroundColor');
        }
    })

// Footer quick links
    $('.footer-pop-div').click(()=>{
        $('.footer-pop-div').removeClass('footer-active');
    });

    $('popup-close-btn').click(()=>{
        $('.footer-pop-div').removeClass('footer-active');
    });
    //privacy policy
    $('#privacy-policy').click(()=>{
        console.log('pp')
        $('#pp-popup').addClass('footer-active');
    });

    // cancellation policy
    $('#cancellation-policy').click(()=>{
        console.log('cp')
        $('#cp-popup').addClass('footer-active');
    });

    // terms and cond
    $('#terms-and-cond').click(()=>{
        console.log('t&c')
        $('#tc-popup').addClass('footer-active');
    });

    //disclaimer
    $('#disclaimer-policy').click(()=>{
        console.log('disc')
        $('#d-popup').addClass('footer-active');
    });

    // about us
    $('#about-us').click(()=>{
        $('#a-popup').addClass('footer-active');
        console.log('about')
    });
})