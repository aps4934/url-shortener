document.getElementById('shorten-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const originalUrl = document.getElementById('original-url').value;
    const resultDiv = document.getElementById('result');
    const shortUrlInput = document.getElementById('short-url');

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
        } else {
            alert(data.error || 'An error occurred');
            resultDiv.style.display = 'none';
        }
    } catch (error) {
        alert('Failed to connect to server');
        resultDiv.style.display = 'none';
    }
});

function copyToClipboard() {
    const shortUrlInput = document.getElementById('short-url');
    shortUrlInput.select();
    shortUrlInput.setSelectionRange(0, 99999);
    document.execCommand('copy');
    alert('Copied to clipboard: ' + shortUrlInput.value);
}
