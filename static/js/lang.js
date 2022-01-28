function googleTranslateElementInit() {
    new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'en,pt', layout: google.translate.TranslateElement.InlineLayout.SIMPLE, autoDisplay: false}, 'google_translate_element');
  }
  
 

  function translateLanguage(lang) {
      var $frame = $('.goog-te-menu-frame:first');
      if (!$frame.size()) {
          alert("Error: Could not find Google translate frame.");
          return false;
      }
      $frame.contents().find('.goog-te-menu2-item span.text:contains(' + lang + ')').get(0).click();
  
      $("a").click(function() {   
        $("#line").addClass("lineAnimation");
        $("#line").find("div").html($(this).html());
    
        setTimeout(function() {
          $("#line").removeClass("lineAnimation");
        }, 6250);
       });

      return false;
  }  