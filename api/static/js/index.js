function wordcloud(keywords) {

     var e = document.getElementById("wc");

        //e.firstElementChild can be used.
        var child = e.lastElementChild;
        while (child) {
            e.removeChild(child);
            child = e.lastElementChild;
        }


    var fill = d3.scale.category20();
    d3.layout.cloud().size([550, 290])
        .words(
            Object.keys(keywords).map(function (key, value) {
                console.log(key)
                console.log(value)
                return {text: key, size: value * 6};

//        return {text: d[0], size: 10 + Math.random() * 50};
            }))
        .padding(5)
        .rotate(function () {
            return ~~(Math.random() * 0) * 90;
        })
        .font("Impact")
        .fontSize(function (d) {
            return d.size;
        })
        .on("end", draw)
        .start();

    function draw(words) {
        d3.select(document.getElementById('wc')).append("svg")
            .attr("width", 550)
            .attr("height", 290)
            .append("g")
            .attr("transform", "translate(250,150)")
            .selectAll("text")
            .data(words)
            .enter().append("text")
            .style("font-size", function (d) {
                return d.size + "px";
            })
            .style("font-family", "Impact")
            .style("fill", function (d, i) {
                return fill(i);
            })
            .attr("text-anchor", "middle")
            .attr("transform", function (d) {
                return "translate(" + [d.x,d.y] + ")rotate(" + d.rotate + ")";
            })
            .text(function (d) {
                return d.text;
            });
    }
}

(function ($) {
    $(document).ready(function () {
        $('#btn-wc').click(function () {
            ShowCustomDialog();
        });
    });


    function ShowCustomDialog() {

        ShowDialogBox('WordCloud', 'Record updated successfully.', 'Close', '', 'GoToAssetList', null);
    }

    function ShowDialogBox(title, content, btn1text, btn2text, functionText, parameterList) {
        var btn1css;
        var btn2css;

        if (btn1text == '') {
            btn1css = "hidecss";
        } else {
            btn1css = "showcss";
        }

        if (btn2text == '') {
            btn2css = "hidecss";
        } else {
            btn2css = "showcss";
        }
        $("#lblMessage").html(content);

        $("#dialog").dialog({
            resizable: false,
            title: title,
            modal: true,
            width: '400px',
            height: 'auto',
            bgiframe: false,
            hide: {effect: 'scale', duration: 400},

            buttons: [
                {
                    text: btn1text,
                    "class": btn1css,
                    click: function () {

                        $("#dialog").dialog('close');

                    }
                },
                {
                    text: btn2text,
                    "class": btn2css,
                    click: function () {
                        $("#dialog").dialog('close');
                    }
                }
            ]
        });
    }
})(jQuery);

