/*
 Template Name: Stexo - Responsive Bootstrap 4 Admin Dashboard
 Author: Themesdesign
 Website: www.themesdesign.in
 File: C3 Chart init js
 */

  CCM.client_id = ko.observable(0);
  CCM.country_id = ko.observable(0);
  CCM.store_id = ko.observableArray([]);
  CCM.client_list = ko.observableArray([]);
  CCM.country_list = ko.observableArray([]);
  CCM.store_list = ko.observableArray([]);
  CCM.main_ids_list = ko.observableArray([]);
  CCM.from_date = ko.observable('');
  CCM.to_date = ko.observable('');
  CCM.user_timezone = ko.observable('');


  CCM.getDashboardClients = function () {
    var csrftoken = CCM.getCookie('csrftoken');
    $.ajax({
      method: 'GET',
      url: '/account/api/dashboard/clients/get',
      dataType: 'json',
      beforeSend: function (xhr, settings) {
        GBL.showLoading();
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
         })
      .done(function (d, textStatus, jqXHR) {
        CCM.client_list([]);
        for (var i = 0; i < d.length; i++) {
          CCM.client_list.push(d[i]);
        }
        CCM.selectedDashboardClientCountryStoresids();
        CCM.country_list.push({id: 0, country__name: "All"});
        $('#filterClient').attr("disabled", false);
        $('#filterClient').trigger('change').select2({tags: false});
        setTimeout(function() {
          $('#filterCountry').trigger('change').select2({tags: false});
        }, 10);
        
      })
      .fail(function (jqXHR, textStatus, errorThrown) {
        jsonValue = jQuery.parseJSON( jqXHR.responseText );
        var errormessage = ''
        for (index = 0; index < jsonValue.errors.length; index++) {
            errormessage = errormessage + jsonValue.errors[index].message; 
        }
        alertify.error(errormessage)
      })
      .always(function () {
        GBL.hideLoading();
      })
    }


  CCM.getDashboardCountries = function (data, e) { 
      var csrftoken = CCM.getCookie('csrftoken');
      var formdata = {
        'client_id': CCM.client_id(),
      }
      $.ajax({
        method: 'GET',
        url: '/account/api/dashboard/countries/get',
        data: formdata,
        datatype: 'json',
        beforeSend: function (xhr, settings) {
          GBL.showLoading();
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      })
      .done(function (d, textStatus, jqXHR) {
        console.log(d)
        CCM.country_list([]);
        for (var i = 0; i < d.length; i++) {
          CCM.country_list.push(d[i]);
        }
        CCM.selectedDashboardClientCountryStoresids();

         $('#filterStore').multiselect('destroy');  
          $('#filterStore').val(0);
          $('#filterStore').attr("disabled", true);
          
          $('#filterStore').multiselect({
            nonSelectedText: 'Select',
            includeSelectAllOption: true,
            enableFiltering: true,
            buttonWidth: '100%',
            maxHeight: 400,
          });


        if(CCM.client_id()==0){
          $('#filterCountry').attr("disabled", true);                  
        }else{          
          $('#filterCountry').attr("disabled", false);
        }
        $('#filterCountry').trigger('change').select2({tags: false});
      })
      .fail(function (jqXHR, textStatus, errorThrown) {
        jsonValue = jQuery.parseJSON( jqXHR.responseText );
        var errormessage = ''
        for (index = 0; index < jsonValue.errors.length; index++) {
            errormessage = errormessage + jsonValue.errors[index].message + "<br>"; 
        }
        alertify.error(errormessage)
      })
      .always(function () {
        GBL.hideLoading();
          })
    };


    $('#filterStore').multiselect({
        nonSelectedText: 'Select',
        includeSelectAllOption: true,
        enableFiltering: true,
        buttonWidth: '100%',
        maxHeight: 400,
      }); 


  CCM.getDashboardStores = function (data, e) {
      var csrftoken = CCM.getCookie('csrftoken');
      var formdata = {
        'country_id': CCM.country_id(),'client_id': CCM.client_id(),
      }
      $.ajax({
        method: 'GET',
        url: '/account/api/dashboard/stores/get',
        data: formdata,
        datatype: 'json',
        beforeSend: function (xhr, settings) {
          GBL.showLoading();
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      })
        .done(function (d, textStatus, jqXHR) {
          CCM.store_list([]);
          for (var i = 0; i < d.length; i++) {
            CCM.store_list.push(d[i]);
          }
          CCM.selectedDashboardClientCountryStoresids();


          $('#filterStore').multiselect('destroy');
          $('#filterStore').attr("disabled", false);
          if(CCM.country_id()==0){
            $('#filterStore').attr("disabled", true);
          }
         
            setTimeout(function() {
              $('#filterStore').multiselect({
                nonSelectedText: 'Select',
                includeSelectAllOption: true,
                enableFiltering: true,
                buttonWidth: '100%',
                maxHeight: 400,
                onSelectAll: function() {
                  CCM.store_id([0]);
                  CCM.selectedDashboardClientCountryStoresids();
                },
                onDeselectAll: function() {
                    CCM.store_id();
                }
              });               
            }, 0);

          
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
          jsonValue = jQuery.parseJSON( jqXHR.responseText );
          var errormessage = ''
          for (index = 0; index < jsonValue.errors.length; index++) {
              errormessage = errormessage + jsonValue.errors[index].message + "<br>"; 
          }
          alertify.error(errormessage)
        })
        .always(function () {
          GBL.hideLoading();
        })
    }


  CCM.reloadClick = function(){
    location.reload()
  }

  CCM.selectedDashboardClientCountryStoresids = function (data, e) {
      var csrftoken = CCM.getCookie('csrftoken');
      var formdata = {
        'country_id': CCM.country_id(),'client_id': CCM.client_id(),'store_id': ko.toJSON(CCM.store_id()),'from_date': CCM.from_date(),'to_date': CCM.to_date(),
      }
      $.ajax({
        method: 'GET',
        url: '/account/api/dashboard/client/country/stores/ids/get',
        data: formdata,
        datatype: 'json',
        beforeSend: function (xhr, settings) {
          GBL.showLoading();
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      })
        .done(function (d, textStatus, jqXHR) {
          // console.log('d',d)
          var yAxisData1 = d.average_reaction_y_axis;
          yAxisData1.unshift('Average Reaction Time');

          c3.generate({
            bindto: '#chart1',
            data: {
                columns: [
                yAxisData1,
                // ['Average Reaction Time', 50, 30, 57, 10, 9],
                ],
                type: 'bar',
                colors: {
                    'Average Reaction Time': '#588ef7',
                }
            },
            zoom: {
        enabled: true
    },
            axis: {
                x: {
                    type: 'category',
                    categories: d.average_reaction_x_axis
                    // categories: ['Gucci', 'Berluti', 'CCM Global', 'Christian Dior', 'Bimba']
                },
                y: {
                    tick: {
                            format: function (d) { return d + " hr"; }
                        }
                    }
                },
                bar: {
                    width:30
                }
            });


          var yAxisData2 = d.average_closing_y_axis;
          yAxisData2.unshift('Average Closing Time');

          c3.generate({
            bindto: '#chart2',
            data: {
                columns: [
                yAxisData2,
                // ['Average Closing Time', 50, 30, 57, 10, 9],
                ],
                type: 'bar',
                colors: {
                    'Average Closing Time': '#588ef7',
                }
            },
            zoom: {
        enabled: true
    },
            axis: {
                x: {
                    type: 'category',
                    categories: d.average_closing_x_axis
                    // categories: ['Gucci', 'Berluti', 'CCM Global', 'Christian Dior', 'Bimba']
                },
                y: {
                    tick: {
                            format: function (d) { return d + " hr"; }
                        }
                    }
                },
                bar: {
                    width:30
                }
            });




          var opened_by_bar_y_axis_client = d.opened_by_bar_y_axis_client;
          var opened_by_bar_y_axis_staff = d.opened_by_bar_y_axis_staff;
          var opened_by_bar_y_axis_total = d.opened_by_bar_y_axis_total;
          opened_by_bar_y_axis_client.unshift('Clients');
          opened_by_bar_y_axis_staff.unshift('Staff');
          opened_by_bar_y_axis_total.unshift('Total');

           c3.generate({
            bindto: '#chart3',
            data: {
                columns: [
                opened_by_bar_y_axis_client,
                opened_by_bar_y_axis_staff,
                opened_by_bar_y_axis_total
                // ['Clients', 50, 30, 57, 10, 9],
                // ['Staff', 10, 50, 27, 5, 10],
                // ['Total', 20, 10, 60, 10, 1],
                ],
                type: 'bar',
                colors: {
                    'Clients': '#588ef7',
                    'Staff': '#7bd172',
                    'Total': '#efd765',
                }
            },
            zoom: {
        enabled: true
    },
            axis: {
              y: {
                  tick: { format: d3.format("d") }
              },
                x: {
                    type: 'category',
                    categories: d.opened_by_bar_x_axis
                    // categories: ['Australia', 'Malaysia', 'Singapore', 'Thailand', 'Vietnam']
                },
                },
                bar: {
                    width:13
                }
            });

           console.log('d.opened_by_line_x_axis',d.opened_by_line_x_axis)
           console.log('d.opened_by_line_y_axis_staff',d.opened_by_line_y_axis_staff)
           // var xAxisData4 = d.opened_by_line_x_axis;
           // xAxisData4.unshift('x');

           var opened_by_line_y_axis_staff = d.opened_by_line_y_axis_staff;
           var opened_by_line_y_axis_client = d.opened_by_line_y_axis_client;
           opened_by_line_y_axis_client.unshift('Clients');
           opened_by_line_y_axis_staff.unshift('Staff');



           c3.generate({
                bindto: '#chart4',
                padding: {
                  right: 10
              },
              data: {
                // x: 'x',
                columns: [
                // xAxisData4,
                opened_by_line_y_axis_client,
                opened_by_line_y_axis_staff
                // ['x', '2020-12-01', '2020-01-01', '2020-03-01', '2020-04-01', '2020-04-01', '2020-06-01'],
                // ['Clients', 30, 200, 100, 400, 150, 250],
                // ['Staff', 30, 50, 80, 500, 100, 150]
                ],
                type: 'line',
                colors: {
                    'Clients': '#273d6b',
                    // 'Staff': '#588ef7',
                }
            },
            zoom: {
        enabled: true
    },
            axis : {
                y: {
                  tick: { format: d3.format("d") },
                  min:1
                },
                x : {
                    type: 'category',
                    categories: d.opened_by_line_x_axis,
                    // categories: d.opened_by_line_x_axis,
                    extent: [0, 6],
                    tick: {
                      fit:false,
                    },
                        height: 60
                    }
                }
            });



           visitation_y_axis = d.visitation_y_axis;
           visitation_y_axis.unshift('No of Visits');
           c3.generate({
            bindto: '#chart5',
            data: {
                columns: [
                // ['No of Visits', 40, 50, 10, 20, 30],
                visitation_y_axis,
                // ['No of Visits', 40, 50, 10, 20, 30],
                ],
                type: 'bar',
                colors: {
                    'No of Visits': '#588ef7',
                }
            },
            zoom: {
        enabled: true
    },
            axis: {
                x: {
                    type: 'category',
                    categories: d.visitation_x_axis
                    // categories: ['Gucci', 'Berluti', 'CCM Global', 'Christian Dior', 'Bimba']
                },
                y: {
                  tick: { format: d3.format("d") },
                  min:1
                },
                },
                bar: {
                    width:30
                }
            });


        })
        .fail(function (jqXHR, textStatus, errorThrown) {
          jsonValue = jQuery.parseJSON( jqXHR.responseText );
          var errormessage = ''
          for (index = 0; index < jsonValue.errors.length; index++) {
              errormessage = errormessage + jsonValue.errors[index].message + "<br>"; 
          }
          alertify.error(errormessage)
        })
        .always(function () {
          GBL.hideLoading();
        })
      }




!function($) {
    "use strict";

    var ChartC3 = function() {};

    ChartC3.prototype.init = function () {
        //generating chart 
        
        
        
        

         

        

    },
    $.ChartC3 = new ChartC3, $.ChartC3.Constructor = ChartC3

}(window.jQuery),

//initializing 
function($) {
    "use strict";
    $.ChartC3.init()
    // var tz = moment.tz.guess();
    // CCM.user_timezone(tz)
    CCM.getDashboardClients();
    CCM.selectedDashboardClientCountryStoresids();
    CCM.getBaseProfileImage();
}(window.jQuery);

