document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const uploadButton = document.getElementById('uploadButton');
    const fileNameSpan = document.getElementById('fileName');
    const loader = document.getElementById('loader');
    const reviewContainer = document.getElementById('review-container');
    const reportFileName = document.getElementById('reportFileName');
    const reviewReportDiv = document.getElementById('review-report');

    // Trigger file input when the custom button is clicked
    uploadButton.addEventListener('click', () => {
        fileInput.click();
    });

    // Handle file selection
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            const file = fileInput.files[0];
            fileNameSpan.textContent = file.name;
            handleFileUpload(file);
        } else {
            fileNameSpan.textContent = 'No file chosen';
        }
    });

    async function handleFileUpload(file) {
        // Show loader and hide previous report
        loader.style.display = 'block';
        reviewContainer.style.display = 'none';

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/review', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            
            if (result.error) {
                displayError(result.error);
            } else {
                displayReport(result);
            }

        } catch (error) {
            console.error('Error during file upload:', error);
            displayError('An error occurred while communicating with the server.');
        } finally {
            // Hide loader
            loader.style.display = 'none';
        }
    }

    function displayReport(data) {
        reportFileName.textContent = data.filename;
        // Use the 'marked' library to convert markdown to HTML
        reviewReportDiv.innerHTML = marked.parse(data.report);
        reviewContainer.style.display = 'block';
    }

    function displayError(errorMessage) {
        reportFileName.textContent = 'Error';
        reviewReportDiv.innerHTML = `<p style="color: red; font-weight: bold;">${errorMessage}</p>`;
        reviewContainer.style.display = 'block';
    }
});