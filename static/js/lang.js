function googleTranslateElementInit() {
    new google.translate.TranslateElement({/*pageLanguage: 'en',*/includedLanguages: 'en,pt', layout: google.translate.TranslateElement.InlineLayout.SIMPLE, autoDisplay: false}, 'google_translate_element');
  }
  
var selectedLang;

$(".dropdown-menu").find("a").click(function() {
  var newElem = "<div class='line lineAnimation'><div class='sixth-color'>"+$(this).html()+"</div></div>";

  $(".line").remove();

  $("#line-container").append(newElem);
  
  setTimeout(function() {
    $(newElem).remove();
  }, 6250);
 });

function translateLanguage(lang) {
      var $frame = $('.goog-te-menu-frame:first');
      if (!$frame.size()) {
          alert("Error: Could not find Google translate frame.");
          return false;
      }

      switch(lang) {
        case 'en':
          if(selectedLang != 'en') {
            $frame.contents().find('a').get(0).click();
            break;
          }
          break;
        case 'pt':
          if(selectedLang != 'pt') {
            $frame.contents().find('a').get(1).click();
            break;
          }
          break;
      }

      selectedLang = lang;

      return false;
  }  