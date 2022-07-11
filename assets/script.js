var slide = document.querySelector('.image-container');
var btn1 = document.querySelector('#btn1');
var btn2 = document.querySelector('#btn2');
var btn3 = document.querySelector('#btn3');
var btn4 = document.querySelector('#btn4');


// btn1.onclick = function() {
//     slide.style.transform = "translateX(0px)";
// }
btn1.addEventListener('click', () => {
    slide.style.transform = "translateX(-0px)";
})
btn2.onclick = function() {
    slide.style.transform = "translateX(-25%)";
}
btn3.onclick = function() {
    slide.style.transform = "translateX(-50%)";
}
btn4.onclick = function() {
    slide.style.transform = "translateX(-75%)";
}

var spans = document.querySelectorAll('span');

spans.forEach(span => {
    span.addEventListener('click', function() {
        spans.forEach(span => span.classList.remove('active'));
        span.classList.add('active');
    })
})