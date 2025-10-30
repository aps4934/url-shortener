document.getElementById('shorten-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const originalUrl = document.getElementById('original-url').value;
    const resultDiv = document.getElementById('result');
    const shortUrlInput = document.getElementById('short-url');
    const loadingDiv = document.getElementById('loading');
    const submitBtn = document.getElementById('submit-btn');

    // Show loading state
    loadingDiv.style.display = 'block';
    resultDiv.style.display = 'none';
    submitBtn.disabled = true;
    submitBtn.textContent = 'Shortening...';

    try {
        const response = await fetch('/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: originalUrl })
        });

        const data = await response.json();
        if (response.ok) {
            shortUrlInput.value = data.short_url;
            resultDiv.style.display = 'block';
            // Scroll to result
            resultDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
            alert(data.error || 'An error occurred');
            resultDiv.style.display = 'none';
        }
    } catch (error) {
        alert('Failed to connect to server. Please try again.');
        resultDiv.style.display = 'none';
    } finally {
        // Hide loading state
        loadingDiv.style.display = 'none';
        submitBtn.disabled = false;
        submitBtn.textContent = 'Shorten URL';
    }
});

function copyToClipboard() {
    const shortUrlInput = document.getElementById('short-url');
    const copyMessage = document.getElementById('copy-message');

    shortUrlInput.select();
    shortUrlInput.setSelectionRange(0, 99999);

    try {
        document.execCommand('copy');
        copyMessage.style.display = 'block';
        setTimeout(() => {
            copyMessage.style.display = 'none';
        }, 2000);
    } catch (err) {
        alert('Failed to copy to clipboard. Please copy manually.');
    }
}

// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link:not(.cta-nav)');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Add scroll effect to navbar
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(10, 10, 10, 0.98)';
        } else {
            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
        }
    });

    // Add interactive effects to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Add interactive effects to step cards
    const stepCards = document.querySelectorAll('.step-card');
    stepCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 15px 35px rgba(0, 0, 0, 0.1)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = 'none';
        });
    });


});
