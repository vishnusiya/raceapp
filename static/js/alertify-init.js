"use strict";

(function() {

    function $(selector) {
        return document.querySelector(selector);
    }

    function reset (ev) {
        ev.preventDefault();
        alertify.reset();
    }

    function logToast(selector) {
        (ga || function() { })("send", "event", "button", "click", "toastview", selector);
    }

    function toastview(selector, cb) {
        var el = $(selector);
        if(el) {
            el.addEventListener("click", function(ev) {
                ev.preventDefault();
                logToast(selector);
                cb();
            });
        }
    }

    var ga = ga || function() {};


    
})();