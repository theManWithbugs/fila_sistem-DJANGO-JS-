function redirectNewSolci() {
    window.location.replace("http://127.0.0.1:8000/home/nova_solicitacao/");
}

const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Collum1', 'Collum2', 'Collum3', 'Collum4',
            'Collum5', 'Collum6'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1,
            backgroundColor: [
                '#00CED1', '#DC143C','#FFA500', '#B0C4DE',
                '#F4A460', '#F0F8FF'
            ],
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});



