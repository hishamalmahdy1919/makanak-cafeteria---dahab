document.addEventListener('DOMContentLoaded', function () {
  // تحديث السنة في الفوتر
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // إغلاق قائمة اللغات عند النقر خارجها
  document.addEventListener('click', function (e) {
    var menu = document.getElementById('langMenu');
    var toggle = document.querySelector('.lang-toggle');
    if (!menu || !toggle) return;
    if (!menu.contains(e.target) && !toggle.contains(e.target)) {
      menu.classList.remove('open');
    }
  });

  // إغلاق القائمة الجانبية للموبايل عند الضغط على أي رابط
  document.querySelectorAll('.mobile-nav a').forEach(function (a) {
    a.addEventListener('click', function () {
      document.getElementById('mobileNav').classList.remove('open');
    });
  });

  // تشغيل الـ Slideshow لصور الهيرو (تبديل الصور مع النصوص)
  const slides = document.querySelectorAll('.hero-slideshow .slide');
  if (slides.length > 0) {
    let currentSlide = 0;
    setInterval(function() {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 5000); // تغيير الصورة كل 5 ثواني
  }
});