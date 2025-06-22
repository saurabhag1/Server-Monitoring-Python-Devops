fetch("/metrics").then(res => res.json()).then(data => {
    const cpuUsage = data.local.cpu;
    new Chart(document.getElementById("cpuChart"), {
        type: 'doughnut',
        data: {
            labels: ["CPU Usage", "Free"],
            datasets: [{
                data: [cpuUsage, 100 - cpuUsage],
                backgroundColor: ["#f00", "#0f0"]
            }]
        }
    });
});
