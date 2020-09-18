(function (window) {

  $(document).on('keypress','.pagination-input',function( event ) {
    if ( event.which == 13 ) {
       var _this = $(this)
       setTimeout(function() {
       _this.closest('.pagination-input-group').find('.input-group-append button').trigger('click');
       }, 0);
    }
  });

    GBL = {}
    CCM = {}
    CCM.userprofile__profile_pic = ko.observable('');
  
     $('.modal').on('hidden.bs.modal', function (e) {
      $('.modal span.error').remove();
    })
    
    GBL.showError = function(){
      GBL.showErrorModal('Feature not implemented');
    }
    GBL.showLoading = function(){
      $(".loader-bg").removeClass('d-none');
      $(".no-data").removeClass('active');
    }
    GBL.hideLoading = function(){
      $(".loader-bg").addClass('d-none');
      $(".no-data").addClass('active');
    }
    GBL.showToast = function(msg){
      $(".toast").text(msg).addClass('active');
      setTimeout(function(){
        GBL.hideToast();
      }, 3000);
    }
    GBL.hideToast = function() {
      $(".toast").removeClass('active');
    }
    GBL.showErrorModal = function(msg){
      $("#errorModal").modal('show');
      $("#errorMessage").text(msg);
    }


    CCM.getCookie = function(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    };

    CCM.getBaseProfileImage = function () {
        var csrftoken = CCM.getCookie('csrftoken');
        $.ajax({
          method: 'GET',
          url: '/account/api/base/userprofile/image/get',
          dataType: 'json',
          beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        })
        .done(function (d, textStatus, jqXHR) {
          if(d.userprofile__profile_pic__path == ''){
           CCM.userprofile__profile_pic ('/static/images/user1.png')
          }else{
            CCM.userprofile__profile_pic(d.userprofile__profile_pic__path)
          }

          // CCM.userprofile__profile_pic(d.userprofile__profile_pic__path)
        })
        .fail( function (jqXHR, textStatus, errorThrown) {
          console.log('notification failed')
        })
      }
  
  
    $(document).on("hidden.bs.modal", function (e) { 
      if ($('.modal:visible').length) { 
          $('body').addClass('modal-open');
      }
    });
  
    $(document).on("keypress", ".form-control", function(e) {
      if (e.which === 32 && !this.value.length){
        e.preventDefault();
      }
    });
  
    ko.bindingHandlers.popover = {
      init: function (element, valueAccessor) {
        var local = ko.utils.unwrapObservable(valueAccessor()),
        options = {};
  
        ko.utils.extend(options, ko.bindingHandlers.popover.options);
        ko.utils.extend(options, local);
  
        $(element).popover(options);
  
        ko.utils.domNodeDisposal.addDisposeCallback(element, function () {
          $(element).popover("dispose");
        });
      },
      options: {
        placement: "top",
        trigger: "hover"
      }
    };
  
    ko.bindingHandlers.select2 = {
      init: function(el, valueAccessor, allBindingsAccessor, viewModel) {
        ko.utils.domNodeDisposal.addDisposeCallback(el, function() {
          $(el).select2('destroy');
        });
  
        var allBindings = allBindingsAccessor(),
            select2 = ko.utils.unwrapObservable(allBindings.select2);
  
        $(el).select2(select2);
      },
      update: function (el, valueAccessor, allBindingsAccessor, viewModel) {
          var allBindings = allBindingsAccessor().select2;
  
          if ("value" in allBindings) {
  
              if ((allBindings.multiple || el.multiple) && allBindings.value().constructor != Array) {                
                  $(el).val(allBindings.value().split(',')).trigger('chaCCM');
              }
              else {
                  $(el).val(allBindings.value()).trigger('chaCCM');
              }
  
              // if ((allBindings.select2.multiple || el.multiple)) {                
              //   $(el).val(allBindings.value()).trigger('chaCCM');
              // }
              // else {
              //   $(el).val(allBindings.value()).trigger('chaCCM');
              // }
          } else if ("selectedOptions" in allBindings) {
              var converted = [];
              var textAccessor = function(value) { return value; };
              if ("optionsText" in allBindings) {
                  textAccessor = function(value) {
                      var valueAccessor = function (item) { return item; }
                      if ("optionsValue" in allBindings) {
                          valueAccessor = function (item) { return item[allBindings.optionsValue]; }
                      }
                      var items = $.grep(allBindings.options(), function (e) { return valueAccessor(e) == value});
                      if (items.length == 0 || items.length > 1) {
                          return "UNKNOWN";
                      }
                      return items[0][allBindings.optionsText];
                  }
              }
              $.each(allBindings.selectedOptions(), function (key, value) {
                  converted.push({id: value, text: textAccessor(value)});
              });
              $(el).select2("data", converted);
          }
          $(el).trigger("chaCCM");
      }
    };
  
    $(document).on('select2:opening.disabled', ':disabled', function() { return false; })
    
  })(this);


  function init() {
if (document.readyState == "interactive") {
    GBL.hideLoading();  
    
    ko.applyBindings(CCM);
}
}
document.onreadystatechange = init;