(function($) {

    　 //el操纵对象，option属性值

    　
    $.love = function(el, option) {

        　　　　
        var lo = $(el);

        　　　　
        lo.vars = $.extend({}, $.love.default, option); //合并成新对象，则是新的属性列表

        　　　　 //定义其他属性

        　　　　
        var method = {};

        　　　　 //私有方法,私有方法之间可互相调用

        　　　　
        method = {

            　　　　
            functionA: function() {
                console.log("functionA called");
            },

            　　　　functionB: function() {
                console.log("functionB called");
            },

            　　　　functionC: function() {
                console.log("functionC called");
            }　　　　
        }

        　　　　 //公有方法（特权方法），供类外调用

        　　　　
        this.publicFunction = function(a, b) {

            lo.css({
                "color": "white",
                "background-color": "#98bf21",
                "width": "300px",
                "height": "200px",
                "padding": "5px"
            });　　　　　

            /*调用私有函数*/

            　　　　　　
            method.functionA();　　　　
        }　
    }

    　 //可设置默认属性

    　
    $.love.default = {

        　　
        width: 500,

        height: 400　
    }

})(jQuery);