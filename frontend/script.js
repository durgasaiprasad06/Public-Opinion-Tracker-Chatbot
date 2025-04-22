let chart = null;

async function analyze() {
    const topic = document.getElementById('topicInput').value.trim();
    if (!topic) return;

    try {
        const response = await fetch('http://localhost:5000/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic })
        });

        const data = await response.json();
        
        if (data.error) {
            alert(`Error: ${data.error}`);
            return;
        }

        updateUI(data);
        document.getElementById('results').classList.remove('hidden');
    } catch (error) {
        alert('Failed to analyze. Please try again.');
    }
}

function updateUI(data) {
    // Update chart
    if (chart) chart.destroy();
    
    const ctx = document.getElementById('sentimentChart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Negative', 'Neutral'],
            datasets: [{
                data: [data.sentiment.positive, data.sentiment.negative, data.sentiment.neutral],
                backgroundColor: ['#10b981', '#ef4444', '#64748b']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });

    // Update points
    document.getElementById('positivePoints').innerHTML = data.positive_points
        .map(point => `<li>${point}</li>`)
        .join('');

    document.getElementById('negativePoints').innerHTML = data.negative_points
        .map(point => `<li>${point}</li>`)
        .join('');

    // Update analysis
    document.getElementById('impactAnalysis').textContent = data.impact_analysis;
    document.getElementById('summary').textContent = data.summary;
}