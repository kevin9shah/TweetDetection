document.getElementById('tweetForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const tweetText = document.getElementById('tweetText').value;
    if (!tweetText.trim()) {
        alert('Please enter a tweet');
        return;
    }

    // Show loading state
    const button = e.target.querySelector('button');
    const originalButtonText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
    button.disabled = true;

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: tweetText })
        });

        const data = await response.json();
        
        // Display results
        const resultDiv = document.getElementById('result');
        const predictionSpan = document.getElementById('prediction');
        const predictionIcon = document.getElementById('predictionIcon');
        const probabilitySpan = document.getElementById('probability');
        const progressFill = document.querySelector('.circular-progress-fill');
        
        // Update prediction text and icon
        predictionSpan.textContent = data.prediction;
        if (data.prediction === 'Disaster') {
            predictionIcon.className = 'fas fa-exclamation-triangle';
            predictionIcon.style.color = '#dc3545';
            progressFill.style.stroke = '#dc3545';
        } else {
            predictionIcon.className = 'fas fa-check-circle';
            predictionIcon.style.color = '#28a745';
            progressFill.style.stroke = '#28a745';
        }
        
        // Update probability with animation
        const probability = (data.probability * 100).toFixed(2);
        probabilitySpan.textContent = '0';
        
        // Animate the circular progress
        setTimeout(() => {
            const circumference = 565.48; // 2 * π * r (r = 90)
            const offset = circumference - (probability / 100) * circumference;
            progressFill.style.strokeDashoffset = offset;
            
            // Animate the number counter
            let currentProb = 0;
            const animationDuration = 1000; // 1 second
            const interval = 10; // Update every 10ms
            const steps = animationDuration / interval;
            const increment = probability / steps;
            
            const counter = setInterval(() => {
                currentProb += increment;
                if (currentProb >= probability) {
                    currentProb = probability;
                    clearInterval(counter);
                }
                probabilitySpan.textContent = currentProb.toFixed(2);
            }, interval);
        }, 100);

        // Show result with animation
        resultDiv.style.display = 'block';
        
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while processing your request');
    } finally {
        // Restore button state
        button.innerHTML = originalButtonText;
        button.disabled = false;
    }
}); 