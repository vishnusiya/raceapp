/*
 Template Name: Stexo - Responsive Bootstrap 4 Admin Dashboard
 Author: Themesdesign
 Website: www.themesdesign.in
 File: C3 Chart init js
 */

!function($) {
    "use strict";

    var ChartC3 = function() {};

    ChartC3.prototype.init = function () {
        //generating chart 
        c3.generate({
            bindto: '#chart1',
            data: {
                columns: [
                ['Ticket Cost', 50, 30, 57, 10, 9],
                ],
                type: 'bar',
                colors: {
                    'Ticket Cost': '#588ef7',
                }
            },
            axis: {
                x: {
                    type: 'category',
                    categories: ['Gucci', 'Berluti', 'CCM Global', 'Christian Dior', 'Bimba']
                },
                y: {
                    tick: {
                            format: function (d) { return d + " S$"; }
                        }
                    }
                },
                bar: {
                    width:30
                }
            });

        
        c3.generate({
            bindto: '#chart2',
            data: {
                columns: [
                    ['Cost Applicable', 150, 100, 90, 152, 250],
                    ['Not Applicable', 230, 150, 120, 240, 180]
                ],
                type: 'bar',
                colors: {
                    'Cost Applicable': '#588ef7',
                    'Not Applicable': '#7bd172',
                }
            },   
            axis: {
                x: {
                    type: 'category',
                    categories: ['Gucci', 'Berluti', 'CCM Global', 'Christian Dior', 'Bimba']
                },
                y: {
                    tick: {
                            format: function (d) { return d + " S$"; }
                        }
                    }
                },
                bar: {
                    width:20
                }
            });

         c3.generate({
            bindto: '#chart3',
            data: {
                columns: [
                ['Total Cost Incurred', 50, 30, 57, 10, 9],
                ],
                type: 'bar',
                colors: {
                    'Total Cost Incurred': '#588ef7',
                }
            },
            axis: {
                x: {
                    type: 'category',
                    categories: ['Australia', 'Malaysia', 'Singapore', 'Thailand', 'Vietnam']
                },
                y: {
                    tick: {
                            format: function (d) { return d + " S$"; }
                        }
                    }
                },
                bar: {
                    width:30
                }
            });

         c3.generate({
            bindto: '#chart4',
            data: {
                columns: [
                ['Cost Incurred per sqm', 50, 30, 57, 10, 9],
                ],
                type: 'bar',
                colors: {
                    'Cost Incurred per sqm': '#588ef7',
                }
            },
            axis: {
                x: {
                    type: 'category',
                    categories: ['Westfield', 'Bondi', 'Tokyo', 'Alanka', 'Wuhan']
                },
                y: {
                    tick: {
                            format: function (d) { return d + " S$"; }
                        }
                    }
                },
                bar: {
                    width:30
                }
            });

        

    },
    $.ChartC3 = new ChartC3, $.ChartC3.Constructor = ChartC3

}(window.jQuery),

//initializing 
function($) {
    "use strict";
    $.ChartC3.init()
}(window.jQuery);



