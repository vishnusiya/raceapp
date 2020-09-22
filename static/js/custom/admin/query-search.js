(function (window) {
  HRC = {}
  HRC.page_url = ko.observable('');
  HRC.heading1 = ko.observable('');
  HRC.heading2 = ko.observable('');
  HRC.reslultsList = ko.observableArray([]);


  HRC.getCookie = function (name) {
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


  HRC.showLoading = function(){
      $(".loader-bg").removeClass('d-none');
      $(".no-data").removeClass('active');
  }
  HRC.hideLoading = function(){
    $(".loader-bg").addClass('d-none');
    $(".no-data").addClass('active');
  }

  HRC.showErrorModal = function(msg){
      $("#errorModal").modal('show');
      $("#errorMessage").text(msg);
    }

  
  HRC.querySearchSubmit = function(){
    var csrftoken = HRC.getCookie('csrftoken');
    var formdata = new FormData();
    formdata.append('page_url', HRC.page_url());
    $.ajax({
      method: 'POST',
      url: '/apprace/create/result/details',
      data: formdata,
      contentType: false,
      processData: false,
      beforeSend: function(xhr, settings) {
        HRC.showLoading();
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      HRC.showErrorModal(d)
      setTimeout(function() {
        location.reload()
      }, 1000);
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      HRC.showErrorModal(jQuery.parseJSON(jqXHR.responseText));
    })
    .always(function () {
        HRC.hideLoading();
      })
  }


  HRC.getAllResults = function () {
    var csrftoken = HRC.getCookie('csrftoken');
    $.ajax({
      method: 'GET',
      url: '/apprace/result/list/get',
      dataType: 'json',
      beforeSend: function (xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      })
      .done(function (d, textStatus, jqXHR) {
        console.log(d)
        HRC.reslultsList([]);
        for (var i = 0; i < d.length; i++) {
          HRC.reslultsList.push(d[i]);
        }        

        console.log( HRC.reslultsList())    

      })
      .fail(function (jqXHR, textStatus, errorThrown) {
        jsonValue = jQuery.parseJSON( jqXHR.responseText );
        alert(jsonValue)
      })
    }




})(this);

function init() {
if (document.readyState == "interactive") {
    HRC.hideLoading();
    HRC.getAllResults();
    ko.applyBindings(HRC);
}
}
document.onreadystatechange = init;