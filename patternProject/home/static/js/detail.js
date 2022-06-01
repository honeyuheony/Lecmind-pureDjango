let chartOne = document.getElementById('chartOne').getContext('2d');
let chartTwo = document.getElementById('chartTwo').getContext('2d');

// let timelines = document.getElementById('timelines');
// var ctx = timelines.getContext('2d');



let barChart = new Chart(chartOne, {
    type: 'line',
    data: {
        labels: ['1차시', '2차시', '3차시', '4차시', '5차시', '6차시'],
        datasets: [{
            label: '차시 별 복습추천구간 빈도수',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: false,
        layout: {
            padding: {
                left: 50,
                bottom: 20
            }
        },
    }
});


var cmpTimeChart = {
    labels: ['1차시', '2차시', '3차시', '4차시', '5차시', '6차시'],
    datasets: [{
        label: '강의시간',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
            '#fabed7'
        ],
    }, {
        label: '수강시간',
        data: [20, 9, 12, 6, 3, 5],
        backgroundColor: [
            '#f768a1'
        ],
    }]
};

let barChartTwo = new Chart(chartTwo, {
    type: 'bar',
    data: cmpTimeChart,
    options: {
        responsive: false,
        layout: {
            padding: {
                left: 50,
                bottom: 20
            }
        },
    }
});

function makeSpot() {
    var spot_list = document.querySelector('.timeline');
    var spot = document.createElement("li");
    spot.setAttribute('time-spot', '00:00'); //(속성명:속성값(초기값)) , 데이터 삽입
    spot_list.append(spot);
}


// // 타임스탬프
// ctx.beginPath();
// ctx.moveTo(0,0);
// ctx.lineTo(600,0);
// ctx.stroke();

// //start지점
// ctx.moveTo(40,40);
// ctx.lineTo(40,60);
// ctx.stroke();

// //end지점
// ctx.moveTo(600,40);
// ctx.lineTo(600,60);
// ctx.stroke();
