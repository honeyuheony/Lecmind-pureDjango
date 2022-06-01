let myChartOne = document.getElementById('myChartOne').getContext('2d');
let myChartTwo = document.getElementById('myChartTwo').getContext('2d');

let barChart = new Chart(myChartOne,{
    type : 'bar',
    data : {
        labels : ['객체지향개발론', '운영체제', '알고리즘 및 실습', '컴퓨터네트워크'],
        datasets : [{
            label : '강의별 평균 수강시간',
            data:[
                10,
                50,
                90,
                20
            ],
            backgroundColor:[
                '#FBF46D',
                '#B4FE98',
                '#77E4D4',
                '#998CEB'
            ]
        }]
    },
    options:{
        responsive: false,
    }
});

let barChartTwo = new Chart(myChartTwo,{
    type : 'doughnut',
    data : {
        labels : ['객체지향개발론', '운영체제', '알고리즘 및 실습', '컴퓨터네트워크'],
        datasets : [{
            label : '강의별 복습추천구간 비율',
            data:[
                20,
                10,
                60,
                35
            ],
            backgroundColor:[
                '#FBF46D',
                '#B4FE98',
                '#77E4D4',
                '#998CEB'
            ]
        }]
    },
    options:{
        responsive: false,
    }
});