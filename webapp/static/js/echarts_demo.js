$(document).ready(
    function () {
        generate_pie_chart();
        setInterval(generate_pie_chart, 60000);
    }
);


function generate_pie_chart() {
    var options = {
        type: "GET",
        url: "http://127.0.0.1:5001/EchartsApi/pie",
        dataType: "json",
        async: true,
        success: function (echarts_data) {
            var myChart = document.getElementById('pie');
            var myChart = echarts.init(myChart, 'macarons');
            var option = {
                title: {
                    text: 'Pie Demo',
                    left: 'center',
                    top: 20,
                    textStyle: {
                        color: '#ccc'
                    }
                },
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },
                legend: {
                    type: 'scroll',
                    orient: 'vertical',
                    x: 'left',
                    data: echarts_data['legend']
                },
                series: [
                    {
                        name: 'pie_demo',
                        type: 'pie',
                        radius: ['50%', '70%'],
                        avoidLabelOverlap: true,
                        label: {
                            normal:{
                                show:false,
                                position: 'center'
                            },
                            emphasis: {
                                show: true,
                                textStyle: {
                                    fontSize: '30',
                                    fontWeight: 'bold'
                                }
                            }
                        },
                        data: echarts_data['data']
                    }
                ]
            };

            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });

        }
    }
    $.ajax(options);
}